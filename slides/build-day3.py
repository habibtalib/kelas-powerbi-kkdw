#!/usr/bin/env python
"""Build the Hari 3 deck — Analitik Risiko, Copilot/AI & Capstone (SESI 11-15).

    cd slides && python build-day3.py     # writes day3-analitik-ai.pptx
"""
import _pbi_lib as L
from _pbi_lib import (ML, MR, MT, CW, SW, SH, MONO, SANS,
                      WHITE, INK, MUTED, GOLD, LGOLD, BLUE, CARD, CARDD, BRD,
                      CODEFG, GOOD, AMBER, BG0)
from pptx.dml.color import RGBColor
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

L.TOTAL = 16
RED = RGBColor(0xE8, 0x5D, 0x5D)
YEL = RGBColor(0xF2, 0xC8, 0x11)
GRN = GOOD


def cover():
    s = L.new_slide()
    L.box(s, 0, 0, 0.18, SH, fill=GOLD, radius=False)
    L.text(s, ML, 1.5, CW, 0.5, "Power BI · Microsoft Fabric · Copilot", size=15, color=LGOLD, bold=True)
    L.title(s, [[("Hari 3 — Analitik & AI", {})]], y=2.1, size=44)
    L.text(s, ML, 3.15, CW, 0.9, [[("Risiko · ", {"color": INK}), ("Copilot / AI", {"color": GOLD}), (" · Capstone", {"color": INK})]], size=26, bold=True)
    L.text(s, ML, 4.2, CW, 0.6, "Menukar data kepada insight yang menyokong keputusan pengurusan", size=16, color=MUTED)
    L.pipeline(s, ML, 5.15, CW, ["Risiko", "Risk Score", "Visual AI", "Copilot", "Capstone"])
    L.note_strip(s, "Hari ini: kesan projek lewat & keutamaan, guna Copilot untuk insight, lengkapkan capstone.", y=6.3)
    L.accent_bar(s); L.footer(s, 1)
    L.notes(s, "Pembukaan Hari 3. Naik taraf dashboard kepada intelligence.")


def recap():
    s = L.new_slide("Sambungan Hari 1-2")
    L.title(s, [[("Kita ada ", {}), ("dashboard berfungsi", {"color": GOLD})]])
    L.bullets(s, ML, 2.1, CW, 2.0, [
        [("hari-2.pbix", {"font": MONO, "color": CODEFG, "bold": True}), (" — model bersepadu + 4 halaman + measures", {})],
        "Diterbit ke Power BI Service, interaktif dengan drill-down & peta",
    ], size=15, gap=9)
    L.box(s, ML, 4.0, CW, 1.5, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 4.25, CW-0.6, 1.0, [[("Hari ini: ", {"color": GOLD, "bold": True}),
           ("bina measure risiko → halaman AI Risk & Early Warning → visual AI terbina → Copilot → capstone yang menjawab soalan pengurusan utama.", {"color": INK})]],
           size=15, line_spacing=1.2)
    L.accent_bar(s); L.footer(s, 2)
    L.notes(s, "Kaitkan dengan capstone: projek/kawasan mana perlu keutamaan, dan mengapa.")


def varians():
    s = L.new_slide("SESI 11 · Early Warning")
    L.title(s, [[("Kesan projek lewat ", {}), ("lebih awal", {"color": GOLD})]])
    L.bullets(s, ML, 2.05, CW, 1.5, [
        [("peratus_jadual_projek", {"font": MONO, "color": CODEFG}), (" — sepatutnya sudah siap sebanyak ini", {})],
        [("peratus_sebenar_projek", {"font": MONO, "color": CODEFG}), (" — kemajuan fizikal betul", {})],
    ], size=15, gap=8)
    L.code(s, ML, 3.5, CW, 1.0, ['Varians = % Sebenar − % Jadual     (negatif = lewat)'], size=14)
    L.box(s, ML, 4.85, CW, 0.9, fill=CARD, line=BRD)
    L.text(s, ML+0.3, 5.1, CW-0.6, 0.5, [[("Bila ", {"color": INK}), ("sebenar < jadual", {"color": RED, "bold": True}),
           (", projek ketinggalan. Ukuran itu = varians.", {"color": INK})]], size=15)
    L.accent_bar(s); L.footer(s, 3)
    L.notes(s, "Dua medan MyProjek ialah asas seluruh analitik risiko. Varians negatif = lewat.")


def rag_indikator():
    s = L.new_slide("SESI 11 · Indikator Risiko")
    L.title(s, [[("Hijau · Kuning · ", {}), ("Merah", {"color": RED})]])
    chips = [("🟢 Hijau", "0 hingga −5%", "Normal / atas jadual", GRN),
             ("🟡 Kuning", "−5% hingga −10%", "Perlu perhatian", YEL),
             ("🔴 Merah", "melebihi −10%", "Berisiko / lewat", RED)]
    w = (CW - 2*0.3)/3
    for i, (hd, rng, desc, col) in enumerate(chips):
        x = ML + i*(w+0.3)
        L.box(s, x, 2.1, w, 1.6, fill=CARD, line=col, line_w=1.5)
        L.box(s, x, 2.1, w, 0.12, fill=col, radius=False)
        L.text(s, x+0.2, 2.35, w-0.4, 0.4, hd, size=17, color=WHITE, bold=True)
        L.text(s, x+0.2, 2.85, w-0.4, 0.4, rng, size=14, color=col, bold=True, font=MONO)
        L.text(s, x+0.2, 3.25, w-0.4, 0.4, desc, size=12.5, color=MUTED)
    L.code(s, ML, 3.95, CW, 1.75, [
        'Status Risiko =',
        'SWITCH ( TRUE (),',
        '   [Varians Kemajuan] >= -5, "Hijau",   -- skala 0-100',
        '   [Varians Kemajuan] >= -10, "Kuning",',
        '   "Merah" )',
    ], size=12.5)
    L.accent_bar(s); L.footer(s, 4)
    L.notes(s, "SWITCH(TRUE()) ialah corak DAX untuk julat berperingkat. Guna Conditional Formatting untuk warnakan matriks.")


def fizikal_kewangan():
    s = L.new_slide("SESI 12 · Fizikal vs Kewangan")
    L.title(s, [[("Kesan ", {}), ("ketidakpadanan", {"color": GOLD})]])
    data = [("⚖️", "Normal", "Fizikal & kewangan bergerak seimbang", False),
            ("🔴", "Risiko kewangan", "Belanja 80% tetapi fizikal 50% → perlu semakan", True),
            ("🐢", "Under-utilisation", "Fizikal baik tetapi belanja masih rendah", False)]
    w = (CW - 2*0.35)/3
    for i, (ico, hd, bd, dyn) in enumerate(data):
        L.card(s, ML + i*(w+0.35), 2.2, w, 2.3, ico, hd, bd, dyn=dyn)
    L.note_strip(s, "Scatter: % Utilisasi (x) vs % Sebenar (y) — titik jauh dari pepenjuru = ketidakpadanan yang perlu disemak.", y=5.3)
    L.accent_bar(s); L.footer(s, 5)
    L.notes(s, "Contoh klasik: 80% belanja, 50% siap → tanda merah. Scatter plot paling jelas tunjuk ini.")


def risk_score():
    s = L.new_slide("SESI 12 · Risk Score & Kecekapan")
    L.title(s, [[("Susun projek ikut ", {}), ("skor risiko", {"color": GOLD})]])
    L.code(s, ML, 2.05, CW, 1.75, [
        'Risk Score =',
        'VAR VarLewat   = SWITCH ( TRUE (), [Varians] < -10, 2, [Varians] < -5, 1, 0 )',
        'VAR VarBelanja = IF ( [% Utilisasi] * 100 > [% Sebenar] + 20, 2, 0 )',
        'RETURN VarLewat + VarBelanja',
    ], size=12.5)
    L.code(s, ML, 4.0, (CW-0.4)/2, 1.15, [
        'Kos per KM =',
        'DIVIDE ( SUM(JPD[kos_projek]),',
        '         SUM(JPD[panjang_jalan]) )',
    ], size=12, title_txt="JPD")
    L.code(s, ML+(CW-0.4)/2+0.4, 4.0, (CW-0.4)/2, 1.15, [
        'Kos per Sambungan =',
        'DIVIDE ( SUM(BELB[kos_projek]),',
        '         SUM(BELB[jumlah_projek_peserta]) )',
    ], size=12, title_txt="BELB")
    L.note_strip(s, "Benchmark ~RM9-11 juta/km hanya indikatif — ambil kira geografi, skop & keadaan tapak sebelum simpul.", y=5.5)
    L.accent_bar(s); L.footer(s, 6)
    L.notes(s, "Risk Score gabung faktor jadi satu nombor boleh disusun. Priority Index tambah keperluan (penerima manfaat).")


def visual_ai():
    s = L.new_slide("SESI 13 · Visual AI Terbina")
    L.title(s, [[("Analitik AI ", {}), ("tanpa lesen Copilot", {"color": GOLD})]])
    data = [("🔑", "Key Influencers", "Apa paling pengaruhi status \"Merah\"?"),
            ("🌳", "Decomposition Tree", "Pecah belanja: negeri → daerah → status"),
            ("📝", "Smart Narrative", "Ringkasan teks automatik"),
            ("📈", "Anomaly Detection", "Kesan lonjakan belanja luar norma"),
            ("🔍", "Analyze", "\"Explain increase/decrease\" — kenapa berubah"),
            ("💡", "Quick Insights", "AI imbas model, cari corak automatik")]
    w = (CW - 2*0.3)/3
    for i, (ico, hd, bd) in enumerate(data):
        L.card(s, ML + (i % 3)*(w+0.3), 2.15 + (i//3)*1.7, w, 1.5, ico, hd, bd, body_size=10.5)
    L.note_strip(s, "Semua percuma & terbina (tiada F64) — tidak berbual bahasa biasa. Tambahan: \"Automatically find clusters\" kumpul projek serupa. Copilot (SESI 14) ialah lapisan sembang di atasnya.", y=5.65)
    L.accent_bar(s); L.footer(s, 7)
    L.notes(s, "Penting: peserta tanpa lesen Copilot masih boleh dapat insight AI melalui visual terbina ini. "
               "Analyze & Quick Insights = penerangan/corak automatik; clustering kumpul projek serupa untuk segmen keutamaan. "
               "📘 Buku Bab 12 (Quick Insights ms 272, Analyze ms 273, Decomposition Tree ms 275), Bab 14 (clustering ms 323).")


def copilot():
    s = L.new_slide("SESI 14 · Copilot")
    L.title(s, [[("Copilot — ", {}), ("pegawai analisis maya", {"color": GOLD})]])
    L.bullets(s, ML, 2.05, CW, 2.0, [
        [("Tanya data ", {}), ("bahasa biasa", {"bold": True, "color": INK}), (" (NL Q&A) — tanpa tulis DAX", {})],
        [("Jana ", {}), ("halaman laporan", {"bold": True, "color": INK}), (" automatik daripada arahan", {})],
        [("Ringkas ", {}), ("naratif", {"bold": True, "color": INK}), (" & terangkan insight visual", {})],
        [("Cadang / tulis ", {}), ("measure DAX", {"bold": True, "color": INK}), (" daripada bahasa biasa", {})],
    ], size=15, gap=8)
    L.box(s, ML, 4.55, CW, 1.0, fill=CARDD, line=AMBER, line_w=1.25)
    L.text(s, ML+0.3, 4.77, CW-0.6, 0.6, [[("Lesen: ", {"color": AMBER, "bold": True}),
           ("Copilot perlukan Fabric F64+ / Premium. Sahkan dengan IT KKDW. Jika tiada — guna Q&A visual (percuma).", {"color": INK})]],
           size=13.5, line_spacing=1.15)
    L.note_strip(s, "Dua peranan: pengguna biasa (tanya & ringkas) vs teknikal (auto-jana laporan, tulis DAX). Copilot menghormati RLS/OLS — jawapan terhad kepada data yang dibenarkan.", y=5.8)
    L.accent_bar(s); L.footer(s, 8)
    L.notes(s, "Copilot mempercepat tetapi perlu lesen. Q&A visual ialah alternatif percuma yang serupa. "
               "Pengguna biasa guna Copilot untuk tanya/ringkas; pengguna teknikal untuk auto-jana laporan & tulis DAX. "
               "📘 Buku Bab 12: Copilot pengguna biasa ms 278, teknikal ms 282.")


def pertanyaan():
    s = L.new_slide("SESI 14 · Contoh Pertanyaan")
    L.title(s, [[("Tanya gaya ", {}), ("pengurusan KKDW", {"color": GOLD})]])
    qs = [
        "\"Senaraikan 10 projek JPD dengan jurang terbesar antara jadual dan sebenar.\"",
        "\"Negeri mana perbelanjaan BELB tertinggi tetapi kemajuan paling rendah?\"",
        "\"Ringkaskan prestasi projek BELB untuk Sabah.\"",
        "\"Apakah tiga isu utama portfolio JPD pada tempoh semasa?\"",
        "\"Cari projek kemajuan fizikal < 50% tetapi guna > 70% peruntukan.\"",
    ]
    y = 2.15
    for i, q in enumerate(qs):
        yy = y + i*0.72
        L.box(s, ML, yy, CW, 0.6, fill=CARD, line=BRD, line_w=1)
        L.text(s, ML+0.25, yy+0.13, CW-0.5, 0.4, q, size=13.5, color=INK, italic=True)
    L.note_strip(s, "Untuk setiap jawapan — semak terhadap data sumber. AI membantu, anda memandu.", y=5.95)
    L.accent_bar(s); L.footer(s, 9)
    L.notes(s, "Pertanyaan diambil terus dari cadangan use-case KKDW. Sentiasa sahkan jawapan.")


def batasan():
    s = L.new_slide("SESI 14 · Batasan AI")
    L.title(s, [[("AI membantu, ", {}), ("anda memandu", {"color": GOLD})]])
    L.box(s, ML, 2.2, CW, 1.4, fill=CARDD, line=AMBER, line_w=1.5)
    L.text(s, ML+0.3, 2.45, CW-0.6, 1.0, [[("Copilot boleh salah atau terlepas konteks. ", {"color": INK}),
           ("Sentiasa semak", {"color": AMBER, "bold": True}),
           (" insight terhadap data sumber sebelum dibawa ke keputusan pengurusan.", {"color": INK})]],
           size=16, line_spacing=1.25)
    L.bullets(s, ML, 4.0, CW, 1.6, [
        "Jangan kongsi data sensitif ke perkhidmatan AI luar kawalan tanpa kelulusan",
        "Sahkan angka penting secara manual (matriks / measure)",
        "Gunakan AI untuk mempercepat, bukan menggantikan pertimbangan pegawai",
    ], size=14.5, gap=8)
    L.accent_bar(s); L.footer(s, 10)
    L.notes(s, "Tekankan tadbir urus & residensi data untuk KKDW. AI sebagai pembantu, bukan pembuat keputusan.")


def capstone():
    s = L.new_slide("Capstone")
    L.title(s, [[("Soalan ", {}), ("pengurusan utama", {"color": GOLD})]])
    L.box(s, ML, 2.1, CW, 1.5, fill=CARDD, line=GOLD, line_w=1.5)
    L.text(s, ML+0.35, 2.35, CW-0.7, 1.1, [[("\"Daripada keseluruhan portfolio JPD dan BELB, projek dan kawasan manakah yang perlu diberi keutamaan oleh pengurusan KKDW, dan mengapa?\"", {"color": WHITE})]],
           size=18, bold=True, italic=True, line_spacing=1.2)
    L.text(s, ML, 3.95, CW, 0.4, "Deliverable: capstone.pbix", size=14, color=LGOLD, bold=True, font=MONO)
    L.bullets(s, ML, 4.4, CW, 1.3, [
        "Dashboard 5 halaman + measures risiko + Priority Index",
        "Ringkasan eksekutif (Smart Narrative / Copilot)",
        "3–5 cadangan keutamaan berpaksikan data + pembentangan",
    ], size=14, gap=6)
    L.accent_bar(s); L.footer(s, 11)
    L.notes(s, "Capstone mengaplikasikan keseluruhan proses. Bukti mesti pada skrin (varians, ketidakpadanan, penerima manfaat).")


def penilaian():
    s = L.new_slide("Penilaian")
    L.title(s, [[("Kriteria ", {}), ("capstone", {"color": GOLD})]])
    L.table(s, ML, 2.2, CW, [
        ("Penyediaan & pemodelan data", "20%"),
        ("KPI & measures (DAX)", "20%"),
        ("Reka bentuk dashboard & interaktiviti", "20%"),
        ("Analitik risiko & penggunaan Copilot/AI", "20%"),
        ("Pembentangan & cadangan pengurusan", "20%"),
    ], col_w=[0.78, 0.22], header=["Kriteria", "Wajaran"], row_h=0.62, size=15)
    L.note_strip(s, "Lengkap semua → Sijil Penyertaan: Visualisasi Data & Dashboard Pintar dengan Power BI, Fabric & Copilot.", y=5.95)
    L.accent_bar(s); L.footer(s, 12)
    L.notes(s, "Lima kriteria seimbang. Pembentangan 5 minit setiap kumpulan.")


def rumusan():
    s = L.new_slide("Rumusan Kursus")
    L.title(s, [[("Rantaian kerja data ", {}), ("lengkap", {"color": GOLD})]])
    L.pipeline(s, ML, 2.1, CW, ["Data", "Fabric", "Power BI", "Analitik", "Copilot"])
    L.bullets(s, ML, 3.0, CW, 2.0, [
        [("Sedia & model data ", {}), ("(Fabric / Power Query)", {"bold": True, "color": INK})],
        [("Bina dashboard ", {}), ("(Power BI / DAX)", {"bold": True, "color": INK})],
        [("Analitik risiko ", {}), ("(varians, Risk Score, Priority)", {"bold": True, "color": INK})],
        [("Insight AI ", {}), ("(Copilot / visual AI)", {"bold": True, "color": INK})],
    ], size=14.5, marker="✅  ", gap=7)
    L.box(s, ML, 5.2, CW, 0.9, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 5.42, CW-0.6, 0.5, "Anda kini boleh menukar data projek luar bandar KKDW kepada insight yang menyokong keputusan.",
           size=14.5, color=INK)
    L.accent_bar(s); L.footer(s, 13)
    L.notes(s, "Tutup dengan pencapaian penuh 3 hari. Langkah seterusnya: sumber data sebenar, RLS, kembangkan Priority Index.")


def shots_copilot():
    s = L.new_slide("Lampiran · Tangkapan Skrin Sebenar")
    L.title(s, [[("Copilot ", {"color": GOLD}), ("menjana laporan (sebenar)", {})]], y=1.02, size=27)
    L.picture(s, "fabric-guide/12-copilot-report.jpg", 0.78, 1.85, 5.6)
    L.picture(s, "fabric-guide/13-executive-report.jpg", 6.98, 1.85, 5.6)
    L.text(s, 0.78, 5.28, 5.6, 0.4, "Copilot: satu arahan bahasa biasa → halaman laporan", size=12, color=MUTED)
    L.text(s, 6.98, 5.28, 5.6, 0.4, "Executive Projek Overview atas KKDW_Model", size=12, color=MUTED)
    L.note_strip(s, "Copilot menjana keseluruhan halaman dari satu arahan — atas model DirectLake KKDW_Model, dalam pelayar (tanpa Desktop).", y=5.85)
    L.accent_bar(s); L.footer(s, 14)
    L.notes(s, "Tangkapan skrin sebenar: Copilot dalam Power BI menjana laporan Executive dari arahan bahasa biasa (SESI 14). Copilot aktif dalam tenant ini.")


def alternatif():
    s = L.new_slide("Lampiran · Alternatif Open-Source")
    L.title(s, [[("Alternatif ", {}), ("sumber terbuka", {"color": GOLD}), (" (self-hosted)", {})]], y=1.02, size=27)
    L.text(s, ML, 1.9, CW, 0.5,
           "Bukan stack kursus — rujukan bila kedaulatan data on-prem, elak lesen/kapasiti, atau kawalan infra jadi keutamaan.",
           size=12.5, color=MUTED)
    L.table(s, ML, 2.45, CW, [
        ("OneLake / Lakehouse / Warehouse", "ClickHouse · DuckDB · Postgres + MinIO"),
        ("Transform (Dataflow Gen2 / Power Query)", "dbt · Airbyte · Airflow · n8n"),
        ("Visualisasi (Power BI)", "Apache Superset · Metabase · Grafana"),
        ("Copilot / NL Q&A / jana DAX", "LLM + text-to-SQL (Vanna) · n8n AI Agent"),
        ("Power Automate / Data Alerts", "n8n — amaran email/Teams/WhatsApp"),
        ("Microsoft Entra (identiti / SSO)", "Keycloak"),
    ], col_w=[0.5, 0.5], header=["Lapisan Fabric", "Alternatif open-source (on-prem / VM)"], row_h=0.48, size=12)
    L.box(s, ML, 5.95, CW, 0.95, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 6.12, CW-0.6, 0.65, [[("Gabungan popular: ", {"color": GOLD, "bold": True}),
           ("ClickHouse + Superset (+ n8n untuk ingest/automasi). Konsep — Lakehouse, star schema, SQL/DAX, dashboard — boleh dipindah. Kekal Fabric + Power BI melainkan kedaulatan data / lesen jadi keutamaan.", {"color": INK})]],
           size=11.5, line_spacing=1.1)
    L.accent_bar(s); L.footer(s, 15)
    L.notes(s, "Rujukan sahaja (nota/09-alternatif-open-source.md) — kursus kekal pada Fabric + Power BI + Copilot. "
               "Alasan pertimbang alternatif: tiada lesen per-pengguna, data kekal on-prem (kedaulatan), tiada throttling kapasiti, kos perisian percuma. "
               "ClickHouse = pangkalan data OLAP columnar (peranan Warehouse/Direct Lake). Superset = paling hampir Power BI Service. "
               "n8n = automasi/orkestrasi (ganti Power Automate + Data Alerts) + AI Agent (sebahagian Copilot). "
               "Batasan: urus infra sendiri, tiada Copilot setara siap-pakai, perlu kemahiran SQL/DevOps. "
               "Rumusan: Fabric + Power BI kekal disyorkan untuk kursus & majoriti kes KKDW; pertimbang ClickHouse + Superset hanya bila on-prem/lesen/kawalan infra jadi keutamaan.")


def penutup():
    s = L.new_slide()
    L.box(s, 0, 0, 0.18, SH, fill=GOLD, radius=False)
    L.text(s, ML, 2.6, CW, 1.0, [[("Tahniah!", {"color": WHITE})]], size=46, bold=True)
    L.text(s, ML, 3.8, CW, 0.6, "Kursus 3 hari selesai — daripada data mentah kepada dashboard pintar KKDW.", size=17, color=MUTED)
    L.text(s, ML, 4.8, CW, 0.5, "hari-3/README.md · hari-3/snippets/lab.md · capstone.pbix", size=14, color=LGOLD, font=MONO)
    L.accent_bar(s); L.footer(s, 16)
    L.notes(s, "Penutup kursus + penyampaian sijil.")


for fn in [cover, recap, varians, rag_indikator, fizikal_kewangan, risk_score,
           visual_ai, copilot, pertanyaan, batasan, capstone, penilaian, rumusan,
           shots_copilot, alternatif, penutup]:
    fn()

L.prs.save("day3-analitik-ai.pptx")
print(f"Wrote day3-analitik-ai.pptx ({len(L.prs.slides._sldIdLst)} slides)")
