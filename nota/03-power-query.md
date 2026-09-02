# Nota Konsep: Transformasi Data dengan Power Query

> Nota latar belakang untuk SESI 3–4 (Hari 1). Power Query ialah tempat data **mentah** menjadi data **bersih & sedia** untuk analisis. Fahami konsepnya di sini sebelum lab.

---

## Kenapa perlu transform dahulu?

Data mentah **jarang** sedia untuk analisis. Dalam fail KKDW sebenar, anda akan jumpa:

- Jenis data salah — `kos_projek` disimpan sebagai **teks**, bukan nombor (tak boleh dijumlah).
- Medan tidak seragam — `status_pelaksanaan` ditulis "Sabah" vs "SABAH" vs " sabah ".
- Lajur kosong / `null` pada medan kewangan.
- Lajur teknikal tak berguna (`created_at`, `updated_at`).

Kalau data ini terus dibawa ke dashboard, hasil analisis akan **salah** — dan keputusan pengurusan yang dibuat atasnya pun salah.

> **Analogi KKDW:** Power Query ialah **bilik penyediaan** sebelum pameran. Data projek dibersih, disusun dan distandardkan di sini — supaya bila ia sampai ke dashboard, ia betul dan boleh dipercayai.

---

## Kuasa besar Power Query: Applied Steps

Perbezaan utama Power Query berbanding membersih data manual dalam Excel: ia **merekod setiap langkah** dalam senarai **Applied Steps** di sebelah kanan.

```
Applied Steps:
  1. Source                    ← muat fail Excel
  2. Removed Columns           ← buang created_at, updated_at
  3. Changed Type              ← kos_projek → Decimal Number
  4. Uppercased Text           ← status_pelaksanaan → UPPERCASE
  5. Added Conditional Column  ← cipta kategori_status
```

Kenapa ini berkuasa: bila data KKDW dikemas kini bulan depan, anda **tidak perlu ulang** semua kerja. Klik **Refresh**, dan Power Query jalankan **semua langkah** secara automatik pada data baru. Setiap langkah boleh di-*undo*, diedit atau disusun semula bila-bila masa.

---

## Betulkan jenis data (Data Type)

Setiap lajur mesti ada jenis data yang betul, jika tidak pengiraan gagal:

| Medan | Jenis betul | Kenapa |
|-------|-------------|--------|
| `kos_projek`, `panjang_jalan` | **Decimal Number** | Supaya boleh dijumlah & dibahagi (Kos per KM) |
| `tahun`, `tahun_mula` | **Whole Number** | Nombor bulat, untuk Date table |
| `kod_negeri`, `kod_daerah` | **Text** | Kod (contoh "12") — bukan untuk dikira, kekal sebagai teks |
| `peratus_sebenar_projek` | **Decimal / Percentage** | Untuk kiraan varians risiko (Hari 3) |

> **Perhatian `kod_negeri`:** walaupun ia kelihatan seperti nombor, ia **kod pengenalan**, bukan kuantiti. Jika dibiarkan sebagai nombor, Power BI mungkin cuba **menjumlahkannya** — yang tidak bermakna. Set sebagai **Text**.

---

## Kendali null & buang lajur

- **Buang lajur tak perlu** — pilih `created_at`, `updated_at`, `tarikh_upload` → klik kanan → **Remove Columns**. Model lebih kecil & laju.
- **Ganti null** — pada medan kewangan (`belanja_janm`), gantikan `null` dengan `0` **bila sesuai** (Transform → Replace Values). Berhati-hati: `null` kadang bermaksud "belum ada data", bukan "sifar" — fikir konteks dahulu.

---

## Standardkan medan kunci

Padanan & tapisan hanya tepat jika teks **seragam**. Contoh, `status_pelaksanaan` dalam `data_jpd` sebenarnya hanya ada dua nilai — tetapi ejaan/huruf besar boleh berbeza:

1. Pilih `status_pelaksanaan` → **Transform → Format → UPPERCASE**.
2. Kemudian **Trim** (buang ruang berlebihan di hujung).

Ulang untuk `kod_negeri` dan medan lokasi lain. Selepas ini, "Dalam Pelaksanaan" tidak lagi berpecah kepada beberapa versi berbeza dalam visual.

---

## Conditional Column — cipta kategori baru

**Conditional Column** mencipta lajur baru berdasarkan syarat — seperti `IF` bertingkat, tetapi visual. Contoh sebenar KKDW: ringkaskan `status_pelaksanaan` kepada `kategori_status`:

```
JIKA status_pelaksanaan = "PASCA PELAKSANAAN"  → "Siap"
JIKA status_pelaksanaan = "DALAM PELAKSANAAN"  → "Dalam Pelaksanaan"
selainnya                                      → "Belum Mula / Lain"
```

> **Data sebenar:** dalam `data_jpd`, `status_pelaksanaan` ialah *PASCA PELAKSANAAN* (949 projek) atau *DALAM PELAKSANAAN* (405 projek). `kategori_status` ini akan memberi warna status yang konsisten (Hijau=Siap) sepanjang dashboard.

---

## Merge vs Append — dua cara gabung data

Data KKDW datang dalam **tiga fail berasingan**. Ada dua cara menggabungkannya, dan ia **berbeza sama sekali**:

| | **Append** (susun baris) | **Merge** (gabung lajur) |
|---|--------------------------|--------------------------|
| Buat apa | Cantum baris jadual berstruktur **sama** | Bawa lajur dari satu jadual ke lain |
| Ibarat | Menyusun dua senarai jadi satu senarai panjang | VLOOKUP — tarik maklumat padanan |
| Perlu | Lajur yang sama | **Kunci padanan** (contoh `kod_projek`) |
| Contoh KKDW | Gabung JPD + BELB → satu jadual `Projek_Program` dengan lajur `program` | Tarik `kos_keseluruhan`, `belanja_janm` dari MyProjek ke jadual projek |

```
APPEND:  [JPD baris]  +  [BELB baris]  →  [Projek_Program: semua baris, lajur program = JPD/BELB]

MERGE:   [Projek_Program]  ⋈ kod_projek ⋈  [MyProjek]  →  [+ lajur kewangan dikembangkan]
```

> **Untuk KKDW:** kita *Append* JPD + BELB menjadi satu jadual operasi program (guna `kod_negeri`, `kos_projek`, `status_pelaksanaan`, `program`), kemudian *Merge* dengan MyProjek untuk membawa masuk maklumat kewangan.

Selepas semua langkah selesai, klik **Close & Apply** untuk muat data bersih ke model.

---

Seterusnya: [`04-pemodelan-star-schema.md`](./04-pemodelan-star-schema.md) — susun jadual bersih ini kepada model yang cekap. Lab hands-on: [Hari 1 Latihan 3–4](../hari-1/snippets/lab.md#latihan-3--bersihkan-data-jpd--belb).

## Sumber Rasmi

- **[learn.microsoft.com/power-query](https://learn.microsoft.com/power-query/)** — dokumentasi Power Query.
- **[learn.microsoft.com/power-query/merge-queries-overview](https://learn.microsoft.com/power-query/merge-queries-overview)** — Merge.
- **[learn.microsoft.com/power-query/append-queries](https://learn.microsoft.com/power-query/append-queries)** — Append.
