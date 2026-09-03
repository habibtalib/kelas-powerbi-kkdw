# Nota Konsep: Tadbir Urus & Keselamatan

> Nota latar belakang untuk SESI 10 (Hari 2) & SESI 14 (Hari 3). Data projek KKDW ialah **data kerajaan** — cara ia dikongsi, dilindungi dan ditadbir sama pentingnya dengan analitiknya.

---

## Kenapa tadbir urus penting untuk KKDW

Dashboard yang hebat tetapi berkongsi data secara sembarangan boleh menyebabkan **kebocoran maklumat sensitif** atau **pegawai melihat data di luar bidang kuasa mereka**. Untuk sektor awam, tadbir urus data bukan pilihan — ia **keperluan**.

> **Analogi KKDW:** dashboard ialah bilik pameran, tetapi tidak semua orang patut masuk semua bilik. Pegawai negeri Sabah patut nampak projek Sabah; hanya pengurusan atasan nampak keseluruhan portfolio. Tadbir urus ialah **sistem kunci & kad akses** bilik pameran itu.

---

## Row-Level Security (RLS)

**RLS** mengehadkan **baris data** yang dilihat setiap pengguna, berdasarkan siapa mereka — walaupun mereka lihat dashboard yang sama.

Contoh KKDW: pegawai negeri Sabah log masuk → hanya nampak projek Sabah; pegawai Sarawak → hanya Sarawak; pengurusan pusat → semua.

### Cara ia berfungsi (ringkas)

1. Dalam **Power BI Service** → buka **`KKDW_Model` → Open data model → Manage roles** — buat peranan, contoh `Sabah`.
2. Tetapkan penapis DAX pada jadual, contoh:
   ```dax
   [kod_negeri] = "12"
   ```
3. **Tugaskan pengguna** kepada peranan itu dalam Power BI Service (selepas Publish).

| Konsep RLS | Maksud |
|------------|--------|
| **Static RLS** | Peranan tetap, penapis ditetapkan (contoh satu peranan per negeri) |
| **Dynamic RLS** | Penapis guna `USERPRINCIPALNAME()` — satu peranan, automatik ikut pengguna log masuk |

> RLS **mesti diuji** (View as role) sebelum diterbitkan, dan laksana penuh bergantung pada **dasar capaian rasmi KKDW** — siapa patut nampak apa.

---

## Object-Level Security (OLS) — sekat lajur/jadual

RLS menyembunyikan **baris**; **OLS** menyembunyikan **lajur atau jadual** penuh daripada pengguna tertentu. Guna OLS bila sesetengah **medan** sensitif walaupun barisnya boleh dilihat.

| Teknik | Sekat apa | Contoh KKDW |
|--------|-----------|-------------|
| **RLS** (Row-Level Security) | **Baris** | Pegawai Sabah nampak projek Sabah sahaja |
| **OLS** (Object-Level Security) | **Lajur / jadual** | Sembunyikan lajur kos terperinci daripada pegawai lapangan |

> Kedua-dua **RLS dan OLS dihormati oleh Copilot** — jawapan AI turut terhad kepada data yang pengguna dibenarkan lihat (lihat [`07-copilot-ai.md`](./07-copilot-ai.md)). Data juga **disulitkan (encrypted at rest)** secara lalai dalam Power BI.

---

## Residensi data

**Residensi data** ialah soal **di mana** data disimpan secara fizikal (wilayah geografi pusat data). Untuk data kerajaan Malaysia, ini selalunya keperluan pematuhan.

Perkara yang perlu disahkan dengan pentadbir IT KKDW:

- **Wilayah tenant** — di mana data Power BI Service / Fabric disimpan.
- **Aliran data ke perkhidmatan AI** — adakah data dihantar keluar bila Copilot digunakan?
- **Klasifikasi data** — data mana boleh ke awan, data mana kekal dalaman.

> **Prinsip:** untuk data terperingkat, **jangan** hantar ke perkhidmatan AI luar kawalan tanpa kelulusan. Sahkan dasar dengan IT sebelum guna Copilot atas data sebenar (lihat [`07-copilot-ai.md`](./07-copilot-ai.md)).

---

## Lesen Fabric & Copilot — implikasi tadbir urus

Lesen bukan sekadar kos — ia menentukan **di mana** dan **bagaimana** data diproses:

| Lapisan | Lesen | Nota tadbir urus |
|---------|-------|------------------|
| Power BI Desktop | Percuma | Data dalam fail `.pbix` di komputer pegawai — lindungi fail |
| Publish & kongsi | Power BI Pro | Kawal keahlian Workspace |
| Fabric penuh + Copilot | **F64+ / Premium** | OneLake, Lakehouse, Copilot — sahkan wilayah & dasar AI |

Sahkan konfigurasi lesen dan kesan residensinya dengan pentadbir IT sebelum penggunaan meluas.

---

## Perkongsian selamat Workspace

Bila menerbit ke Power BI Service, kawal capaian dengan teliti:

- **Workspace** — kongsi hanya kepada ahli yang dibenarkan; jangan buat "public".
- **Peranan Workspace** — *Viewer* (lihat sahaja), *Contributor*, *Member*, *Admin* — beri peranan **paling minimum** yang diperlukan (*least privilege*).
- **App** — untuk pengguna akhir, terbitkan sebagai **App** (paket dikawal), bukan beri capaian Workspace mentah.
- **Elak hantar fail `.pbix`** — salinan bertaburan hilang kawalan; kongsi melalui Service dengan RLS.

```
Pembina model  →  Workspace (Contributor)  →  App diterbit  →  Pengguna akhir (Viewer + RLS)
                   kawalan penuh                paket dikawal    nampak data yang dibenarkan sahaja
```

---

## Endorsement — tanda "boleh dipercayai"

Bila banyak laporan wujud, pengguna perlu tahu **mana yang rasmi**. Power BI membenarkan **endorsement badge** pada artifact (kecuali dashboard):

| Badge | Maksud | Siapa boleh tetapkan |
|-------|--------|----------------------|
| **Promoted** | Penulis rasa ia sedia diguna — **belum** disahkan orang lain | Ahli Workspace / pemilik artifact |
| **Certified** | Disahkan rasmi & dipercayai oleh organisasi | Hanya pengguna yang dibenarkan (tetapan tenant) |
| **Master** | Data induk / *single source of truth* (contoh senarai negeri, agensi) | Untuk aset data — Lakehouse, semantic model |

> Untuk KKDW: model bersepadu JPD+BELB+MyProjek yang muktamad patut **di-*Certified*** supaya pegawai tahu itulah sumber rasmi, bukan salinan lama seseorang.

## Deployment pipelines & Git *(rujukan lanjutan — di luar skop kursus)*

Untuk penerbitan berperingkat, Power BI ada **deployment pipelines** (alir kerja **Development → Test → Production**) dan **Git integration** (versi & kawalan perubahan). Ini keperluan **F64+/Premium** dan lebih sesuai untuk pasukan IT.

> **Bukan sebahagian kursus 3 hari ini** — disebut supaya KKDW tahu laluan pengeluaran (*production*) yang betul bila dashboard dinaik taraf daripada `.pbix` tunggal kepada operasi berpasukan. Sensitivity labels (Microsoft Purview) untuk pelabelan kerahsiaan data juga tergolong di lapisan lanjutan ini.

---

## Dasar capaian KKDW — senarai semak

Sebelum dashboard KKDW digunakan secara rasmi, sahkan:

- [ ] **RLS** dikonfigur mengikut bidang kuasa (negeri/jabatan) & diuji
- [ ] **OLS** dipertimbang untuk lajur/jadual sensitif (jika perlu)
- [ ] Model rasmi **di-*Certified*** supaya pegawai kenal sumber sebenar
- [ ] **Peranan Workspace** diberi secara *least privilege*
- [ ] **Residensi data** disahkan dengan IT (wilayah tenant, aliran AI)
- [ ] **Lesen Fabric/Copilot** disahkan sebelum guna ciri AI atas data sebenar
- [ ] **Data sensitif** tidak dihantar ke perkhidmatan luar tanpa kelulusan
- [ ] **Refresh berjadual** dikonfigur supaya data terkini tetapi selamat

---

Kembali ke keseluruhan: [Hari 2 SESI 10](../hari-2/README.md#sesi-10-430--500--menerbit--berkongsi-power-bi-service) (Publish & RLS) · **Hari 3 SESI 14** (tadbir urus Copilot) *(diteruskan semasa kelas)* · 🏠 [Nota Utama](../README.md).

## Sumber Rasmi

- **[learn.microsoft.com/power-bi/enterprise/service-admin-rls](https://learn.microsoft.com/power-bi/enterprise/service-admin-rls)** — Row-Level Security.
- **[learn.microsoft.com/power-bi/guidance/whitepaper-powerbi-security](https://learn.microsoft.com/power-bi/guidance/whitepaper-powerbi-security)** — keselamatan Power BI.
- **[learn.microsoft.com/fabric/admin/region-availability](https://learn.microsoft.com/fabric/admin/region-availability)** — wilayah & residensi Fabric.
- **[learn.microsoft.com/power-bi/collaborate-share/service-endorse-content](https://learn.microsoft.com/power-bi/collaborate-share/service-endorse-content)** — endorsement (Promoted/Certified).
- 📘 *Architecting Power BI Solutions in Microsoft Fabric* (Packt) — Bab 10 *Managing Semantic Model Security* (ms 233–247): OLS ms 240, RLS ms 243; Bab 11 *Performing Power BI Deployments* (ms 249–267): endorsement ms 250, deployment pipelines ms 252, Git ms 259; Bab 15 sensitivity labels (Purview) ms 336; Bab 16 *Designing Power BI Governance* ms 357.
