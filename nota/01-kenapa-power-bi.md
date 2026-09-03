# Nota Konsep: Kenapa Power BI?

> Nota latar belakang — baca **sebelum** SESI 1 (Hari 1). Fahami **kenapa** KKDW guna Power BI untuk pemantauan projek luar bandar sebelum belajar **bagaimana** menggunakannya.

---

## Masalah sebenar KKDW

KKDW memantau **ribuan projek** merentas negeri, daerah, parlimen, DUN dan kampung. Set data kursus sahaja sudah ada **1,376 projek JPD**, **23 projek BELB**, dan **77 projek MyProjek** — dan itu baru sebahagian kecil portfolio sebenar.

Dalam bentuk jadual Excel mentah, pengurusan sukar melihat dengan pantas:

- Projek mana **lewat** atau **berisiko**? (bandingkan `peratus_jadual_projek` vs `peratus_sebenar_projek`)
- Negeri mana perlu diberi **keutamaan**? (kumpul ikut `kod_negeri`)
- Di mana **peruntukan** tinggi tetapi **kemajuan fizikal** rendah? (`belanja_janm` vs `peratus_sebenar_projek`)

Setiap soalan ini boleh dijawab dalam Excel — tetapi memerlukan pivot table, VLOOKUP dan formula manual yang perlu dibina **semula** setiap kali data berubah. Power BI menyelesaikan tepat masalah ini.

---

## Apa itu Power BI?

**Power BI** ialah alat **business intelligence** Microsoft untuk menukar data mentah kepada **visual, dashboard dan laporan interaktif**. Anda sambung ke data sekali, model ia sekali, dan setiap kali data dikemas kini, dashboard **segar automatik** — tanpa membina semula carta.

Tiga bahagian utama:

| Bahagian | Peranan | Bila digunakan |
|----------|---------|----------------|
| **Power BI Service / Fabric (pelayar)** | Bina model, DAX, visual, dashboard — **laluan utama kursus** | Hari 1–3 |
| **Power BI Desktop** | Sama, tetapi aplikasi Windows (percuma) | *Pilihan* (luar talian) |
| **Power BI Service** | Terbit, kongsi & jadualkan refresh (awan) | Hari 2 |
| **Power BI Mobile** | Lihat dashboard di telefon/tablet | Selepas kursus |

> **Analogi KKDW:** Excel ialah **buku nota** — bagus untuk satu jadual, satu masa. Power BI ialah **bilik pameran** yang menyambung semua data projek KKDW dan mempamerkan prestasinya dengan carta & peta yang boleh diklik.

---

## Power BI vs Excel — bila guna yang mana?

Excel **bukan** musuh — ia bagus untuk kemasukan data, kiraan pantas dan jadual kecil. Tetapi untuk pemantauan portfolio KKDW yang besar & berulang, Power BI menang:

| | **Excel** | **Power BI** |
|---|-----------|--------------|
| Saiz data | Perlahan melebihi ratusan ribu baris | Cekap dengan jutaan baris |
| Kemas kini | Bina semula formula/pivot manual | **Refresh sekali klik** (atau berjadual) |
| Hubungan antara jadual | VLOOKUP rapuh | **Relationships** model data (star schema) |
| Interaktiviti | Terhad (slicer asas) | Drill-down, cross-filter, peta, drill-through |
| Visual | Carta statik | Visual interaktif + visual AI terbina |
| Kongsi & keselamatan | Hantar fail (salinan bertaburan) | Terbit sekali + **Row-Level Security** |
| Pengiraan | Formula per-sel | **DAX** — satu measure, banyak konteks |

> **Ringkasnya:** guna Excel untuk **memasukkan & menyunting** data; guna Power BI untuk **memantau, menganalisis & berkongsi** data berulang kali. Untuk 1,376 projek JPD yang dikemas kini setiap bulan, Power BI menjimatkan berjam-jam kerja manual.

---

## Kenapa Power BI sesuai untuk sektor awam

1. **Integrasi Microsoft 365** — kebanyakan agensi kerajaan sudah guna Microsoft 365; Power BI masuk terus tanpa lesen berasingan yang mahal untuk permulaan.
2. **Keselamatan & tadbir urus** — Row-Level Security, kawalan capaian Workspace, dan residensi data — penting untuk data projek yang sensitif (lihat [`08-tadbir-urus-keselamatan.md`](./08-tadbir-urus-keselamatan.md)).
3. **No-code / low-code** — pegawai KKDW membina dashboard secara **visual**, tanpa perlu jadi pengaturcara. DAX ialah satu-satunya "kod", dan ia diterangkan baris demi baris ([`05-dax-asas.md`](./05-dax-asas.md)).
4. **Skala kerajaan** — dari satu dashboard jabatan sehingga platform data seluruh kementerian melalui **Microsoft Fabric** ([`02-fabric-onelake.md`](./02-fabric-onelake.md)).
5. **AI terbina** — Key Influencers, Smart Narrative dan **Copilot** memberi insight tanpa perlu pakar data ([`07-copilot-ai.md`](./07-copilot-ai.md)).

---

## Peranan Power BI dalam kursus ini

Sepanjang 3 hari, Power BI ialah alat utama yang menyatukan segalanya: sediakan & model data JPD/BELB/MyProjek (Hari 1), kira KPI dengan DAX & bina dashboard (Hari 2), dan analitik risiko + Copilot (Hari 3) — sehingga **KKDW Rural Infrastructure Intelligence Dashboard** yang lengkap.

> **Prinsip sepanjang kursus:** *AI membantu, anda memandu.* Power BI mempercepatkan analisis, tetapi keputusan keutamaan pembangunan tetap di tangan pengurusan KKDW — sentiasa semak insight terhadap data sumber.

---

Seterusnya: [`02-fabric-onelake.md`](./02-fabric-onelake.md) — platform data di sebalik Power BI. Kemudian mula hands-on di [Hari 1](../hari-1/README.md).

## Sumber Rasmi

- **[powerbi.microsoft.com](https://powerbi.microsoft.com/)** — laman rasmi Power BI.
- **[learn.microsoft.com/power-bi](https://learn.microsoft.com/power-bi/)** — dokumentasi rasmi.
- **[powerbi.microsoft.com/desktop](https://powerbi.microsoft.com/desktop/)** — muat turun Power BI Desktop (percuma).
