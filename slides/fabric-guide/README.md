# Panduan Visual: Fabric + Copilot (Tangkapan Skrin Sebenar)

Tangkapan skrin **sebenar** dari tenant Fabric semasa persediaan kelas KKDW — untuk diselitkan ke dalam slaid (SESI 2, Hari 1 & SESI Copilot, Hari 3). Semua guna workspace **KKDW Copilot** (kapasiti F2) dan data sebenar JPD/BELB/MyProjek.

## Bahagian A — Persediaan Fabric + Copilot (tadbir urus)
Dilakukan sekali oleh pentadbir sebelum kelas:
1. **Start Fabric trial** (Account manager) — *nota: kapasiti trial TIDAK termasuk Copilot; guna kapasiti berbayar F2+*.
2. Cipta **workspace jenis Fabric** (bukan Template App) pada kapasiti F2.
3. **Admin portal → Tenant settings → Copilot and AI:**
   - "Users can use Copilot…" = **On**
   - "Data sent to Azure OpenAI can be **processed outside** your capacity's geographic region" = **On** ← wajib kerana kapasiti di **Malaysia West** (tiada Azure OpenAI). ⚠️ Keputusan residensi data — sahkan dengan pematuhan KKDW.
4. **Azure portal** → sahkan kapasiti **Active, F2, Malaysia West**.

> ✅ **Tangkapan skrin:** `14-workspace-type-fabric.jpg` — Workspace settings → **Workspace type** (Fabric · SKU F2 · Malaysia West). Kapasiti Fabric = sumber Azure `Microsoft.Fabric/capacities`. *(Versi disunting untuk repo awam ada di `hari-1/img/setup-fabric-capacity.jpg`.)*

### Microsoft Entra & tenant — rujukan pentadbir

**Microsoft Entra ID** (dahulu **Azure AD**) ialah lapisan **identiti/tenant**. Semua log masuk Fabric / Power BI / Copilot disahkan di sini, dan **kapasiti Fabric ialah sumber Azure dalam tenant yang sama**. Log masuk mesti guna akaun **dalam tenant yang memiliki kapasiti** — jika tidak, akses kapasiti/Copilot gagal.

**Peranan yang diperlukan:**

| Tugas | Peranan (Entra / Fabric) |
|------|--------------------------|
| Dayakan Copilot / tetapan AI, RLS peringkat tenant | **Fabric admin** / **Power BI admin** (Admin portal) |
| Urus kapasiti (assign workspace, resize, pause) | **Capacity admin** |
| Umpuk lesen Power BI/Fabric kepada pengguna | **Global admin** / **License admin** |

**Langkah tenant (sekali oleh pentadbir):**
1. Sahkan **tenant pemilik kapasiti** = tenant yang peserta log masuk (`az account show` → `tenantId`; kapasiti `synctexts` berada dalam tenant ini).
2. **Umpuk lesen** Power BI **Pro/PPU** kepada peserta (Entra → Users → Licenses) — perlu untuk **publish & kongsi** (Hari 2).
3. **Dayakan Copilot:** Admin portal → **Tenant settings → Copilot and AI = On** (+ consent proses luar rantau kerana kapasiti **Malaysia West**).
4. **Assign workspace** ke kapasiti **F2** (Workspace settings → Workspace type → Fabric).

**Perangkap tenant biasa (punca ralat "tiada akses"):**
- Log masuk Fabric dengan **akaun tenant berbeza / guest** → tak nampak kapasiti atau Copilot. → Guna akaun **dalam tenant pemilik kapasiti**.
- **Copilot tak muncul** → tetapan tenant belum *On*, atau kapasiti bukan **F2+** (trial **tiada** Copilot).
- **Peserta tak boleh publish** → **tiada lesen** Power BI.

> **Diagnostik cepat:** `az account show` (tenant + user), `az resource list --resource-type Microsoft.Fabric/capacities` (kapasiti + resource group).

## Bahagian B — Muat data ke Lakehouse (SESI 2 / Modul 2)

| # | Fail | Skrin |
|---|------|-------|
| 01 | `01-workspace-kkdw-copilot.jpg` | Workspace KKDW Copilot (kosong) |
| 02 | `02-new-lakehouse-dialog.jpg` | New item → Lakehouse → nama `KKDW_Lakehouse` |
| 03 | `03-lakehouse-explorer-getdata.jpg` | Lakehouse Explorer + "Get data in your lakehouse" |
| 04 | `04-files-uploaded.jpg` | 3 fail Excel dalam **Files** (data_jpd/belb/myprojek) |
| 05 | `05-dataflow-getdata.jpg` | Dataflow Gen2 → sumber data (**Import from Excel**) |
| 06 | `06-dataflow-excel-connect.jpg` | Connect to data source (Excel) → **Browse OneDrive** |
| 07 | `07-navigator-jpd-preview.jpg` | Navigator → pilih Sheet1 → **pratonton data JPD sebenar** |
| 08 | `08-powerquery-jpd-loaded.jpg` | Power Query Online — query **JPD** dimuat, Applied Steps, destinasi = Lakehouse |
| 09 | `09-three-queries-loaded.jpg` | Ketiga-tiga query (**JPD · BELB · MyProjek**) dimuat dalam dataflow `KKDW_Ingest` |

### Membersih data dalam dataflow (SESI 3 — Power Query)

Untuk **setiap** query (JPD, BELB, MyProjek), dalam Power Query Online:

1. **Promote headers** — pastikan baris tajuk sebenar dinaikkan (jika fail ada baris tajuk/logo di atas, buat **Remove Top Rows** dahulu). *Punca #1 ralat "Changed column type" ialah header salah dinaikkan.*
2. **Change type ikut medan** — jangan biar auto-detect meneka salah:
   - Nombor: `kos_projek`, `panjang_jalan`, `jumlah_projek_peserta`, `lat_1/long_1/lat_2/long_2`, `tahun_mula/tahun`, dan (MyProjek) `peratus_jadual_projek`, `peratus_sebenar_projek`, `kos_keseluruhan`.
   - Teks (kunci): `kod_projek`, `kod_negeri`, `kod_daerah`, `kod_parlimen`, `kod_dun`. **Kekalkan sebagai Text** — kod dengan sifar di hadapan akan rosak jika jadi nombor.
   - Jika lajur nombor ada teks (`N/A`, `-`, awalan `RM`): tukar ke **Text** dahulu → **Replace Values** bersihkan → baru tukar jenis nombor. Tarikh: **Change Type → Using Locale…**.
3. **Conditional Column** `kategori_status` dari `status_pelaksanaan` (mis. *DALAM PELAKSANAAN* → "Aktif", *PASCA PELAKSANAAN* → "Siap").
4. Buang lajur yang tak digunakan supaya model ringan.

> Kod M rujukan penuh: [`../../hari-1/snippets/power-query.m`](../../hari-1/snippets/power-query.m). Nota konsep: [`../../nota/03-power-query.md`](../../nota/03-power-query.md).

## Bahagian C — Terbit dataflow → jadual dalam Lakehouse (SESI 3–4)

Corak yang sama, dalam dataflow `KKDW_Ingest`:

1. Query **JPD** sudah dimuat (skrin 08). **Get data → Import from Excel → Browse OneDrive** untuk `data_belb.xlsx` → rename query **BELB**.
2. Ulang untuk `data_myprojek.xlsx` → rename query **MyProjek** (skrin 09 = ketiga-tiganya siap dimuat).
3. Set **Data destination = `KKDW_Lakehouse`** bagi setiap query (butang destinasi di bahagian bawah kanan setiap query).
4. **Publish** dataflow → klik **Refresh now**. Selepas berjaya, buka **`KKDW_Lakehouse` → Tables** → sepatutnya nampak `JPD`, `BELB`, `MyProjek`.

> ✅ **SIAP:** dataflow `KKDW_Ingest` telah dijalankan — 3 jadual Delta (`JPD` 1,376 baris, `BELB` 23, `MyProjek` 77) wujud dalam `KKDW_Lakehouse/Tables/dbo/`.

## Bahagian D — Semantic model & star schema (SESI 5) — ✅ **SIAP (dibina tanpa Power BI Desktop)**

Model **`KKDW_Model`** telah dibina & di-deploy ke workspace **KKDW Copilot** — **100% dari Mac, tanpa Power BI Desktop** (guna Fabric + Power BI Modeling MCP: bina jadual bersepadu secara tempatan → tulis ke OneLake sebagai Delta → model DirectLake → relationships + measures → uji dengan DAX langsung).

**Model dibina (7 jadual DirectLake):**
- Jadual mentah: `JPD`, `BELB`, `MyProjek`
- Jadual bersepadu baharu: **`Projek_Program`** (JPD∪BELB, lajur `program` + `kategori_status`, 1,399 baris), **`Dim_Negeri`** (16 negeri), **`Dim_Tarikh`** (2017–2028, *Mark as date table*), **`Dim_Agensi`** (15 agensi)

**4 relationships (star schema):**
```
Projek_Program ──kod_negeri──►  Dim_Negeri
MyProjek       ──negeri──────►  Dim_Negeri
MyProjek       ──agensi_pemilik─► Dim_Agensi
Projek_Program ──tarikh_tahun─► Dim_Tarikh (Date table)
```
Kardinaliti: dimensi **1** → fakta **many (∗)**, penapis **single**.

**23 measures** dibina & diuji (mis. Jumlah Projek = 1,399 · Projek Siap = 952 · % Utilisasi ≈ 80.5% · Projek Merah = 3). Kod: [`../../hari-2/snippets/measures.dax`](../../hari-2/snippets/measures.dax), [`../../hari-3/snippets/risk-measures.dax`](../../hari-3/snippets/risk-measures.dax).

> **Penyesuaian dengan data sebenar (penting untuk kelas):**
> 1. `peratus_jadual_projek`/`peratus_sebenar_projek` ialah **0–100** (bukan 0–1) → ambang risiko jadi **-5 / -10**.
> 2. `lat/long` **kosong** dalam sumber → peta ikut **negeri** sahaja (bukan titik).
> 3. Measures kos (Kos per KM/Sambungan) lalui `Projek_Program` yang dinormalkan (kod_negeri mentah JPD/BELB tak seragam, mis. "N.SEMBILAN").
>
> **Nota alat:** laluan Fabric di atas berjaya sepenuhnya di macOS. Untuk membina **laporan/visual & DAX** (Hari 2–3), Power BI Desktop (Windows sahaja) ialah alat rasmi & termudah — di macOS guna **Power BI Service (pelayar)** atas `KKDW_Model`, atau VM Windows. **Hari 1 (data + model) tidak perlukan Desktop.**

> ✅ **Tangkapan skrin:** `10-model-view.jpg` — Model view `KKDW_Model` (Projek_Program & MyProjek → Dim_Negeri/Dim_Tarikh/Dim_Agensi) + 7 jadual dalam panel Data.

## Bahagian E — Dashboard (SESI 6–10, Hari 2) — ✅ **SIAP (dibina oleh Copilot, tanpa Desktop)**

Halaman laporan **Executive Projek Overview** dibina **terus dalam pelayar** atas `KKDW_Model` (tiada Power BI Desktop):

- Kad: **Jumlah Projek** (1,399 ≈ "1K") · **% Utilisasi** (80.5%)
- **Jumlah Projek by program** (JPD vs BELB) · **Jumlah Peruntukan & Belanja**
- **Bilangan projek ikut negeri** (bar) · **% Utilisasi ikut Tahun** (line) · slicer negeri & program

> ✅ **Tangkapan skrin:** `13-executive-report.jpg` — halaman penuh Executive Projek Overview.
>
> Masih TODO untuk pengeluaran: **Save** laporan ke workspace, **Scheduled refresh**, dan **RLS** per-negeri (`kod_negeri`).

## Bahagian F — Copilot / AI (SESI 13–14, Hari 3) — ✅ **SIAP (Copilot menjana laporan)**

**Copilot tersedia** dalam workspace ini — butang **Copilot** aktif dalam editor laporan. Satu arahan bahasa biasa menjana keseluruhan halaman di atas:

> *"Create an executive overview page: total projects by program (JPD, BELB), total peruntukan and total belanja, % utilisasi, and a bar chart of projects by negeri."*

> ✅ **Tangkapan skrin:** `12-copilot-report.jpg` — panel Copilot + laporan yang dijana ("Your new report page is ready!").
>
> Lanjutan (Hari 3): uji pertanyaan gaya-pengurusan tambahan + visual AI (Key Influencers, Decomposition Tree, Smart Narrative). *Nota lesen: Copilot umumnya perlu kapasiti F2+/Copilot-enabled — ia aktif dalam tenant ini.*

## Ringkasan tangkapan skrin

| Status | Skrin |
|--------|-------|
| ✅ Ada (fokus **persediaan Hari 1**) | 01–09 (Bahagian A–B: tenant, Lakehouse, upload 3 Excel, dataflow, 3 query dimuat) |
| ✅ Ada | **10** — Model view `KKDW_Model` (Bahagian D: 7 jadual + relationships star schema) |
| ✅ Ada | **11** — Lakehouse `Projek_Program` (Bahagian C: jadual bersepadu JPD∪BELB, 1,399 baris) |
| ✅ Ada | **12** — Copilot menjana laporan (Bahagian F) |
| ✅ Ada | **13** — Halaman Executive Projek Overview (Bahagian E) |
| ⬜ TODO | Save laporan · Scheduled refresh · RLS |

## Cara guna dalam slaid
Tangkapan skrin **01–09 memberi tumpuan kepada persediaan Hari 1** (Data → Fabric: tenant → Lakehouse → upload → Dataflow Gen2 → 3 query) — **SESI 2–4**. **10–11** = Bahagian C–D (Lakehouse `Projek_Program` + Model view `KKDW_Model`), **SESI 5**. **12–13** = Bahagian E–F (laporan Executive + Copilot menjana laporan), **Hari 2** & **Hari 3 SESI 13–14**. Keseluruhan dibina **dari macOS, tanpa Power BI Desktop**.
