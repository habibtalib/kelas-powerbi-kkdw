# Nota Konsep: DAX Asas

> Nota latar belakang untuk SESI 6 (Hari 2). DAX ialah bahasa yang menukar model data kepada **KPI hidup**. Setiap measure diterangkan **baris demi baris** — anda tidak perlu jadi pengaturcara.

---

## Apa itu DAX?

**DAX (Data Analysis Expressions)** ialah bahasa formula Power BI. Ia seperti formula Excel, tetapi dengan satu perbezaan besar: DAX bekerja atas **jadual & relationships**, bukan sel individu.

Dalam Excel, `=SUM(B2:B100)` merujuk **julat sel tertentu**. Dalam DAX, `SUM ( Fakta_Projek[belanja_janm] )` merujuk **seluruh lajur** — dan hasilnya berubah automatik mengikut konteks visual (negeri mana, tahun mana).

> **Analogi KKDW:** satu measure DAX seperti **kalkulator pintar** yang tahu konteks. `Jumlah Belanja` menunjukkan jumlah keseluruhan pada kad, tetapi bila diletak dalam carta "ikut negeri", ia automatik kira **per negeri** — tanpa anda tulis formula berulang.

---

## Measure vs Calculated Column — beza penting

Ini perbezaan paling asas & paling kerap keliru:

| | **Calculated Column** | **Measure** |
|---|-----------------------|-------------|
| Dikira | Baris demi baris, **disimpan** dalam jadual | Masa nyata, **ikut konteks** visual |
| Guna memori | Ya (disimpan dalam model) | Tidak (dikira atas permintaan) |
| Bila guna | Perlu nilai **per-baris** (contoh `kategori_status`) | KPI & agregat (Jumlah Peruntukan, % Utilisasi) |
| Amalan KKDW | Guna berhemat | **Utamakan measure** untuk semua KPI |

> **Peraturan mudah:** jika anda mahu **satu nombor yang berubah ikut penapis** (jumlah, purata, peratus) → **Measure**. Jika anda mahu **nilai tetap untuk setiap baris** (kategori, bendera) → **Calculated Column** (atau lebih baik, Conditional Column dalam Power Query).

---

## Filter Context — konsep terpenting DAX

Nilai measure **berubah mengikut konteks penapis** (*filter context*) di sekelilingnya. Measure yang sama memberi jawapan berbeza dalam konteks berbeza:

```
[Jumlah Belanja] pada Card kosong        →  jumlah SEMUA projek
[Jumlah Belanja] dalam bar "ikut negeri" →  jumlah PER negeri
[Jumlah Belanja] + slicer Tahun = 2024   →  jumlah projek 2024 sahaja
```

Setiap visual, slicer dan baris matriks menetapkan konteks penapis. **Inilah kuasa DAX** — anda tulis satu measure, ia berfungsi dalam beribu konteks. Fungsi `CALCULATE` (di bawah) ialah cara kita **mengubah** konteks penapis ini dengan sengaja.

---

## Fungsi teras yang kita guna

| Fungsi | Buat apa | Contoh |
|--------|----------|--------|
| `SUM`, `AVERAGE`, `COUNTROWS`, `DISTINCTCOUNT` | Agregat asas | `SUM(Fakta_Projek[belanja_janm])` |
| `CALCULATE` | **Ubah konteks penapis** | Kira jumlah untuk status tertentu sahaja |
| `FILTER` | Tapis jadual mengikut syarat | Projek dengan varians < −10% |
| `IF` / `SWITCH` | Logik bersyarat | Tetapkan Hijau/Kuning/Merah |
| `DIVIDE` | Bahagi **selamat** (elak ralat ÷0) | `% Utilisasi` |

> **Sentiasa guna `DIVIDE(a, b)` bukan `a / b`** — jika `b` sifar (contoh peruntukan kosong), `DIVIDE` pulang kosong dengan selamat, bukan ralat yang merosakkan visual.

---

## 6 measure teras KKDW — baris demi baris

```dax
Jumlah Projek = COUNTROWS ( Fakta_Projek )
```
Kira bilangan baris (= bilangan projek) dalam konteks semasa. Ikut negeri → projek per negeri.

```dax
Jumlah Peruntukan = SUM ( Fakta_Projek[peruntukan_disemak_janm] )
```
Jumlahkan lajur peruntukan yang disemak (JANM). Ini "berapa duit diperuntukkan".

```dax
Jumlah Belanja = SUM ( Fakta_Projek[belanja_janm] )
```
Jumlahkan lajur perbelanjaan sebenar. Ini "berapa duit telah dibelanja".

```dax
Baki = [Jumlah Peruntukan] - [Jumlah Belanja]
```
Measure boleh **guna measure lain** — Baki ialah peruntukan tolak belanja. Nilai berbaki yang belum digunakan.

```dax
% Utilisasi = DIVIDE ( [Jumlah Belanja], [Jumlah Peruntukan] )
```
Peratus peruntukan yang telah dibelanja. `DIVIDE` elak ralat jika peruntukan sifar. Ini penunjuk utama kecekapan kewangan.

```dax
Projek Siap =
CALCULATE ( [Jumlah Projek], Fakta_Projek[kategori_status] = "Siap" )
```
`CALCULATE` **mengubah konteks** — kira `Jumlah Projek`, tetapi **hanya** untuk projek berstatus "Siap". Ini corak paling penting dalam DAX: *measure + syarat penapis*.

---

## Contoh SWITCH — kategori dinamik

`SWITCH ( TRUE(), ... )` menyemak beberapa syarat mengikut turutan (seperti `IF` bertingkat, tetapi lebih kemas):

```dax
Saiz Projek =
SWITCH (
    TRUE (),
    [Jumlah Peruntukan] >= 10000000, "Besar",
    [Jumlah Peruntukan] >= 1000000,  "Sederhana",
    "Kecil"
)
```

Corak `SWITCH(TRUE(), ...)` ini digunakan semula pada Hari 3 untuk **Status Risiko** (Hijau/Kuning/Merah) — lihat [`06-analitik-risiko.md`](./06-analitik-risiko.md).

---

## VAR — measure yang kemas & pantas (nota lanjutan)

Bila satu measure guna nilai yang sama beberapa kali, simpan ia dalam **VAR** (variable). Ia kira **sekali**, lebih mudah dibaca, dan lebih pantas:

```dax
% Utilisasi Selamat =
VAR Belanja    = [Jumlah Belanja]
VAR Peruntukan = [Jumlah Peruntukan]
RETURN
    DIVIDE ( Belanja, Peruntukan )
```

Corak `VAR ... RETURN` ini dipakai secara meluas pada Hari 3 (contoh `Risk Score` — lihat [`06-analitik-risiko.md`](./06-analitik-risiko.md)). Baca kod dari atas ke bawah seperti langkah — inilah cara measure kompleks kekal senang difahami.

## Amalan prestasi model (ringkas)

Model yang laju bermula dari **model yang kemas**, bukan DAX yang pintar:

- **Utamakan measure, bukan calculated column** — measure tidak menambah saiz model.
- **Jika perlu lajur baru, buat di Power Query/sumber**, bukan calculated column DAX — ia lebih kecil & boleh *fold* di sumber (lihat [`03-power-query.md`](./03-power-query.md)).
- **Buang lajur & jadual yang tidak digunakan** — setiap lajur menambah memori.
- **Nama measure & lajur yang jelas** — bukan sahaja untuk manusia, tetapi juga supaya **Copilot** beri jawapan tepat (Hari 3, [`07-copilot-ai.md`](./07-copilot-ai.md)).

---

Seterusnya: [`06-analitik-risiko.md`](./06-analitik-risiko.md) — guna DAX untuk kesan projek berisiko. Lab hands-on: [Hari 2 Latihan 6](../hari-2/snippets/lab.md#latihan-6--8-measure-teras).

## Sumber Rasmi

- **[learn.microsoft.com/dax](https://learn.microsoft.com/dax/)** — rujukan fungsi DAX.
- **[learn.microsoft.com/power-bi/transform-model/desktop-measures](https://learn.microsoft.com/power-bi/transform-model/desktop-measures)** — measures.
- **[learn.microsoft.com/dax/calculate-function-dax](https://learn.microsoft.com/dax/calculate-function-dax)** — CALCULATE.
- **[learn.microsoft.com/dax/var-dax](https://learn.microsoft.com/dax/var-dax)** — variables (VAR).
- 📘 *Architecting Power BI Solutions in Microsoft Fabric* (Packt) — Bab 9 *Performing Optimizations in Power BI* (ms 181–230): calculated column vs measure ms 210, query folding ms 206, DAX optimization ms 225.
