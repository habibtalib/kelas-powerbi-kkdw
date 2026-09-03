# Nota Konsep: Microsoft Fabric, OneLake & Lakehouse

> Nota latar belakang untuk SESI 2 (Hari 1). Fahami **platform data** di sebalik Power BI — di mana data KKDW disimpan, disedia dan dimodel sebelum jadi dashboard.

---

## Kenapa perlu platform data, bukan sekadar fail Excel?

Untuk kursus ini, data KKDW datang dalam tiga fail Excel kecil. Tetapi dalam realiti, KKDW ada **banyak sumber**: sistem MyProjek, pangkalan data agensi pelaksana, fail Excel jabatan, dan laporan negeri. Bila setiap pegawai simpan salinan sendiri, data jadi **bertaburan, tidak konsisten dan lapuk**.

**Microsoft Fabric** menyelesaikan ini dengan menyediakan **satu platform** tempat semua data dikumpul, dibersih, dimodel dan diterbitkan — supaya semua orang bekerja dengan **sumber kebenaran yang sama** (*single source of truth*).

---

## Apa itu Microsoft Fabric?

**Microsoft Fabric** ialah **platform analitik bersepadu** — satu payung untuk seluruh kitaran hayat data: simpanan, penyediaan, transformasi, pemodelan, pelaporan dan AI. Power BI kini sebahagian daripada Fabric.

> **Analogi KKDW:** Fabric ialah **gudang & bilik sedia data** kementerian — semua data projek dikumpul di satu tempat, dibersihkan dan disusun kemas, sebelum dibawa ke "bilik pameran" (Power BI) untuk dipapar.

### Komponen penting Fabric

| Komponen | Maksud (mudah) | Kaitan KKDW |
|----------|----------------|-------------|
| **OneLake** | "OneDrive untuk data" — satu *data lake* untuk seluruh organisasi | Semua data JPD, BELB, MyProjek duduk di satu tempat |
| **Workspace** | Ruang kerja berkumpulan tempat item disimpan & dikongsi | Workspace "KKDW Pemantauan Projek" |
| **Lakehouse** | Gabungan *data lake* + *data warehouse* — simpan fail mentah **dan** jadual berstruktur | Fail Excel mentah + jadual bersih untuk analisis |
| **Dataflows Gen2** | Power Query di awan — transformasi boleh dijadual & dikongsi | Bersihkan `status_pelaksanaan`, `kod_negeri` sekali, guna semula |
| **Semantic Model** | Model data (jadual + relationships + measures) yang jadi sumber laporan | Star schema JPD+BELB+MyProjek ([`04-pemodelan-star-schema.md`](./04-pemodelan-star-schema.md)) |
| **Data Factory** | Alat *pipeline* untuk membawa masuk data dari pelbagai sumber | Tarik data dari sistem sumber KKDW |

---

## OneLake — "OneDrive untuk data"

**OneLake** ialah satu tasik data (*data lake*) tunggal, automatik untuk seluruh tenant. Sama seperti setiap organisasi ada **satu** OneDrive, ia ada **satu** OneLake.

Kenapa ini penting untuk KKDW:

- **Tiada salinan bertaburan** — data disimpan sekali, dirujuk oleh banyak laporan.
- **Semua alat berkongsi data sama** — Dataflows, Notebook, dan Power BI baca dari OneLake yang sama.
- **Format terbuka** — data disimpan dalam format Delta/Parquet, bukan format tertutup.

```
                    ┌─────────── OneLake (satu tasik data KKDW) ───────────┐
   Data sumber  →   │  Lakehouse: fail mentah  →  jadual bersih (Delta)     │  →  Power BI
   (Excel, MyProjek)│           Dataflows Gen2 (transformasi) · Semantic Model │     (dashboard)
                    └───────────────────────────────────────────────────────┘
```

---

## Lakehouse — gabungan dua dunia

Secara tradisi ada dua pilihan: **data lake** (simpan apa sahaja fail mentah, murah, tetapi kurang struktur) atau **data warehouse** (jadual berstruktur untuk analisis, tetapi ketat). **Lakehouse** menggabungkan kedua-duanya — simpan fail mentah **dan** jadual berstruktur di tempat yang sama.

Untuk KKDW: fail `data_myprojek.xlsx` mentah boleh dimuat naik ke Lakehouse, kemudian ditransform menjadi jadual bersih `Fakta_Projek` — semuanya dalam satu Lakehouse.

### Lakehouse vs Warehouse — bila guna yang mana

Fabric ada **dua** simpanan berstruktur yang serupa. Untuk audiens no-code KKDW, **Lakehouse memadai** — Warehouse hanya perlu bila ada pasukan mahir SQL.

| | **Lakehouse** | **Data Warehouse** |
|---|---|---|
| Sesuai untuk | Pemula, fail campur, no-code | Pasukan mahir **T-SQL** |
| Cara sedia data | Muat naik / Dataflows / Notebook (Spark) | Skrip **T-SQL** (baca **dan** tulis) |
| Akses SQL | *SQL Analytics endpoint* — **baca sahaja** | T-SQL penuh (baca & tulis) |
| Untuk KKDW | **Pilihan kursus** | Rujukan lanjutan sahaja |

---

## Direct Lake — mode sambungan ketiga (khas Fabric)

Selain **Import** dan **DirectQuery** (dibincang di [Hari 1 SESI 2](../hari-1/README.md#sesi-2-1030--100--microsoft-fabric--menyambung-data)), Fabric memperkenalkan mode **keempat**: **Direct Lake** — hanya bila sumber data ialah **Lakehouse atau Warehouse** dalam OneLake.

Kenapa ia istimewa:

- **Kelajuan hampir Import, kesegaran hampir DirectQuery.** Enjin Power BI menjalankan DAX **terus** atas fail Delta/Parquet di OneLake — tanpa menyalin data masuk `.pbix`, dan **tanpa perlu jadual refresh** kerana ia sentiasa baca data terkini.
- **Tiada terjemahan query.** DirectQuery lambat kerana ia menukar DAX → SQL dan bergantung enjin sumber. Direct Lake langkau langkah ini.
- **Fallback automatik.** Jika query melebihi had memori SKU atau bilangan baris, enjin **jatuh balik** (*fallback*) ke DirectQuery secara automatik.

| Mode | Data di mana | Refresh perlu? | Kelajuan |
|------|--------------|----------------|----------|
| **Import** | Dalam `.pbix` (memori) | Ya (berjadual) | Sangat pantas |
| **DirectQuery** | Kekal di sumber | Tidak (masa nyata) | Bergantung sumber |
| **Direct Lake** | Lakehouse/Warehouse (OneLake) | **Tidak** | Hampir Import |

> **Untuk kursus ini kita guna Fabric (pelayar)** — muat data ke **Lakehouse**, kemudian model **DirectLake `KKDW_Model`** dibina dalam **Power BI Service** (bukan Desktop). *(Mod Import masih boleh untuk data kecil sebagai pilihan.)* Direct Lake ialah pilihan terbaik bila data besar & perlu sentiasa terkini.

---

## Lesen Fabric — nota penting

Ciri penuh Fabric memerlukan **Fabric capacity**, dijual mengikut saiz (F2, F4, ... F64, dan ke atas). **Ciri Copilot dan AI memerlukan sekurang-kurangnya kapasiti F64** (atau kapasiti Power BI Premium yang setara & didayakan Copilot).

| Kapasiti | Keupayaan ringkas |
|----------|-------------------|
| Power BI Desktop (percuma) | Bina model, DAX, visual, visual AI terbina — **tiada Copilot** |
| Power BI Pro | Terbit & kongsi (per pengguna) |
| Fabric **F64+** / Premium | OneLake penuh, Lakehouse, Dataflows Gen2, **Copilot** |

---

## Bila guna Fabric penuh vs Power BI Desktop sahaja

| Situasi | Guna |
|---------|------|
| Belajar, prototaip, data kecil (kursus ini) | **Power BI Desktop sahaja** (percuma) |
| Data besar, banyak sumber, pasukan berkongsi | **Fabric** (OneLake + Lakehouse + Dataflows) |
| Perlu Copilot / NL Q&A penuh | **Fabric F64+** atau tenant Copilot |
| Transformasi berjadual & boleh guna semula | **Dataflows Gen2** dalam Fabric |

Untuk kursus ini, latihan berjalan dalam **Power BI Service / Fabric (pelayar)** — muat data ke **Lakehouse**, bina model & laporan dalam **Service**. Power BI Desktop ialah **pilihan luar talian** sahaja.

---

Seterusnya: [`03-power-query.md`](./03-power-query.md) — cara sebenar membersih & mentransform data. Mula hands-on di [Hari 1 SESI 2](../hari-1/README.md).

## Sumber Rasmi

- **[learn.microsoft.com/fabric](https://learn.microsoft.com/fabric/)** — dokumentasi Microsoft Fabric.
- **[learn.microsoft.com/fabric/onelake](https://learn.microsoft.com/fabric/onelake/onelake-overview)** — OneLake.
- **[learn.microsoft.com/fabric/data-engineering/lakehouse-overview](https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview)** — Lakehouse.
- **[learn.microsoft.com/fabric/get-started/direct-lake-overview](https://learn.microsoft.com/fabric/get-started/direct-lake-overview)** — Direct Lake.
- 📘 *Architecting Power BI Solutions in Microsoft Fabric* (Packt) — Bab 5 *Deciding on the Storage Mode* (ms 75–106); Bab 7 *Understanding Microsoft Fabric* (ms 125–153): Lakehouse ms 136, Data Warehouse ms 141, **Direct Lake ms 146–148**.

> ⚠️ **Peringatan lesen:** Fabric penuh & **Copilot memerlukan kapasiti F64+ atau tenant yang telah didayakan Copilot**. Ini **bukan** ciri percuma — **sahkan konfigurasi lesen dengan pentadbir IT KKDW** sebelum merancang penggunaan meluas. Jika belum sedia, seluruh kursus (kecuali Copilot) masih berjalan dalam **Power BI Service / Fabric**, menggunakan **Q&A + visual AI percuma** sebagai ganti Copilot.
