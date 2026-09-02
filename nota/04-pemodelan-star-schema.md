# Nota Konsep: Pemodelan Data & Star Schema

> Nota latar belakang untuk SESI 5 (Hari 1). Ini **fondasi tersembunyi** setiap dashboard yang baik. Model yang betul membuat DAX mudah & visual laju; model yang salah membuat segalanya susah.

---

## Kenapa model, bukan satu jadual besar?

Godaan pertama pemula: susun **semua** data ke **satu jadual raksasa** (JPD + BELB + MyProjek + negeri + tarikh, semua dalam satu). Ini nampak mudah, tetapi menyebabkan:

- **Pertindihan data** — nama negeri "SABAH" diulang ribuan kali.
- **Saiz besar & pengiraan perlahan** — model membengkak.
- **Sukar diselenggara** — tukar satu nama negeri, kena tukar di ribuan baris.

Penyelesaian standard industri: **Star Schema**.

> **Analogi KKDW:** bayangkan borang projek. Setiap projek ada **nombor** (kos, peruntukan, kemajuan) dan **konteks** (negeri, daerah, status, tahun). Star schema mengasingkan **nombor** (jadual Fakta) daripada **konteks** (jadual Dimensi) — supaya konteks disimpan sekali sahaja dan dikongsi.

---

## Star Schema — Fakta di tengah, Dimensi di sekeliling

```
                 ┌─────────────┐
                 │  Dim_Negeri │
                 └──────┬──────┘
   ┌─────────────┐      │      ┌─────────────┐
   │  Dim_Status │──┐   │   ┌──│  Dim_Tarikh │
   └─────────────┘  ▼   ▼   ▼  └─────────────┘
                 ┌───────────────┐
                 │  Fakta_Projek │  ← kos, peruntukan, belanja, baki, % kemajuan
                 └───────────────┘
```

Bentuknya seperti **bintang** — jadual Fakta di tengah, jadual Dimensi memancar keluar.

### Jadual Fakta vs Jadual Dimensi

| | **Jadual Fakta** | **Jadual Dimensi** |
|---|------------------|--------------------|
| Isi | Nombor yang **diukur** | Konteks untuk **menapis / mengumpul** |
| Contoh medan KKDW | `kos_projek`, `kos_keseluruhan`, `belanja_janm`, `baki_kos_de`, `peratus_sebenar_projek` | `Dim_Negeri`, `Dim_Status`, `Dim_Daerah`, `Dim_Tarikh` |
| Satu baris = | Satu projek | Satu negeri / satu status / satu tarikh |
| Saiz | Panjang (banyak baris) | Pendek (nilai unik sahaja) |

Fakta menjawab *"berapa?"*; Dimensi menjawab *"mengikut apa?"* — contoh: *"berapa `belanja_janm` (Fakta) mengikut negeri (Dimensi)?"*

---

## Relationships & Kardinaliti

**Relationship** ialah garisan yang menyambung Fakta ke Dimensi berdasarkan lajur sepunya (contoh `kod_negeri`). Ia membolehkan satu slicer negeri menapis **semua** visual serentak.

**Kardinaliti** menerangkan jenis hubungan:

| Kardinaliti | Maksud | Contoh KKDW |
|-------------|--------|-------------|
| **One-to-many** (1:*) | Satu baris dimensi → banyak baris fakta | Satu negeri → banyak projek |
| **Many-to-one** (*:1) | Banyak fakta → satu dimensi | Banyak projek → satu negeri |
| **Many-to-many** (*:*) | Elak melainkan perlu | (jarang; boleh sebabkan hasil ganjil) |

Hubungan biasa dalam model KKDW:

```
Fakta_Projek[kod_negeri]  →  Dim_Negeri[kod_negeri]    (many-to-one)
Fakta_Projek[tahun]       →  Dim_Tarikh[Tahun]         (many-to-one)
Fakta_Projek[status]      →  Dim_Status[status]        (many-to-one)
```

> **Arah penapisan:** dalam star schema, penapis mengalir dari Dimensi **ke** Fakta (satu arah). Pilih Sabah dalam `Dim_Negeri` → hanya projek Sabah dalam `Fakta_Projek` ditapis. Inilah asas kepada seluruh interaktiviti dashboard Hari 2.

---

## Date table — wajib untuk analisis masa

Buat **jadual kalendar khusus** (Date table) supaya analisis mengikut tahun/tempoh dan fungsi **Time Intelligence** DAX (Hari 2) berfungsi betul:

```dax
Dim_Tarikh =
CALENDAR ( DATE ( 2015, 1, 1 ), DATE ( 2030, 12, 31 ) )
```

Kemudian tambah lajur `Tahun`:

```dax
Tahun = YEAR ( Dim_Tarikh[Date] )
```

Akhir sekali: **Modeling → Mark as Date Table**. Sambungkan `Fakta_Projek[tahun]` ke `Dim_Tarikh[Tahun]`.

> **Kenapa Date table sendiri, bukan medan tarikh dalam Fakta?** Ia memberi **satu barisan tarikh lengkap & bersambung** (termasuk tahun tanpa projek), yang diperlukan fungsi masa DAX. Guna medan tarikh mentah sahaja menyebabkan jurang & kiraan salah.

---

## Amalan terbaik pemodelan

- **Nama jelas & konsisten** — `Fakta_Projek`, `Dim_Negeri` (bukan `Query1`, `Sheet3`).
- **Sembunyikan lajur teknikal** — klik kanan `id`, kunci → **Hide** supaya paparan kemas untuk pembina visual.
- **Satu Date table aktif** untuk seluruh model.
- **Elak many-to-many** melainkan benar-benar perlu.
- **Simpan model ringkas** — buang lajur tak digunakan (ingat Power Query, [`03-power-query.md`](./03-power-query.md)).

---

Seterusnya: [`05-dax-asas.md`](./05-dax-asas.md) — sekarang model siap, kita kira KPI dengannya. Lab hands-on: [Hari 1 Latihan 5](../hari-1/snippets/lab.md#latihan-5--bina-model-bersepadu).

## Sumber Rasmi

- **[learn.microsoft.com/power-bi/guidance/star-schema](https://learn.microsoft.com/power-bi/guidance/star-schema)** — panduan star schema.
- **[learn.microsoft.com/power-bi/transform-model/desktop-relationships-understand](https://learn.microsoft.com/power-bi/transform-model/desktop-relationships-understand)** — relationships & kardinaliti.
- **[learn.microsoft.com/power-bi/guidance/model-date-tables](https://learn.microsoft.com/power-bi/guidance/model-date-tables)** — Date table.
