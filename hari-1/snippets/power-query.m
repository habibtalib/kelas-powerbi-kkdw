// power-query.m
// Rujukan transformasi Power Query (bahasa M) untuk data KKDW.
// Anda boleh tampal kod ini dalam Power Query Editor > Home > Advanced Editor,
// ATAU lakukan setiap langkah melalui antara muka (GUI) seperti dalam README/lab.
//
// Ganti laluan fail dengan lokasi sebenar data/*.xlsx di komputer anda.
//
// SUMBER (pilih satu):
//  A) Fail tempatan (Power BI Desktop):    Excel.Workbook(File.Contents("C:\...\data_jpd.xlsx"), null, true)
//  B) OneLake / Lakehouse Files (Fabric):  guna ADLS Gen2 — bukan "Browse SharePoint/OneDrive"
//     (sambungan Excel SharePoint selalu gagal; ADLS Gen2 baca terus fail dalam Lakehouse Files).
//
//     let
//         Source = AzureStorage.DataLake(
//             "https://onelake.dfs.fabric.microsoft.com/KKDW Copilot/KKDW_Lakehouse.Lakehouse/Files"
//         ),
//         Fail  = Table.SelectRows(Source, each [Name] = "data_jpd.xlsx"){0}[Content],
//         Sheet = Excel.Workbook(Fail, true){[Item="Sheet1", Kind="Sheet"]}[Data],
//         NaikTajuk = Table.PromoteHeaders(Sheet, [PromoteAllScalars = true])
//     in NaikTajuk
//     // Auth: Organizational account. Boleh guna nama atau GUID workspace/lakehouse dalam URL.

// ============================================================
// 1) JPD — bersihkan jadual fakta Jalan Perhubungan Desa
//    (Sumber A ditunjukkan; tukar ke Sumber B untuk OneLake.)
// ============================================================
let
    Source = Excel.Workbook(
        File.Contents("C:\Kursus-PowerBI\data\data_jpd.xlsx"), null, true
    ),
    Sheet = Source{[Item = "Sheet1", Kind = "Sheet"]}[Data],
    NaikTajuk = Table.PromoteHeaders(Sheet, [PromoteAllScalars = true]),

    // Tetapkan jenis data
    UbahJenis = Table.TransformColumnTypes(NaikTajuk, {
        {"kod_projek", type text},
        {"nama_projek", type text},
        {"kos_projek", Currency.Type},
        {"panjang_jalan", type number},
        {"jumlah_projek_peserta", Int64.Type},
        {"kod_negeri", type text},
        {"kod_daerah", type text},
        {"status_pelaksanaan", type text},
        {"lat_1", type number}, {"long_1", type number},
        {"tahun", Int64.Type}
    }),

    // Buang lajur teknikal yang tidak digunakan
    BuangLajur = Table.RemoveColumns(UbahJenis,
        {"created_at", "updated_at", "tarikh_upload"}, MissingField.Ignore),

    // Kemas teks medan kunci (Trim + UPPERCASE untuk padanan konsisten)
    KemasTeks = Table.TransformColumns(BuangLajur, {
        {"status_pelaksanaan", each Text.Upper(Text.Trim(_)), type text},
        {"kod_negeri", Text.Trim, type text},
        {"kod_daerah", Text.Trim, type text}
    }),

    // Lajur bersyarat: kategori status ringkas (untuk visual status konsisten)
    KategoriStatus = Table.AddColumn(KemasTeks, "kategori_status", each
        if [status_pelaksanaan] = "PASCA PELAKSANAAN" then "Siap"
        else if [status_pelaksanaan] = "DALAM PELAKSANAAN" then "Dalam Pelaksanaan"
        else "Belum Mula / Lain", type text),

    // Tandakan program (untuk Append dengan BELB)
    TandaProgram = Table.AddColumn(KategoriStatus, "program", each "JPD", type text)
in
    TandaProgram

// ============================================================
// 2) BELB — ulang langkah yang sama, program = "BELB"
//    (Salin blok di atas, tukar fail ke data_belb.xlsx,
//     tambah {"nama_kampung", type text}, program = "BELB".)
// ============================================================

// ============================================================
// 3) Projek_Program — Append JPD + BELB jadi satu jadual
//    Home > Append Queries as New > pilih JPD & BELB.
//    Hanya lajur sepunya dikekalkan untuk analisis merentas program.
// ============================================================
// = Table.Combine({JPD, BELB})

// ============================================================
// 4) (Lanjutan) Merge kewangan MyProjek ke Projek_Program
//    ikut kunci kod_projek, kemudian kembangkan lajur kewangan.
// ============================================================
// let
//     Gabung = Table.NestedJoin(Projek_Program, {"kod_projek"},
//                  MyProjek, {"kod_projek"}, "mp", JoinKind.LeftOuter),
//     Kembang = Table.ExpandTableColumn(Gabung, "mp",
//                  {"peratus_jadual_projek", "peratus_sebenar_projek",
//                   "kos_keseluruhan", "baki_kos_de"})
// in
//     Kembang
