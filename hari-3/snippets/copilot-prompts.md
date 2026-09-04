# Copilot Prompts — KKDW (salin & tampal)

Prompt siap-guna untuk **Copilot dalam Power BI & Microsoft Fabric**, berdasarkan model **`KKDW_Model`** (fakta `Projek_Program` & `MyProjek`; dimensi `Dim_Negeri`, `Dim_Tarikh`, `Dim_Agensi`). Medan sebenar: `kod_negeri`, `kod_projek`, `nama_projek`, `kos_projek`, `panjang_jalan`, `kategori_status`, `peratus_jadual_projek`, `peratus_sebenar_projek` (skala **0–100**), `peruntukan_disemak_janm_tahun_1`, `belanja_janm_tahun_1`.

> ⚠️ **Lesen:** Copilot penuh perlu **Fabric F64+ / kapasiti Copilot-enabled**. Tiada lesen → guna **Q&A visual** (percuma) + visual AI terbina (Key Influencers, Decomposition Tree, Smart Narrative, Analyze). Lihat [`../../nota/07-copilot-ai.md`](../../nota/07-copilot-ai.md).
> ⚠️ **AI membantu, anda memandu:** sahkan **setiap** DAX & jawapan dengan sumber sebelum guna untuk keputusan. Copilot boleh salah faham medan / skala 0–100.

---

## 1. Natural-Language Q&A (Copilot chat / Q&A visual)

*Buka **Copilot** (Power BI Service / Fabric) atau tambah visual **Q&A**, taip:*

- `Senaraikan 10 projek JPD dengan jurang terbesar antara kemajuan jadual dan sebenar.`
- `Negeri mana perbelanjaan BELB tertinggi tetapi kemajuan projek paling rendah?`
- `Ringkaskan prestasi projek BELB untuk Sabah.`
- `Apakah tiga isu utama portfolio JPD pada tempoh semasa?`
- `Cari projek dengan kemajuan fizikal bawah 50% tetapi telah guna lebih 70% peruntukan.`
- `Berapa jumlah projek dan jumlah kos ikut negeri?`
- `Projek mana paling lewat berbanding jadual?`

---

## 2. Jana / cadang **DAX** dengan Copilot

*Power BI Desktop atau Service → **DAX query view → Copilot** ("Run a DAX query"), atau cadangan measure dalam formula bar (ikut ketersediaan tenant). **Semak & justify setiap baris** — bandingkan dengan [`risk-measures.dax`](./risk-measures.dax) / [`../../hari-2/snippets/measures.dax`](../../hari-2/snippets/measures.dax).*

- `Buat measure Jumlah Projek = kira bilangan baris dalam Projek_Program.`
- `Tulis measure Jumlah Belanja = jumlah belanja_janm_tahun_1 dalam MyProjek.`
- `Cipta measure Kos per KM = jumlah kos_projek dibahagi jumlah panjang_jalan (elak bahagi sifar).`
- `Buat measure % Utilisasi = DIVIDE(Jumlah Belanja, Jumlah Peruntukan).`
- `Cipta measure Varians Kemajuan = purata (peratus_sebenar_projek tolak peratus_jadual_projek). Ingat skala 0–100.`
- `Measure yang kira bilangan projek dengan kategori_status = "Siap".`
- `Buat measure Status Risiko guna SWITCH: Hijau jika Varians ≥ -5, Kuning jika ≥ -10, selainnya Merah.`
- `Terangkan apa measure ini buat, baris demi baris: [tampal DAX di sini].`
- `Optimumkan / permudah measure ini tanpa menukar hasil: [tampal DAX].`

> **Nota:** Copilot kerap **lupa skala 0–100** (guna 0.05 dan bukan -5). Sentiasa semak ambang & DIVIDE (bukan `/`).

---

## 3. Cipta **visual / halaman** dengan Copilot

*Power BI Service (report) → **Copilot → Create a report / Suggest content for this page**, atau taip arahan visual:*

- `Cipta halaman ringkasan eksekutif: kad Jumlah Projek, Jumlah Peruntukan, % Utilisasi, dan bar chart Jumlah Projek ikut negeri.`
- `Tambah bar chart Jumlah Projek mengikut kod_negeri, disusun menurun.`
- `Bina halaman prestasi BELB ikut negeri dengan jadual projek berisiko (Status Risiko = Merah).`
- `Cadangkan visual terbaik untuk bandingkan peratus_jadual_projek vs peratus_sebenar_projek mengikut projek.`
- `Buat kad KPI untuk Baki (Peruntukan tolak Belanja) dengan format ringgit.`
- `Cipta peta (filled map) Jumlah Projek mengikut kod_negeri.`
- `Tambah decomposition tree: pecah Jumlah Belanja ikut negeri kemudian kategori_status.`
- `Tukar carta ini kepada column chart dan tambah warna bersyarat merah untuk Status Risiko Merah.`

---

## 4. Ringkasan / naratif (Smart Narrative & Copilot)

- `Ringkaskan halaman ini untuk pengurusan atasan dalam 3 poin.`
- `Tulis ringkasan naratif prestasi portfolio JPD pada tempoh semasa.`
- `Beri 3 cadangan tindakan berdasarkan projek Status Risiko Merah.`
- *(Smart Narrative visual)* `Tambah kotak Smart Narrative pada halaman AI Risk untuk auto-jana ulasan.`

---

## 5. Fabric Copilot (Dataflow / Notebook / Data agent)

*Dalam Fabric (bukan report Power BI):*

- **Dataflow Gen2 (Power Query):** `Trim dan UPPERCASE lajur kod_negeri.` · `Tambah lajur tempoh_hari = beza hari antara tarikh_terima dan tarikh_selesai.` · `Tapis baris di mana kos_projek kosong.`
- **Notebook (Spark):** `Baca data_jpd.csv dari Lakehouse Files dan papar 5 baris pertama.` · `Kira jumlah kos_projek ikut kod_negeri dan simpan sebagai jadual Delta.`
- **Data agent / OneLake:** `Projek JPD mana di Sabah dengan varians kemajuan paling negatif?`

---

## Susulan yang baik selepas jawapan Copilot

- `Tunjuk DAX / query yang kamu guna untuk jawapan ini.` *(untuk sahkan)*
- `Apakah andaian yang kamu buat?`
- `Kecualikan projek yang belum bermula daripada kiraan.`
