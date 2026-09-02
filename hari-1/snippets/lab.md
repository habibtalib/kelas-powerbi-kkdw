# Hari 1 — Lab Hands-On (SESI 1–5)

Latihan langkah demi langkah untuk membina **model data bersepadu** JPD + BELB + MyProjek. Fail data (JPD/BELB/MyProjek) **disediakan semasa kelas** — *tidak disertakan dalam repo awam ini*.

> 📎 **Rujukan kod:** [`power-query.m`](./power-query.m) — kod M untuk bersih & gabung data (tampal dalam Advanced Editor, atau ikut GUI di bawah).

> **Peringatan:** kita **belum** bina visual hari ini — fokus data yang **bersih & bermodel**.

### Aliran Hari 1 (gambaran keseluruhan)

```mermaid
flowchart LR
    X["3 fail Excel<br/>JPD · BELB · MyProjek"] --> PQ["Power Query<br/>bersih & taip"]
    PQ --> AP["Append<br/>Projek_Program"]
    AP --> MD["Model star schema<br/>+ Date table + relationships"]
    MD --> OUT(["Deliverable Hari 1<br/>model bersepadu"])
    classDef hi fill:#F2C811,color:#111,stroke:#B8960A
    class OUT hi
```

## Dua laluan — **pelayar (wajib) + Desktop (pilihan)**

**Laluan A (pelayar) ialah tulang belakang untuk semua** — ia **satu-satunya** tempat untuk **Fabric & Copilot**, dan boleh laksana keseluruhan kursus (Hari 1–3). **Laluan B (Desktop)** cuma alat tambahan untuk authoring Hari 2–3 (Windows), **bukan** ganti Fabric/Copilot.

| | **Laluan A — Fabric (pelayar) · WAJIB** | **Laluan B — Power BI Desktop · PILIHAN** |
|---|---|---|
| Peranan | Tulang belakang: **Fabric + Copilot + semua Hari 1–3** | Authoring laporan/DAX lebih kaya (Hari 2–3) |
| Alat | Microsoft Fabric di **pelayar** (OneLake, Lakehouse, Dataflow Gen2, Service, Copilot) | Power BI **Desktop** (aplikasi) |
| OS | **Mana-mana** (termasuk macOS) | **Windows sahaja** |
| Fabric & Copilot? | ✅ **Ya — hanya di sini** | ❌ Tidak (tak boleh cipta Lakehouse/Dataflow; Copilot Fabric di pelayar) |
| Simpan hasil | Jadual Delta + **semantic model** dalam workspace | fail `hari-1.pbix` |

> ⚠️ **Peserta yang guna Desktop sahaja akan terlepas Fabric & Copilot** (objektif teras kursus). **Setiap peserta perlu Laluan A (pelayar).** Di macOS, guna Power BI **Service** (pelayar) untuk authoring Hari 2–3 — bukan Desktop.

---

## Latihan 0 — Persediaan (Setup)

**Tujuan:** pastikan alat sedia sebelum mula. Pilih laluan ikut komputer anda.

### Pautan penting — daftar / log masuk

| Perkhidmatan | Pautan | Untuk |
|---|---|---|
| **Power BI** | [app.powerbi.com](https://app.powerbi.com) | Daftar / log masuk · bina & kongsi laporan (Service) |
| **Microsoft Fabric** | [app.fabric.microsoft.com](https://app.fabric.microsoft.com) | Workspace, Lakehouse, Dataflow, Copilot (Laluan A) |
| **Power BI Desktop** | [powerbi.microsoft.com/desktop](https://powerbi.microsoft.com/desktop/) | Muat turun (Windows, Laluan B) |
| **Azure Portal** | [portal.azure.com](https://portal.azure.com) | *(pentadbir)* sahkan kapasiti Fabric |
| **Microsoft Entra** | [entra.microsoft.com](https://entra.microsoft.com) | *(pentadbir)* identiti, pengguna, lesen |

> **Log masuk dengan akaun organisasi KKDW** yang diberi (dalam **tenant KKDW**). Jika belum ada akaun, minta **pentadbir IT** daftarkan anda — **bukan** akaun peribadi/guest (akan gagal akses kapasiti/Copilot).

### Laluan A — Fabric (pelayar) · mana-mana OS (termasuk macOS)

1. Buka pelayar → **`app.fabric.microsoft.com`** → **Sign in** dengan akaun organisasi KKDW.
2. Pilih (atau minta pentadbir cipta) **Workspace** jenis Fabric pada kapasiti **F2+** — kursus guna workspace **KKDW Copilot**.
3. Sahkan anda nampak **New item → Lakehouse / Dataflow Gen2** dalam workspace.
4. *(Copilot — Hari 3)* sahkan tetapan tenant Copilot **On** — rujuk panduan pentadbir Fabric (disediakan semasa kelas).

### Laluan B — Power BI Desktop · Windows sahaja

1. Pasang **Power BI Desktop** — **Microsoft Store** (cari "Power BI Desktop") atau [powerbi.microsoft.com/desktop](https://powerbi.microsoft.com/desktop/). *Percuma.*
2. Buka → **Sign in** (kanan atas) dengan akaun organisasi KKDW.
3. Sahkan **Home → Get Data** berfungsi.

> **macOS tiada Power BI Desktop** — guna **Laluan A**, atau **Power BI Service** (pelayar) untuk laporan Hari 2–3.

### Sahkan kapasiti Fabric (= kapasiti Azure)

Kapasiti Fabric ialah **sumber Azure** (`Microsoft.Fabric/capacities`) — jadi "setup Fabric" dan "setup Azure" merujuk kapasiti yang sama. Sahkan langkah demi langkah:

1. Dalam workspace → **Workspace settings** (kanan atas).
2. Klik tab **Workspace type**.
3. Sahkan: **Current workspace type = Fabric**, **SKU: F2**, **Region: Malaysia West**.

![Workspace settings → Workspace type: Fabric, SKU F2, Region Malaysia West (nama kapasiti & Capacity ID disunting)](../img/setup-fabric-capacity.jpg)

4. *(Pentadbir)* Sahkan sumber di **Azure portal → Microsoft Fabric → Capacities**: status **Active**, **F2**, **Malaysia West**. *(Nama kapasiti & Capacity ID disunting dalam gambar untuk privasi.)*

> Dalam kelas ini, `az` mengesahkan kapasiti: **SKU F2 · tier Fabric · region malaysiawest** — sepadan dengan skrin di atas.

### Identiti & lesen (Microsoft Entra)

Fabric, Power BI & Copilot semua log masuk melalui **Microsoft Entra ID** (dahulu **Azure AD**) — lapisan identiti/tenant organisasi.

1. **Log masuk dengan akaun dalam tenant yang sama** dengan pemilik workspace. Akaun **guest / tenant lain** selalu gagal akses kapasiti atau Copilot.
2. **Lesen:** setiap peserta perlu lesen **Power BI (Pro/PPU)** untuk **publish & kongsi** (Hari 2). Kapasiti **Fabric F2+** menampung item Fabric.
3. **Copilot:** perlu kapasiti **F2+** **DAN** pentadbir tenant dayakan di **Admin portal → Copilot and AI**.

> Peserta biasa **tidak** perlu peranan admin — hanya **akaun tenant + lesen**. Tetapan tenant/Copilot & umpukan lesen dibuat sekali oleh **pentadbir IT KKDW**.

```mermaid
flowchart LR
    U["Akaun peserta<br/>(Microsoft Entra)"] --> T{"Dalam tenant<br/>pemilik kapasiti?"}
    T -->|"Ya + ada lesen"| OK["✅ Akses Fabric,<br/>publish, Copilot (jika On)"]
    T -->|"Guest / tenant lain"| NO["❌ Tiada akses<br/>kapasiti / Copilot"]
    classDef ok fill:#3DDC97,color:#111
    classDef no fill:#E86A6A,color:#111
    class OK ok
    class NO no
```

### Nota lesen (penting)

- **Fabric penuh + Copilot** perlukan kapasiti **F2+ berbayar** (trial **tidak** termasuk Copilot). Sahkan dengan **pentadbir IT KKDW** sebelum kelas.
- Jika akses Fabric belum sedia, Hari 1 masih boleh 100% dalam **Power BI Desktop** (Windows).

✅ **Semak:** anda boleh log masuk + buka workspace Fabric (Laluan A) **atau** Power BI Desktop (Laluan B), dan kapasiti = **Fabric F2, Malaysia West**.

---

## Latihan 1 — Bengkel Soalan Pengurusan

**Tujuan:** faham *kenapa* sebelum *bina*.

1. Dalam kumpulan kecil, senaraikan **5 soalan** yang pengurusan KKDW mahu dashboard jawab. Contoh:
   - Berapa jumlah projek JPD & BELB, dan berapa yang lewat?
   - Negeri mana paling banyak peruntukan tetapi kemajuan rendah?
2. Untuk setiap soalan, padankan dengan **medan data** yang ada:

| Soalan | Data | Medan |
|--------|------|-------|
| Berapa projek lewat? | MyProjek | `peratus_jadual_projek`, `peratus_sebenar_projek` *(skala 0–100)* |
| Peruntukan vs belanja? | MyProjek | `peruntukan_disemak_janm_tahun_1..5`, `belanja_janm_tahun_1..5` |
| Kos jalan ikut negeri? | JPD | `kos_projek`, `panjang_jalan`, `kod_negeri` |

3. Simpan senarai — ia jadi **panduan** bila kita bina dashboard Hari 2.

---

## Latihan 2 — Muat Naik 3 Set Data

**Mode sambungan — Import vs DirectQuery vs Direct Lake** (kursus guna **Import**):

```mermaid
flowchart TD
    Q{"Saiz & lokasi data?"}
    Q -->|"Kecil–sederhana<br/>(data KKDW)"| I["Import ✅ pilihan kursus<br/>data dalam .pbix · sangat pantas"]
    Q -->|"Sangat besar /<br/>masa nyata"| DQ["DirectQuery<br/>tanya terus di sumber"]
    Q -->|"Sudah dalam<br/>Lakehouse / Warehouse"| DL["Direct Lake (khas Fabric)<br/>laju macam Import · tiada refresh"]
    classDef pick fill:#F2C811,color:#111,stroke:#B8960A
    class I pick
```

### Laluan A — Fabric (pelayar)

**Cipta workspace dahulu** (Lakehouse mesti duduk dalam workspace jenis Fabric):

1. Buka **Fabric** ([app.fabric.microsoft.com](https://app.fabric.microsoft.com)) → panel kiri **Workspaces → + New workspace**.
2. **Name:** `KKDW Copilot` → buka **Advanced** → **License mode: Fabric capacity** → pilih kapasiti **F2+** (mis. Malaysia West) → **Apply** *(lihat 3 tangkapan skrin di bawah)*.
   > Perlu peranan **Admin / Member** pada kapasiti. Jika pilihan *Fabric capacity* tiada, minta pentadbir tenant tetapkan (rujuk Latihan 0). Jika workspace sudah wujud, cuma **buka** ia dan teruskan ke langkah 3.

**Tangkapan skrin — cipta workspace:**

*1) Panel **Workspaces → + New workspace**:*
![Fabric: panel Workspaces dengan butang + New workspace](../img/step-w1-new-workspace.jpg)

*2) Isi **Name** (tunggu "This name is available") → buka **Advanced**:*
![Create a workspace: Name diisi + Advanced (Contact list, Workspace type)](../img/step-w2-create-workspace.jpg)

*3) **Workspace type = Fabric** → **Details:** pilih kapasiti Fabric (F2+) → **Apply**. (Nama kapasiti disunting untuk privasi.)*
![Create a workspace: Workspace type Fabric + Details kapasiti Fabric (nama kapasiti disunting)](../img/step-w3-fabric-capacity.jpg)

**Kemudian cipta Lakehouse & muat data:**

3. Dalam workspace → **New item → Lakehouse** → nama `KKDW_Lakehouse` *(lihat tangkapan di bawah)*.
4. **Get data / Upload** 3 fail Excel (`data_jpd.xlsx`, `data_belb.xlsx`, `data_myprojek.xlsx`) ke **Files** *(lihat tangkapan **Get Data → Excel** di bawah)*.
5. **New Dataflow Gen2** (`KKDW_Ingest`) → sambung ke Excel **dari Lakehouse Files (OneLake)** *(lihat tangkapan **Dataflow Gen2** di bawah)*:
   - **Get data → Azure Data Lake Storage Gen2** *(bukan Excel "Browse OneDrive/SharePoint" — sambungan itu selalu gagal untuk Excel; ia perlu fail di SharePoint/OneDrive-for-Business + auth organisasi).*
   - **URL** (folder Files Lakehouse anda):
     `https://onelake.dfs.fabric.microsoft.com/KKDW Copilot/KKDW_Lakehouse.Lakehouse/Files`
     *(boleh guna nama **atau** GUID bagi workspace & lakehouse).*
   - **Authentication: Organizational account** → **Sign in** → **Connect**.
   - ADLS Gen2 pulangkan senarai fail; pada lajur **Content** (binary) fail `.xlsx`, tambah langkah `Excel.Workbook([Content], true)` → gerudi ke **Sheet1**. Contoh M untuk query **JPD**:

   ```m
   let
       // Baca fail dari OneLake (Lakehouse Files) — bukan SharePoint
       Source = AzureStorage.DataLake(
           "https://onelake.dfs.fabric.microsoft.com/KKDW Copilot/KKDW_Lakehouse.Lakehouse/Files"
       ),
       Fail  = Table.SelectRows(Source, each [Name] = "data_jpd.xlsx"){0}[Content],
       Book  = Excel.Workbook(Fail, true),
       Sheet = Book{[Item = "Sheet1", Kind = "Sheet"]}[Data],
       NaikTajuk = Table.PromoteHeaders(Sheet, [PromoteAllScalars = true])
   in
       NaikTajuk
   ```

   Ulang untuk `data_belb.xlsx` & `data_myprojek.xlsx`.
6. Dalam Power Query Online, **rename** setiap query: `JPD`, `BELB`, `MyProjek` *(lihat tangkapan **Power Query**, Latihan 3)*.

> **Alternatif jika ADLS Gen2 masih rewel:** (a) **Get data → Excel workbook → Upload file** (muat naik fail terus ke dataflow, tiada SharePoint); atau (b) simpan fail sebagai **CSV**, muat naik ke Lakehouse **Files**, kemudian klik kanan CSV → **Load to Tables** (CSV→Delta secara native; Excel **tidak** boleh) → guna via **Direct Lake**.

**Tangkapan skrin — Lakehouse & Dataflow:**

*a) **New item** → cari "Lakehouse" → pilih petak **Lakehouse**:*
![Fabric New item: petak Lakehouse](../img/step-lh1-new-item.jpg)

*b) Dialog **New Lakehouse**: isi **Name** → **Location** = workspace → **Create**:*
![New Lakehouse: Name + Location + Create](../img/step-lh2-new-lakehouse.jpg)

*c) **New item** → cari "Dataflow" → pilih **Dataflow Gen2**:*
![Fabric New item: petak Dataflow Gen2](../img/step-df1-dataflow-gen2.jpg)

### Laluan B — Power BI Desktop

1. Buka **Power BI Desktop** → log masuk akaun organisasi KKDW.
2. **Home → Get Data → Excel workbook** → pilih `data_jpd.xlsx`.
3. Dalam Navigator, tanda `Sheet1` → klik **Transform Data** (jangan *Load* terus).
4. Ulang untuk `data_belb.xlsx` dan `data_myprojek.xlsx` → rename `JPD`, `BELB`, `MyProjek`.

✅ **Semak:** tiga query kelihatan di panel *Queries*.

**Tangkapan skrin — Get Data → Excel (muat naik / sambung):** pilih **Excel workbook** → **Link to file / Upload file** → **Browse OneDrive**. (Auth *Anonymous*, gateway *none* untuk fail OneLake.)

![Get data: Connect to data source — Excel workbook, Browse OneDrive](../img/step-0-getdata-excel.jpg)

---

## Latihan 3 — Bersihkan Data JPD & BELB (Power Query)

Sama untuk kedua-dua laluan (Power Query Online atau Desktop). Untuk query **JPD**:

> **Konsep — Query sebagai resipi:** setiap query ialah senarai **Applied Steps** (auto-jana: *Source → Navigation → Promoted headers → Changed Type*). Klik mana-mana langkah untuk lihat data pada peringkat itu — boleh edit, susun semula, atau buang (**X**). Di sebalik tabir, setiap langkah = satu baris kod **M**; satu **Refresh** jalankan semula **semua** langkah automatik. Sebab itu kita bersih di sini, **bukan** dalam Excel.

1. **Naikkan header betul:** pastikan baris tajuk sebenar dinaikkan (**Home → Use First Row as Headers**). *Punca #1 ralat "Changed column type" ialah header salah dinaikkan.*
2. **Buang lajur tak perlu:** `created_at`, `updated_at`, `tarikh_upload` → klik kanan → **Remove Columns**.
3. **Betulkan jenis data** — klik ikon jenis di kiri setiap nama lajur:

   | Lajur | Jenis data | Kenapa |
   |---|---|---|
   | `kod_projek`, `kod_program`, `kod_negeri`, `kod_daerah`, `kod_parlimen`, `kod_dun` | **Text** | kod dengan sifar di hadapan rosak jika jadi nombor |
   | `nama_projek`, `status_pelaksanaan`, `jenis_projek` | **Text** | label / teks |
   | `kos_projek` | **Currency** (Fixed decimal) | nilai RM |
   | `panjang_jalan`, `jumlah_projek_peserta` | **Whole/Decimal Number** | untuk KPI (mis. Kos per KM) |
   | `tahun`, `tahun_mula` | **Whole Number** | untuk Date table & time-intelligence |

   > **Penting:** jika `tahun` / medan tarikh kekal *Text*, fungsi tarikh & time-intelligence (Hari 2) **tak berfungsi**.
4. **Standardkan teks:** pilih `kod_negeri`, `status_pelaksanaan` (tahan **Ctrl** untuk pilih berbilang) → **Transform → Format → UPPERCASE** + **Trim** *(elak "SABAH " vs "SABAH" dikira dua kategori)*.
5. **Conditional Column** `kategori_status` (**Add Column → Conditional Column**):
   - JIKA `status_pelaksanaan` = `PASCA PELAKSANAAN` → `Siap`
   - JIKA `status_pelaksanaan` = `DALAM PELAKSANAAN` → `Dalam Pelaksanaan`
   - Selainnya → `Belum Mula / Lain`

   ```mermaid
   flowchart LR
       S["status_pelaksanaan"] --> C{"Nilai?"}
       C -->|"PASCA PELAKSANAAN"| A["Siap"]
       C -->|"DALAM PELAKSANAAN"| B["Dalam Pelaksanaan"]
       C -->|"lain-lain"| D["Belum Mula / Lain"]
   ```

6. Ulang langkah 1–5 untuk query **BELB**.
7. **Semak kualiti data (Data Profiling):** hidupkan **View → Column quality · Column distribution · Column profile** — kesan *null*, ralat, & bilangan nilai unik sebelum teruskan (mis. berapa negeri unik dalam `kod_negeri`).
8. **Lihat kod M penuh:** **Home → Advanced Editor** — setiap langkah GUI di atas = satu baris **M**. Rujukan siap-tampal (boleh salin ke Advanced Editor): [`power-query.m`](./power-query.m).

✅ **Semak:** panel *Applied Steps* menunjukkan setiap langkah; `kategori_status` betul (JPD+BELB: Siap 952 · Dalam Pelaksanaan 425).

**Tangkapan skrin — Power Query (muat naik + transform):** 3 query (JPD/BELB/MyProjek) dari Excel, panel **Applied Steps** (Source → Navigation → Promoted headers → Changed column type), dan destinasi **Lakehouse**.

![Power Query Online: 3 query, Applied Steps, destinasi Lakehouse (data disunting)](../img/step-1-powerquery-transform.jpg)

> **Nota data sebenar:** `lat_1/long_1/lat_2/long_2` wujud tetapi **kosong** dalam sumber — jadi peta Hari 2 ikut **negeri** (bukan titik koordinat).

---

## Latihan 4 — Gabung JPD & BELB → `Projek_Program`

**Tujuan:** satu jadual operasi program (JPD ∪ BELB) untuk KPI gabungan.

> **Konsep — gabung & bentuk data:** **Append** = tindan **baris** (JPD + BELB → `Projek_Program`, struktur sama); **Merge** = cantum **lajur** ikut kunci sepadan (seperti VLOOKUP / SQL JOIN — bawa kewangan MyProjek ikut `kod_projek`); **Unpivot** = tukar data *wide* (satu lajur per tahun) → *long* (satu baris = projek × tahun) supaya mudah dijumlah & ditapis ikut tahun.

```mermaid
flowchart TB
    subgraph AP["APPEND — susun baris (struktur sama)"]
        direction LR
        J["JPD · 1,376"] --> P["Projek_Program · 1,399"]
        B["BELB · 23"] --> P
    end
    subgraph MG["MERGE — gabung lajur ikut kunci"]
        direction LR
        P2["Projek_Program"] -.->|"kod_projek"| M["+ lajur kewangan<br/>dari MyProjek"]
    end
```

1. Dalam **JPD**, tambah **Custom Column** `program` = `"JPD"`. Dalam **BELB**, `program` = `"BELB"`.
2. Pastikan kedua-dua query kongsi lajur sepunya: `program`, `kod_projek`, `nama_projek`, `kos_projek`, `jumlah_projek_peserta`, `kod_negeri`, `status_pelaksanaan`, `kategori_status`, `tahun` (JPD tambah `panjang_jalan`; BELB tambah `nama_kampung`).
3. **Home → Append Queries → Append Queries as New** → pilih `JPD` + `BELB` → namakan hasil **`Projek_Program`**.
4. *(Untuk time-intelligence)* tambah lajur tarikh `tarikh_tahun` = awal tahun bagi `tahun` (mis. `#date([tahun],1,1)`).

✅ **Semak:** `Projek_Program` = **1,399 baris** (JPD 1,376 + BELB 23) dengan lajur `program`.

> **Laluan A (Fabric):** set **Data destination = `KKDW_Lakehouse`** bagi setiap query → **Publish/Refresh** dataflow. Jadual terbentuk dalam `KKDW_Lakehouse/Tables/dbo/`.
> **Laluan B (Desktop):** klik **Close & Apply** untuk muat ke model.

### 4B (Lanjutan) — Merge: bawa kewangan MyProjek

Untuk laporan Kewangan (Hari 2), cantum medan kewangan MyProjek ke `Projek_Program`:

1. **Home → Merge Queries** (bukan *as New* jika mahu ubah `Projek_Program` terus).
2. Jadual atas: `Projek_Program`; jadual bawah: `MyProjek`. Klik lajur kunci **`kod_projek`** pada kedua-dua (mesti jenis & format sama).
3. **Join Kind: *Left Outer*** (kekalkan **semua** projek JPD/BELB, walau tiada padanan MyProjek).
4. Klik ikon kembang **⇔** pada lajur `MyProjek` → pilih `peratus_jadual_projek`, `peratus_sebenar_projek`, `kos_keseluruhan`, `baki_kos_de` → **OK** (buang *"Use original column name as prefix"*).

✅ **Semak:** projek tanpa padanan MyProjek papar *null* pada lajur kewangan (dijangka) — bukan ralat.

### 4C (Lanjutan) — Unpivot: kewangan ikut tahun

Medan kewangan MyProjek dipecah *wide* (`..._tahun_1` … `..._tahun_5`). Untuk analisis trend tahunan (satu baris = projek × tahun):

1. Pilih lajur `peruntukan_disemak_janm_tahun_1` … `_tahun_5` (tahan **Ctrl**).
2. **Transform → Unpivot Columns**.
3. Hasil: lajur **Attribute** (nama tahun) + **Value** (RM). Guna **Transform → Extract → Last Characters** pada *Attribute* untuk dapatkan nombor tahun.

> **Enable load:** query perantara (mis. senarai negeri mentah) boleh dimatikan — klik kanan query → nyahtanda **Enable load** — supaya ia bukan jadual berasingan dalam model.

---

## Latihan 5 — Bina Model Bersepadu (star schema)

**Tujuan:** star schema + Date table + relationships. *(Inilah struktur `KKDW_Model` yang dibina untuk kelas.)*

```mermaid
flowchart TB
    DN["Dim_Negeri"]:::dim
    DT["Dim_Tarikh"]:::dim
    DA["Dim_Agensi"]:::dim
    PP["Projek_Program<br/>fakta: kos · panjang · peserta"]:::fact
    MY["MyProjek<br/>fakta: peruntukan · belanja · % kemajuan"]:::fact
    DN -->|"kod_negeri"| PP
    DT -->|"tarikh_tahun"| PP
    DN -->|"negeri"| MY
    DA -->|"agensi_pemilik"| MY
    classDef dim fill:#4AB3E0,color:#111,stroke:#2E7FA6
    classDef fact fill:#F2C811,color:#111,stroke:#B8960A
```

*Dimensi (biru) → Fakta (emas), hubungan **many-to-one**, penapis **single**.*

**Tangkapan skrin — Model view (KKDW_Model):** 7 jadual + relationships star schema (Projek_Program & MyProjek → Dim_Negeri/Dim_Tarikh/Dim_Agensi).

![Model view KKDW_Model: 7 jadual + relationships star schema](../img/step-2-model-view.jpg)

1. **Jadual dimensi:**
   - **`Dim_Negeri`** — senarai negeri unik (gabungan `kod_negeri` JPD/BELB + `negeri` MyProjek, dinormalkan; mis. `N.SEMBILAN` → `NEGERI SEMBILAN`). 16 negeri.
   - **`Dim_Tarikh`** — Date table 2017–2028. Dalam Desktop: **Modeling → New Table** →
     ```dax
     Dim_Tarikh = CALENDAR ( DATE ( 2017, 1, 1 ), DATE ( 2028, 12, 31 ) )
     ```
     Tambah `Tahun = YEAR ( Dim_Tarikh[Date] )` → **Mark as Date Table**.
   - **`Dim_Agensi`** — senarai agensi unik dari `agensi_pemilik` / `agensi_pelaksana_utama` (MyProjek). 15 agensi.
2. **Relationships** (View → **Model**) — **seret** lajur dari jadual **fakta** dan lepas di atas lajur padanan dalam jadual **dimensi**. Power BI kesan *cardinality* automatik; sahkan dalam dialog:

   | Seret (fakta) | Lepas di (dimensi) | Cardinality | Arah penapis |
   |---|---|---|---|
   | `Projek_Program[kod_negeri]` | `Dim_Negeri[kod_negeri]` | **Many-to-one (∗:1)** | **Single** |
   | `MyProjek[negeri]` | `Dim_Negeri[kod_negeri]` | **Many-to-one (∗:1)** | **Single** |
   | `MyProjek[agensi_pemilik]` | `Dim_Agensi[agensi]` | **Many-to-one (∗:1)** | **Single** |
   | `Projek_Program[tarikh_tahun]` | `Dim_Tarikh[Date]` | **Many-to-one (∗:1)** | **Single** |

   > **Konsep — cardinality & arah:** banyak baris fakta menunjuk **satu** baris dimensi → **∗:1**. Arah **Single** bermaksud penapis mengalir **dimensi → fakta** (pilih *SELANGOR* dalam slicer negeri → hanya projek Selangor tinggal). Elak *Both* melainkan perlu — ia boleh cipta laluan penapis samar-samar.

3. **Kemas paparan:** sembunyikan lajur teknikal (`id`, lajur kunci) — klik kanan → *Hide in report view*.

✅ **Semak & simpan:**
- [ ] `Dim_Tarikh` ditanda sebagai Date Table
- [ ] 4 relationships kelihatan sebagai garisan dalam Model view
- [ ] **Laluan A:** semantic model `KKDW_Model` wujud dalam workspace · **Laluan B:** **File → Save As → `hari-1.pbix`**

> **Hasil sebenar kelas:** model DirectLake **`KKDW_Model`** (7 jadual, 4 relationships, 23 measures) telah dibina & diuji — mis. `Jumlah Projek` = 1,399, `% Utilisasi` ≈ 80.5%. Measures dibina Hari 2 (diteruskan semasa kelas).

---

## Cabaran (jika ada masa)

Bina **Conditional Column** kedua dalam MyProjek: `bendera_ketidakpadanan` = `"Semak"` jika `belanja` tinggi tetapi `peratus_sebenar_projek` rendah (ingat: skala **0–100**) — kita akan guna idea ini pada Hari 3 (Risk Score & Early Warning).

---

## 📘 Rujukan Buku

*Architecting Power BI Solutions in Microsoft Fabric* (Packt) — bacaan lanjut bagi topik Hari 1:

| Latihan / topik | Bab & muka surat |
|---|---|
| SESI 2 · Fabric, OneLake, **Lakehouse** | Bab 7 *Understanding Microsoft Fabric* (ms 125–153) — Lakehouse **ms 136**, Warehouse ms 141 |
| SESI 2 · **Import vs DirectQuery vs Direct Lake** | Bab 5 *Deciding on the Storage Mode* (ms 75–106); Direct Lake **ms 146–148** |
| SESI 3 · Power Query (transform, query folding) | Bab 9 *Performing Optimizations in Power BI* — query folding **ms 206** |
| SESI 5 · Pemodelan (calc column vs measure) | Bab 9 — calculated column vs measure **ms 210** |

> Nota konsep berkaitan: [`../../nota/02-fabric-onelake.md`](../../nota/02-fabric-onelake.md) · [`../../nota/04-pemodelan-star-schema.md`](../../nota/04-pemodelan-star-schema.md).
