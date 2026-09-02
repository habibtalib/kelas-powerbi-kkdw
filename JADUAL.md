# Aturcara Rasmi — Kursus Visualisasi Data & Dashboard Pintar Berasaskan AI (Power BI · Fabric · Copilot)

> Sumber rasmi: **Cadangan Use Case** — *Kursus Visualisasi Data dan Dashboard Pintar Berasaskan AI*, disediakan untuk **Kementerian Kemajuan Desa dan Wilayah (KKDW)** — versi 1.0 (2026). Modul ini **mengikut** aliran pembelajaran yang dicadangkan (Data → Fabric → Power BI → Analitik → Copilot/AI); jangan ubah skop hari tanpa menyemaknya.
>
> **Tema kursus:** *Dashboard Pintar Pemantauan Prestasi Program JPD & BELB Bersepadu dengan MyProjek* — menukar data projek luar bandar kepada insight yang menyokong keputusan pengurusan.

## Maklumat Sesi

| Perkara | Butiran |
|---------|---------|
| **Kod Kursus** | BI-FABRIC-KKDW-101 |
| **Tempoh** | 3 Hari (~15.25 jam kontak) |
| **Tahap** | Permulaan hingga Pertengahan — *tiada pengalaman pengaturcaraan diperlukan* |
| **Tarikh** | *(indikatif)* — untuk disahkan dengan KKDW |
| **Masa** | **Rabu** 4.00 ptg – 10.00 mlm · **Khamis** 8.30 pg – 6.00 ptg · **Jumaat** 8.30 pg – 12.30 tgh |
| **Mod** | Fizikal / Maya / Hibrid (makmal komputer disyorkan) |
| **Anjuran** | Kementerian Kemajuan Desa dan Wilayah (KKDW) |
| **Bilangan peserta disyorkan** | 15 – 25 orang |

> **Rentak harian (jadual baharu — 3 blok berbeza):**
> - **Rabu (Hari 1) — 4.00 petang hingga 10.00 malam:** sesi petang 4.00–7.00; **rehat, makan malam & solat Maghrib 7.00–8.00**; sesi malam 8.00–10.00. (~4.75 jam kontak)
> - **Khamis (Hari 2) — 8.30 pagi hingga 6.00 petang:** pendaftaran 8.30–9.00; sesi pagi 9.00–1.00; **rehat, makan tengah hari & solat Zohor 1.00–2.30**; sesi petang 2.30–6.00. (~7 jam kontak)
> - **Jumaat (Hari 3) — 8.30 pagi hingga 12.30 tengah hari:** sesi separuh hari, **tamat sebelum solat Jumaat**. (~3.5 jam kontak)

> **Konvensyen bahasa:** Nota & penerangan dalam **Bahasa Melayu**; nama medan data, fungsi DAX, istilah Power BI/Fabric dikekalkan dalam **Bahasa Inggeris** (amalan standard industri).

---

## HARI 1 — Fondasi Data: Microsoft Fabric, Power Query & Pemodelan · **Rabu (4.00 petang – 10.00 malam)**

**Fokus:** Bina fondasi data yang kukuh sebelum bina visual. Habiskan hari dengan satu **model data bersepadu** (JPD + BELB + MyProjek) yang sedia untuk analisis. *(Blok petang–malam; sesi lebih padat berbanding sehari penuh.)*

| Masa | Agenda |
|------|--------|
| 4.00 – 4.15 petang | Pendaftaran Peserta & Taklimat Ringkas |
| **4.15 – 5.30 petang** | **SESI 1: Pengenalan — Ekosistem Data & Konteks KKDW**<br>• Kenapa visualisasi data? · Landskap Power BI, Microsoft Fabric & Copilot<br>• Aliran kerja: Data → Fabric → Power BI → Analitik → AI<br>• Kes sebenar KKDW: JPD, BELB & MyProjek · Persediaan Power BI Desktop<br>• 🧠 **Bengkel:** Kenal pasti soalan pengurusan yang dashboard perlu jawab |
| **5.30 – 7.00 petang** | **SESI 2: Microsoft Fabric & Menyambung Data**<br>• Konsep OneLake, Workspace, Lakehouse & lesen Fabric<br>• Komponen: Data Factory (Dataflows Gen2), Notebook, Semantic Model<br>• Import vs DirectQuery · Menyambung fail Excel (JPD, BELB, MyProjek)<br>• 💻 **Lab:** Muat naik 3 set data ke Power BI / Lakehouse |
| 7.00 – 8.00 malam | Rehat, Makan Malam & Solat Maghrib |
| **8.00 – 8.50 malam** | **SESI 3: Transformasi Data dengan Power Query**<br>• Power Query Editor & "Applied Steps" · Tukar jenis data · Kendali null<br>• Standardkan medan kunci: `negeri`, `daerah`, `status_pelaksanaan`<br>• Conditional Column (kategori status projek)<br>• 💻 **Lab:** Bersihkan set data JPD & BELB |
| **8.50 – 9.25 malam** | **SESI 4: Integrasi & Penggabungan Data**<br>• Merge (gabung lajur) vs Append (susun baris) · Kunci padanan `kod_projek`<br>• Gabungkan JPD + BELB + MyProjek kepada struktur konsisten<br>• 💻 **Latihan:** Bina jadual projek bersepadu |
| **9.25 – 10.00 malam** | **SESI 5: Pemodelan Data (Data Modeling)**<br>• Star Schema — jadual Fakta vs Dimensi · Date table<br>• Dimension: Negeri, Daerah, Agensi, Status · Relationships & kardinaliti<br>• 💻 **Lab:** Bina model data bersepadu (deliverable Hari 1) |
| 10.00 malam | Bersurai |

**Hasil Hari 1:** Peserta faham ekosistem Fabric/Power BI dan sudah membina **satu model data bersepadu** JPD + BELB + MyProjek yang bersih dan sedia untuk analisis.

> Hari ini **belum** menyentuh DAX kompleks, visual atau Copilot — semua itu **Hari 2 & 3**. Fokus hari ini **semata-mata** data yang betul, bersih dan bermodel.

---

## HARI 2 — Power BI: DAX, Visualisasi & Pembinaan Dashboard · **Khamis (8.30 pagi – 6.00 petang)**

**Fokus:** Tukar model data kepada **dashboard pengurusan interaktif** — kira KPI dengan DAX, bina visual & drill-down, dan terbitkan ke Power BI Service. *(Hari paling panjang — teras pembinaan dashboard.)*

| Masa | Agenda |
|------|--------|
| 8.30 – 9.00 pagi | Pendaftaran Peserta & Minum Pagi |
| **9.00 – 10.45 pagi** | **SESI 6: Pengiraan dengan DAX**<br>• Calculated Column vs Measure · Filter Context (ringkas & praktikal)<br>• SUM, AVERAGE, COUNT, DISTINCTCOUNT · CALCULATE, FILTER, IF, SWITCH<br>• KPI: Jumlah Projek, Peruntukan, Belanja, Baki, % Utilisasi<br>• 💻 **Lab:** Bina 8 measure teras KKDW |
| 10.45 – 11.00 pagi | Rehat |
| **11.00 – 1.00 tgh** | **SESI 7: Visualisasi Data Berkesan**<br>• Memilih visual betul: Card/KPI, Bar, Column, Line, Matrix, Donut<br>• Prinsip reka bentuk dashboard pengurusan · Conditional Formatting<br>• 💻 **Lab:** Bina visual JPD & BELB mengikut negeri/status |
| 1.00 – 2.30 petang | Rehat, Makan Tengah Hari & Solat Zohor |
| **2.30 – 4.00 petang** | **SESI 8: Interaktiviti, Drill-Down & Peta**<br>• Slicer, Filters, cross-filtering · Drill-down & Drill-through<br>• Hierarki: Malaysia → Negeri → Parlimen → DUN → Kampung → Projek<br>• Peta (Map / Filled Map) guna `lat/long` & negeri<br>• 💻 **Lab:** Tambah navigasi & peta lokasi projek |
| 4.00 – 4.15 petang | Rehat |
| **4.15 – 5.15 petang** | **SESI 9: Membina Dashboard Bersepadu**<br>• Halaman 1 Executive Overview · Halaman 2 JPD Performance<br>• Halaman 3 BELB Performance · Halaman 4 Financial & Physical Progress<br>• 💻 **Lab:** Bina 4 halaman dashboard (deliverable Hari 2) |
| **5.15 – 6.00 petang** | **SESI 10: Menerbit & Berkongsi (Power BI Service)**<br>• Publish ke Workspace · Refresh data & penjadualan<br>• Report vs Dashboard vs App · Row-Level Security (RLS) ringkas |
| 6.00 petang | Bersurai |

**Hasil Hari 2:** Dashboard pengurusan berfungsi dengan 4 halaman (Executive, JPD, BELB, Financial), interaktif dengan drill-down & peta, dan telah diterbitkan ke Power BI Service.

---

## HARI 3 — Analitik Risiko, Copilot / AI & Capstone · **Jumaat (8.30 pagi – 12.30 tengah hari)**

**Fokus:** Naik taraf dashboard kepada **intelligence** — kesan risiko & anomali dengan analitik, dan guna Copilot/AI untuk insight & ringkasan pengurusan, sehingga capstone. *(Separuh hari — padat & lebih berfokus demo; kerja lab lanjutan boleh disambung sebagai tugasan susulan.)*

| Masa | Agenda |
|------|--------|
| 8.30 – 8.45 pagi | Pendaftaran & Sambung Semula (taklimat ringkas) |
| **8.45 – 9.45 pagi** | **SESI 11: Analitik Risiko & Early Warning**<br>• Varians % Jadual vs % Sebenar · Indikator Hijau/Kuning/Merah<br>• Early Warning projek lewat · DAX untuk skor risiko<br>• 💻 **Lab:** Bina measure varians + pemformatan bersyarat risiko |
| **9.45 – 10.30 pagi** | **SESI 12: Fizikal vs Kewangan, Risk Score & Priority Index**<br>• Kemajuan fizikal vs kadar belanja (under/over-utilisation)<br>• Project Risk Score (varians + kadar belanja + status)<br>• Kos per KM (JPD), Kos per Sambungan (BELB) · Priority Index<br>• 💻 **Lab:** Bina halaman "AI Project Risk & Early Warning" |
| 10.30 – 10.45 pagi | Rehat |
| **10.45 – 11.20 pagi** | **SESI 13: Ciri Analitik AI Terbina dalam Power BI**<br>• Key Influencers · Decomposition Tree · Smart Narrative<br>• Anomaly detection · "Explain the increase/decrease"<br>• 🔎 **Demo:** Gunakan visual AI ke atas data projek |
| **11.20 – 11.55 pagi** | **SESI 14: Copilot / AI sebagai Pegawai Analisis Maya**<br>• Copilot dalam Power BI & Fabric · Keperluan lesen & persediaan<br>• Pertanyaan bahasa semula jadi (Q&A) · Naratif & penjanaan DAX<br>• Amalan terbaik & batasan AI (semak sebelum guna)<br>• 💻 **Demo + Lab:** pertanyaan Copilot gaya-pengurusan KKDW |
| **11.55 – 12.30 tgh** | **Projek Capstone + Demo & Sijil**<br>• Pembentangan ringkas dashboard · Penilaian · Sijil |
| 12.30 tengah hari | Bersurai (sebelum solat Jumaat) |

**Hasil Hari 3:** Dashboard intelligence lengkap dengan analitik risiko + Copilot/AI, dan projek capstone yang dibentang.

---

## Pemetaan Sesi → Deliverable

| Sesi | Deliverable / Artifak |
|------|------------------------|
| SESI 2 | Data JPD/BELB/MyProjek dimuat ke Power BI / Lakehouse |
| SESI 3–4 | Query Power Query bersih + jadual projek bersepadu |
| SESI 5 | **Model data bersepadu** (`hari-1.pbix`) |
| SESI 6 | 8 measure DAX teras KKDW |
| SESI 8–9 | **Dashboard 4 halaman** (`hari-2.pbix`) |
| SESI 10 | Laporan diterbit ke Power BI Service |
| SESI 11–12 | Measures risiko + halaman **AI Project Risk & Early Warning** |
| SESI 14 | Log 5 pertanyaan Copilot + ringkasan eksekutif |
| Capstone | **KKDW Rural Infrastructure Intelligence Dashboard** (`capstone.pbix`) |

## Soalan Pengurusan Utama (Capstone)

> *"Daripada keseluruhan portfolio JPD dan BELB, projek dan kawasan manakah yang perlu diberi perhatian atau keutamaan oleh pengurusan KKDW, dan mengapa?"*

Peserta menggunakan dashboard **dan** Copilot/AI untuk menjawab soalan ini — mengaplikasikan keseluruhan proses daripada penyediaan data, pemodelan, visualisasi, analitik risiko, sehingga penjanaan cadangan yang menyokong keputusan.

## Kriteria Penilaian (Capstone)

| Kriteria | Wajaran |
|----------|---------|
| Penyediaan & pemodelan data | 20% |
| KPI & measures (DAX) | 20% |
| Reka bentuk dashboard & interaktiviti | 20% |
| Analitik risiko & penggunaan Copilot/AI | 20% |
| Pembentangan & cadangan pengurusan | 20% |

> Peserta yang lengkap semua latihan, dashboard 4 halaman (Hari 2), analitik risiko (Hari 3), projek capstone & pembentangan akan menerima **Sijil Penyertaan** — *Visualisasi Data & Dashboard Pintar Berasaskan AI dengan Power BI, Fabric & Copilot*.
