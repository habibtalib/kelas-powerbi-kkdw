# Hari 1 — Edaran Peserta (Handout)

**Kursus Visualisasi Data & Dashboard Pintar Berasaskan AI · Power BI · Microsoft Fabric · Copilot** (KKDW)
**Rabu · 4.00 petang – 10.00 malam** · *Fondasi Data*

---

## 🎯 Matlamat hari ini
Bina **satu model data bersepadu** yang bersih daripada 3 set data KKDW — **sebelum** kita bina visual (itu Hari 2). *Dashboard yang baik bermula dengan data yang betul.*

## 🧱 Apa anda akan bina
Data mentah (Excel) → dibersih (Power Query) → digabung (Append) → **model star schema** (Fakta + Dimensi + Date table + relationships). Deliverable: **`hari-1.pbix`** / semantic model.

## 📊 Data KKDW
| Set data | Isi | Baris |
|---|---|---|
| **JPD** | Jalan Perhubungan Desa | 1,376 |
| **BELB** | Bekalan Elektrik Luar Bandar | 23 |
| **MyProjek** | Pemantauan RMK (kos, peruntukan, belanja, % kemajuan) | 77 |

## 🗓️ 5 sesi hari ini
| Masa | Sesi | Anda buat |
|---|---|---|
| 4.15–5.30 ptg | **SESI 1** Ekosistem & konteks KKDW | 🧠 Senarai 5 soalan pengurusan |
| 5.30–7.00 ptg | **SESI 2** Fabric & sambung data | 💻 Muat naik 3 set data |
| *7.00–8.00 mlm* | *Rehat / makan malam / Maghrib* | |
| 8.00–8.50 mlm | **SESI 3** Power Query | 💻 Bersihkan JPD & BELB |
| 8.50–9.25 mlm | **SESI 4** Integrasi | 💻 Gabung → `Projek_Program` |
| 9.25–10.00 mlm | **SESI 5** Pemodelan | 💻 Star schema + relationships |

## 🔑 Istilah penting
- **OneLake** — "OneDrive untuk data": satu tasik data untuk seluruh organisasi.
- **Lakehouse** — fail mentah **+** jadual berstruktur dalam satu tempat.
- **Dataflow Gen2** — Power Query di awan (transformasi boleh dijadual).
- **Power Query** — alat bersih & transform data; setiap langkah direkod (**Applied Steps**).
- **Append vs Merge** — Append = susun **baris** (JPD+BELB); Merge = gabung **lajur** ikut kunci.
- **Star Schema** — jadual **Fakta** (nombor: kos, belanja, %) dikelilingi jadual **Dimensi** (Negeri, Tarikh, Agensi).
- **Semantic Model** — model data (jadual + relationships + measures) yang jadi sumber laporan.

## ✅ Checklist sebelum balik
- [ ] Log masuk Fabric (pelayar) **atau** Power BI Desktop *(Latihan 0)*
- [ ] 3 set data dimuat & dibersihkan dalam Power Query
- [ ] Medan `kod_*` = **Text**; `status_pelaksanaan`, kewangan bertaip betul
- [ ] `kategori_status` dicipta (Siap / Dalam Pelaksanaan / Belum Mula)
- [ ] `Projek_Program` = 1,399 baris (JPD + BELB)
- [ ] `Dim_Negeri` · `Dim_Tarikh` (Mark as Date Table) · `Dim_Agensi` + relationships
- [ ] Simpan `hari-1.pbix`

## 💻 Prasyarat
- **Laluan A (mana-mana OS):** pelayar → `app.fabric.microsoft.com` → log masuk akaun KKDW → workspace Fabric (F2+).
- **Laluan B (Windows):** pasang **Power BI Desktop** (percuma, Microsoft Store) → log masuk.
- *Tiada pengalaman pengaturcaraan diperlukan — semua dibina secara visual.*

> Lab penuh langkah demi langkah: **`hari-1/snippets/lab.md`**. Nota konsep: **`hari-1/README.md`**.
