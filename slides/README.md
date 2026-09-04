# Slaid Pembentangan

Dek slaid kursus *Visualisasi Data & Dashboard Pintar Berasaskan AI dengan Power BI, Fabric & Copilot* (KKDW, kod **BI-FABRIC-KKDW-101**). Tema gelap/emas Power BI, 16:9, boleh sunting dalam PowerPoint / Google Slides.

## Dek sedia (`.pptx`)

| Dek | Fail | Slaid | Kandungan |
|-----|------|-------|-----------|
| Hari 1 | [`day1-fondasi-data.pptx`](./day1-fondasi-data.pptx) | 17 | SESI 1–5 · ekosistem, **persediaan (setup)**, Fabric, Power Query, integrasi, pemodelan + **2 slaid tangkapan skrin sebenar** (Fabric setup, KKDW_Model) |
| Hari 2 | [`day2-power-bi.pptx`](./day2-power-bi.pptx) | 15 | SESI 6–10 · DAX, visual, drill-down, peta, 4 halaman, publish + **slaid kuiz recap (Kahoot, 12 soalan)** |
| Hari 3 | [`day3-analitik-ai.pptx`](./day3-analitik-ai.pptx) | 16 | SESI 11–15 · risiko, Risk Score, visual AI, Copilot, capstone + **slaid tangkapan skrin Copilot menjana laporan** + **lampiran alternatif open-source (ClickHouse · Superset · n8n)** |
| Gabungan | [`kursus-powerbi-kkdw.pptx`](./kursus-powerbi-kkdw.pptx) | 49 | ketiga-tiga hari dalam satu dek |

Setiap slaid ada **nota penceramah** (Speaker Notes) — buka View → Notes dalam PowerPoint. Nota penceramah turut memetik rujukan buku *Architecting Power BI Solutions in Microsoft Fabric* (Packt) dengan nombor muka surat bagi topik lanjutan (Direct Lake, RLS/OLS, endorsement, Copilot, clustering).

## Jana semula

Perlukan Python + `python-pptx`:

```bash
pip install python-pptx            # atau: pip install -r requirements.txt
cd slides
python build-day1.py               # → day1-fondasi-data.pptx
python build-day2.py               # → day2-power-bi.pptx
python build-day3.py               # → day3-analitik-ai.pptx
python build-combined.py           # gabung → kursus-powerbi-kkdw.pptx
```

## Struktur

- `_pbi_lib.py` — tema Power BI (gelap/emas) + helper kongsi (`title`, `bullets`, `card`, `code`, `pipeline`, `table`, …)
- `build-day{1,2,3}.py` — slaid setiap hari dikodkan sebagai data (deterministik, bukan di-*scrape*)
- `build-combined.py` — cantum 3 dek jadi satu

Ikut konvensyen kelas jiran (`~/Git/kelas-n8n-3-hari-jpj/slides/`). Untuk Google Slides: muat naik `.pptx` ke Drive → buka (auto-tukar).
