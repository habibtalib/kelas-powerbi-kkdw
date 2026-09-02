# Hari 1 — Lab Hands-On (SESI 1–5)

Latihan langkah demi langkah untuk membina **model data bersepadu** JPD + BELB + MyProjek. Fail data (JPD/BELB/MyProjek) **disediakan semasa kelas** — *tidak disertakan dalam repo awam ini*. Simpan kerja anda sebagai `hari-1.pbix`.

> 📎 **Rujukan kod:** [`power-query.m`](./power-query.m) — kod M lengkap untuk bersih & gabung data (boleh tampal dalam Advanced Editor, atau ikut GUI di bawah).

> **Peringatan:** kita **belum** bina visual hari ini — fokus data yang bersih & bermodel.

---

## Latihan 1 — Bengkel Soalan Pengurusan

**Tujuan:** faham *kenapa* sebelum *bina*.

1. Dalam kumpulan kecil, senaraikan **5 soalan** yang pengurusan KKDW mahu dashboard jawab. Contoh:
   - Berapa jumlah projek JPD & BELB, dan berapa yang lewat?
   - Negeri mana paling banyak peruntukan tetapi kemajuan rendah?
2. Untuk setiap soalan, padankan dengan **medan data** yang ada:

| Soalan | Data | Medan |
|--------|------|-------|
| Berapa projek lewat? | MyProjek | `peratus_jadual_projek`, `peratus_sebenar_projek` |
| Peruntukan vs belanja? | MyProjek | `peruntukan_disemak_janm_*`, `belanja_janm_*`, `baki_kos_de` |
| Kos jalan ikut negeri? | JPD | `kos_projek`, `panjang_jalan`, `kod_negeri` |

3. Simpan senarai — ia jadi **panduan** bila kita bina dashboard Hari 2.

---

## Latihan 2 — Muat Naik 3 Set Data

1. Buka **Power BI Desktop** → log masuk akaun organisasi KKDW.
2. **Home → Get Data → Excel workbook** → pilih fail `data_jpd.xlsx` (disediakan semasa kelas).
3. Dalam Navigator, tanda `Sheet1` → klik **Transform Data** (jangan *Load* terus).
4. Ulang untuk `data_belb.xlsx` dan `data_myprojek.xlsx`.
5. Dalam Power Query Editor, **rename** setiap query: `JPD`, `BELB`, `MyProjek`.

✅ **Semak:** tiga query kelihatan di panel *Queries* sebelah kiri.

---

## Latihan 3 — Bersihkan Data JPD & BELB

Untuk query **JPD**:

1. **Buang lajur tak perlu:** pilih `created_at`, `updated_at`, `tarikh_upload` → klik kanan → **Remove Columns**.
2. **Betulkan jenis data:**
   - `kos_projek`, `panjang_jalan` → **Decimal Number**
   - `tahun`, `tahun_mula` → **Whole Number**
   - `kod_negeri`, `kod_daerah` → **Text**
3. **Standardkan teks:** pilih `status_pelaksanaan` → **Transform → Format → UPPERCASE**, kemudian **Trim**.
4. **Conditional Column** (`kategori_status`): **Add Column → Conditional Column**:
   - JIKA `status_pelaksanaan` = `PASCA PELAKSANAAN` → `Siap`
   - JIKA `status_pelaksanaan` = `DALAM PELAKSANAAN` → `Dalam Pelaksanaan`
   - Selainnya → `Belum Mula / Lain`
5. Ulang langkah 1–4 untuk query **BELB**.

✅ **Semak:** panel *Applied Steps* menunjukkan setiap langkah; nilai `kategori_status` betul.

---

## Latihan 4 — Gabung JPD & BELB

**Tujuan:** satu jadual operasi program (JPD + BELB).

1. Dalam **JPD**, tambah **Custom Column** `program` = `"JPD"`. Dalam **BELB**, tambah `program` = `"BELB"`.
2. Pastikan kedua-dua query kongsi lajur sepunya: `nama_projek`, `kos_projek`, `kod_negeri`, `kod_daerah`, `status_pelaksanaan`, `kategori_status`, `program`, `tahun`.
3. **Home → Append Queries → Append Queries as New** → pilih `JPD` + `BELB` → namakan hasil **Projek_Program**.
4. *(Lanjutan)* untuk kaitkan kewangan: **Merge** `Projek_Program` dengan `MyProjek` guna kunci padanan (`kod_projek` jika sepadan) → kembangkan lajur `kos_keseluruhan`, `peruntukan…`, `belanja…`.

✅ **Semak:** `Projek_Program` mengandungi baris JPD **dan** BELB dengan lajur `program`.

> Klik **Close & Apply** untuk muat ke model.

---

## Latihan 5 — Bina Model Bersepadu

**Tujuan:** star schema + Date table + relationships.

1. **Date table** — **Modeling → New Table**:
   ```dax
   Dim_Tarikh =
   CALENDAR ( DATE ( 2015, 1, 1 ), DATE ( 2030, 12, 31 ) )
   ```
   Tambah lajur `Tahun = YEAR ( Dim_Tarikh[Date] )`. Tandakan sebagai **Mark as Date Table**.
2. **Dimension Negeri** — buat jadual rujukan negeri (dari `kod_negeri` unik + nama negeri). *(Jika hanya ada kod, buat pemetaan ringkas kod→nama.)*
3. **Relationships** (View → **Model**):
   - `Projek_Program[kod_negeri]` → `Dim_Negeri[kod_negeri]` (many-to-one)
   - `Projek_Program[tahun]` → `Dim_Tarikh[Tahun]` (many-to-one)
4. **Kemas paparan:** sembunyikan lajur teknikal (`id`, kunci) — klik kanan → *Hide*.

✅ **Semak & simpan:**
- [ ] `Dim_Tarikh` ditanda sebagai Date Table
- [ ] Relationships kelihatan sebagai garisan dalam Model view
- [ ] **File → Save As → `hari-1.pbix`**

---

## Cabaran (jika ada masa)

Bina **Conditional Column** kedua dalam MyProjek: `bendera_ketidakpadanan` = `"Semak"` jika `belanja` tinggi tetapi `peratus_sebenar_projek` rendah — kita akan guna idea ini pada Hari 3.
