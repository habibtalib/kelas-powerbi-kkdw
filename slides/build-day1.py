#!/usr/bin/env python
"""Build the Hari 1 deck — Fondasi Data: Fabric, Power Query & Pemodelan (SESI 1-5).

    cd slides && python build-day1.py     # writes day1-fondasi-data.pptx
"""
import _pbi_lib as L
from _pbi_lib import (ML, MR, MT, CW, SW, SH, MONO, SANS,
                      WHITE, INK, MUTED, GOLD, LGOLD, BLUE, CARD, CARDD, BRD,
                      CODEFG, GOOD, AMBER, BG0)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

L.TOTAL = 17


def cover():
    s = L.new_slide()
    L.box(s, 0, 0, 0.18, SH, fill=GOLD, radius=False)
    L.text(s, ML, 1.5, CW, 0.5, "Power BI · Microsoft Fabric · Copilot", size=15, color=LGOLD, bold=True)
    L.title(s, [[("Hari 1 — Fondasi Data", {})]], y=2.1, size=46)
    L.text(s, ML, 3.15, CW, 0.9, [[("Microsoft Fabric · Power Query · ", {"color": INK}),
           ("Pemodelan Data", {"color": GOLD})]], size=26, bold=True)
    L.text(s, ML, 4.2, CW, 0.6, [[("Tema use-case: ", {"color": LGOLD, "bold": True}),
           ("Pemantauan Prestasi Program JPD & BELB Bersepadu dengan MyProjek", {"color": MUTED})]], size=15)
    L.pipeline(s, ML, 5.15, CW, ["Data", "Fabric", "Power BI", "Analitik", "Copilot"])
    L.note_strip(s, "Hari ini: bina satu model data bersepadu yang bersih & sedia untuk analisis. Belum visual — itu Hari 2.", y=6.3)
    L.accent_bar(s); L.footer(s, 1)
    L.notes(s, "Pembukaan Hari 1. Tekankan: dashboard yang baik bermula dengan data yang betul. Aliran kerja 5 peringkat.")


def aliran():
    s = L.new_slide("Aliran Kerja Kursus")
    L.title(s, [[("Lima peringkat, ", {}), ("satu matlamat", {"color": GOLD})]])
    steps = [("1", "Data", "Kumpul JPD, BELB & MyProjek"),
             ("2", "Fabric", "Sedia, transform, integrasi & model"),
             ("3", "Power BI", "KPI, visual, drill-down, peta"),
             ("4", "Analitik", "Risk Score, Fizikal vs Kewangan"),
             ("5", "Copilot", "Tanya data, ringkasan eksekutif")]
    y = 2.15; h = 0.82
    for i, (n, hd, bd) in enumerate(steps):
        yy = y + i*(h+0.14)
        L.numbered(s, ML, yy+0.16, n, color=(GOLD if i < 2 else BLUE))
        L.box(s, ML+0.7, yy, CW-0.7, h, fill=(CARDD if i < 2 else CARD), line=(GOLD if i < 2 else BRD), line_w=1)
        L.text(s, ML+0.95, yy+0.13, 3.0, 0.5, hd, size=17, color=WHITE, bold=True)
        L.text(s, ML+3.6, yy+0.16, CW-4.2, 0.5, bd, size=13.5, color=MUTED)
    L.text(s, ML+0.7, y+0.02, 3, 0.3, "◄ Fokus Hari 1", size=11, color=GOLD, bold=True, align=PP_ALIGN.RIGHT)
    L.accent_bar(s); L.footer(s, 2)
    L.notes(s, "Peringkat 1-2 (Data + Fabric) ialah fokus hari ini. 3-5 datang Hari 2 & 3.")


def konteks():
    s = L.new_slide("Konteks KKDW")
    L.title(s, [[("Use-case sebenar ", {}), ("pembangunan luar bandar", {"color": GOLD})]])
    L.text(s, ML, 1.78, CW, 0.5, [[("Tema: ", {"color": LGOLD, "bold": True}),
           ("Dashboard Pintar Pemantauan Prestasi Program JPD & BELB Bersepadu dengan MyProjek", {"color": INK})]], size=13.5)
    data = [("🛣️", "JPD — 1,376 projek", "Jalan Perhubungan Desa · kos, panjang jalan, negeri, status, koordinat"),
            ("💡", "BELB — 23 projek", "Bekalan Elektrik Luar Bandar · kampung, peserta, kos, status"),
            ("📋", "MyProjek — 77 projek", "Pemantauan RMK · % jadual vs sebenar, peruntukan, belanja, baki, KPI")]
    w = (CW - 2*0.35)/3
    for i, (ico, hd, bd) in enumerate(data):
        L.card(s, ML + i*(w+0.35), 2.45, w, 2.35, ico, hd, bd, dyn=(i == 2))
    L.box(s, ML, 5.12, CW, 0.95, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 5.3, CW-0.6, 0.7, [[("Soalan pengurusan utama: ", {"color": GOLD, "bold": True}),
           ("projek & kawasan JPD/BELB manakah perlu diberi keutamaan oleh KKDW — dan mengapa?", {"color": INK})]],
           size=14, line_spacing=1.12)
    L.accent_bar(s); L.footer(s, 3)
    L.notes(s, "Berdasarkan Cadangan Use Case KKDW. Tema: dashboard bersepadu JPD+BELB dengan MyProjek. "
               "MyProjek paling kaya (kewangan + kemajuan) — tulang belakang analitik risiko Hari 3. "
               "Soalan pengurusan utama ini ialah capstone kursus (Hari 3).")


def kenapa():
    s = L.new_slide("Kenapa Visualisasi")
    L.title(s, [[("Dari ", {}), ("1,476 baris", {"color": GOLD}), (" kepada jawapan", {})]])
    L.text(s, ML, 2.05, CW, 0.5, "Dalam Excel mentah, pengurusan tak nampak dengan pantas:", size=15, color=MUTED)
    L.bullets(s, ML, 2.7, CW, 2.2, [
        [("Projek mana ", {}), ("lewat atau berisiko", {"bold": True, "color": INK}), ("?", {})],
        [("Negeri/kawasan mana perlu diberi ", {}), ("keutamaan", {"bold": True, "color": INK}), ("?", {})],
        [("Di mana ", {}), ("peruntukan tinggi tetapi kemajuan fizikal rendah", {"bold": True, "color": INK}), ("?", {})],
    ], size=17, gap=10)
    L.box(s, ML, 4.7, CW, 1.0, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 4.95, CW-0.6, 0.6, [[("Dashboard menjawab dalam ", {"color": INK}),
           ("beberapa saat", {"color": GOLD, "bold": True}),
           (" — bukan berjam-jam menapis Excel.", {"color": INK})]], size=16)
    L.accent_bar(s); L.footer(s, 4)
    L.notes(s, "Bengkel SESI 1: peserta senaraikan soalan pengurusan sebenar. Ini jadi panduan reka dashboard Hari 2.")


def ekosistem():
    s = L.new_slide("Ekosistem")
    L.title(s, [[("Tiga alat, ", {}), ("tiga peranan", {"color": GOLD})]])
    data = [("🗄️", "Microsoft Fabric", "Platform data bersepadu — simpan, sedia, transform & model data"),
            ("📊", "Power BI", "Bina visual, dashboard & laporan interaktif di atas data"),
            ("🤖", "Copilot / AI", "Pembantu pintar — tanya data bahasa biasa, jana insight")]
    w = (CW - 2*0.35)/3
    for i, (ico, hd, bd) in enumerate(data):
        L.card(s, ML + i*(w+0.35), 2.2, w, 2.3, ico, hd, bd)
    L.box(s, ML, 5.0, CW, 1.0, fill=CARD, line=BRD)
    L.text(s, ML+0.3, 5.18, CW-0.6, 0.7, [[("Analogi: ", {"color": GOLD, "bold": True}),
           ("Fabric = gudang & bilik sedia data · Power BI = bilik pameran · Copilot = pegawai analisis maya.", {"color": INK})]],
           size=14.5, line_spacing=1.15)
    L.accent_bar(s); L.footer(s, 5)
    L.notes(s, "Power BI kini sebahagian daripada Fabric. Copilot memerlukan lesen (F64+) — sahkan dengan IT.")


def persediaan():
    s = L.new_slide("Persediaan")
    L.title(s, [[("Mula di sini ", {}), ("— sediakan alat", {"color": GOLD})]])
    L.box(s, ML, 2.15, (CW-0.4)/2, 2.7, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 2.4, (CW-0.4)/2-0.6, 0.5, "Laluan A · Fabric pelayar — WAJIB", size=15, color=GOLD, bold=True)
    L.bullets(s, ML+0.3, 3.0, (CW-0.4)/2-0.6, 1.8, [
        "Semua peserta · mana-mana OS (macOS)",
        [("Fabric + Copilot ", {"bold": True, "color": INK}), ("— hanya di sini", {})],
        [("app.fabric.microsoft.com", {"font": MONO, "color": CODEFG}), (" → log masuk", {})],
        "Boleh laksana keseluruhan Hari 1–3",
    ], size=13, gap=6)
    x2 = ML + (CW-0.4)/2 + 0.4
    L.box(s, x2, 2.15, (CW-0.4)/2, 2.7, fill=CARD, line=BRD)
    L.text(s, x2+0.3, 2.4, (CW-0.4)/2-0.6, 0.5, "Laluan B · Desktop — PILIHAN", size=15, color=INK, bold=True)
    L.bullets(s, x2+0.3, 3.0, (CW-0.4)/2-0.6, 1.8, [
        "Windows sahaja · pilihan tambahan",
        "Authoring laporan/DAX (Hari 2–3)",
        [("Tak boleh ", {}), ("Fabric/Lakehouse/Copilot", {"bold": True, "color": INK})],
        "macOS → guna Power BI Service",
    ], size=13, gap=6)
    L.box(s, ML, 4.98, CW, 0.72, fill=CARDD, line=BLUE, line_w=1.25)
    L.text(s, ML+0.3, 5.13, CW-0.6, 0.5, [[("Lesen: ", {"color": BLUE, "bold": True}),
           ("Fabric penuh + Copilot perlu kapasiti F2+ berbayar (trial tiada Copilot). Sahkan dengan IT KKDW.", {"color": INK})]],
           size=13, line_spacing=1.12)
    L.note_strip(s, "Hari 1 (data + model) boleh 100% pelayar (Fabric) — tiada Desktop perlu. Desktop (Windows) untuk Hari 2–3.", y=5.9)
    L.accent_bar(s); L.footer(s, 6)
    L.notes(s, "Sediakan alat dahulu. macOS → guna Fabric pelayar (Laluan A). Windows → boleh Desktop. "
               "Sahkan lesen Fabric/Copilot (F2+) dengan IT sebelum kelas. Panduan admin penuh: slides/fabric-guide (Bahagian A).")


def fabric():
    s = L.new_slide("SESI 2 · Microsoft Fabric")
    L.title(s, [[("Istilah Fabric ", {}), ("yang perlu tahu", {"color": GOLD})]])
    rows = [
        ("OneLake", "\"OneDrive untuk data\" — satu tasik data untuk seluruh KKDW"),
        ("Workspace", "Ruang kerja berkumpulan — simpan & kongsi item"),
        ("Lakehouse", "Fail mentah + jadual berstruktur dalam satu tempat"),
        ("Dataflows Gen2", "Power Query di awan — transformasi boleh dijadual"),
        ("Semantic Model", "Model data (jadual + relationships + measures)"),
    ]
    y = 2.15
    for i, (k, v) in enumerate(rows):
        yy = y + i*0.72
        L.box(s, ML, yy, 3.0, 0.58, fill=CARD, line=BRD, line_w=1)
        L.text(s, ML+0.2, yy+0.13, 2.7, 0.4, k, size=15, color=LGOLD, bold=True, font=MONO)
        L.text(s, ML+3.3, yy+0.13, CW-3.3, 0.5, v, size=14, color=INK)
    L.note_strip(s, "Lesen: ciri penuh Fabric perlukan F64+. Lakehouse (no-code, pemula) vs Warehouse (mahir T-SQL) — kursus guna Lakehouse. Boleh 100% Power BI Desktop jika perlu.", y=6.0)
    L.accent_bar(s); L.footer(s, 7)
    L.notes(s, "Jangan tenggelam dalam istilah — tekankan OneLake (satu tempat) & Lakehouse (fail+jadual). "
               "Lakehouse & Warehouse serupa; beza: Warehouse T-SQL baca+tulis, Lakehouse SQL baca-sahaja + Spark — pemula guna Lakehouse. "
               "Sahkan lesen dengan IT KKDW. 📘 Buku Bab 7 (Lakehouse ms 136, Warehouse ms 141).")


def import_dq():
    s = L.new_slide("Mode Sambungan Data")
    L.title(s, [[("Import, DirectQuery ", {}), ("& Direct Lake", {"color": GOLD})]])
    L.box(s, ML, 2.15, (CW-0.4)/2, 2.7, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 2.4, (CW-0.4)/2-0.6, 0.5, "Import  ✓ pilihan kita", size=18, color=GOLD, bold=True)
    L.bullets(s, ML+0.3, 3.05, (CW-0.4)/2-0.6, 1.7, [
        "Data disimpan dalam .pbix (dalam memori)",
        "Sangat pantas",
        "Sesuai data kecil–sederhana",
        [("Data KKDW kecil → ", {}), ("guna Import", {"bold": True, "color": INK})],
    ], size=13.5, gap=6)
    x2 = ML + (CW-0.4)/2 + 0.4
    L.box(s, x2, 2.15, (CW-0.4)/2, 2.7, fill=CARD, line=BRD)
    L.text(s, x2+0.3, 2.4, (CW-0.4)/2-0.6, 0.5, "DirectQuery", size=18, color=INK, bold=True)
    L.bullets(s, x2+0.3, 3.05, (CW-0.4)/2-0.6, 1.7, [
        "Data kekal di sumber; ditanya masa nyata",
        "Kelajuan bergantung sumber",
        "Sesuai data sangat besar / langsung",
        "Untuk kemudian, bukan kursus ini",
    ], size=13.5, gap=6)
    # third mode — Direct Lake (Fabric only)
    L.box(s, ML, 4.98, CW, 0.72, fill=CARDD, line=BLUE, line_w=1.25)
    L.text(s, ML+0.3, 5.13, CW-0.6, 0.5, [[("Mode ketiga (Fabric): ", {"color": BLUE, "bold": True}),
           ("Direct Lake", {"color": WHITE, "bold": True}),
           (" — kelajuan Import tanpa perlu refresh; hanya bila data di Lakehouse/Warehouse. Tidak diguna dalam kursus ini.", {"color": INK})]],
           size=13, line_spacing=1.12)
    L.note_strip(s, "Get Data → Excel → Transform Data (bukan Load terus) — kita bersihkan dulu di SESI 3.", y=5.9)
    L.accent_bar(s); L.footer(s, 8)
    L.notes(s, "Import kerana dataset kecil. Selalu klik Transform Data, bukan Load, supaya masuk Power Query. "
               "Direct Lake ialah mode khas Fabric (data di Lakehouse/Warehouse): laju macam Import tetapi sentiasa terkini, tiada jadual refresh — "
               "bukan skop kursus, tapi arah tuju bila KKDW naik taraf. 📘 Buku Bab 7, Direct Lake ms 146–148.")


def power_query():
    s = L.new_slide("SESI 3 · Power Query")
    L.title(s, [[("Bersihkan data ", {}), ("sebelum guna", {"color": GOLD})]])
    L.bullets(s, ML, 2.05, 6.0, 3.2, [
        [("Applied Steps", {"bold": True, "color": INK}), (" — setiap langkah direkod, boleh diulang", {})],
        [("Jenis data", {"bold": True, "color": INK}), (" — kos_projek → Decimal, tahun → Whole", {})],
        [("Kendali null", {"bold": True, "color": INK}), (" & buang lajur teknikal", {})],
        [("Standardkan", {"bold": True, "color": INK}), (" negeri, daerah, status (UPPERCASE + Trim)", {})],
        [("Conditional Column", {"bold": True, "color": INK}), (" — kategori status ringkas", {})],
    ], size=15, gap=10)
    L.code(s, 7.0, 2.05, CW-6.25, 2.6, [
        'JIKA status = "PASCA PELAKSANAAN"',
        '   → "Siap"',
        'JIKA status = "DALAM PELAKSANAAN"',
        '   → "Dalam Pelaksanaan"',
        'selainnya → "Belum Mula / Lain"',
    ], size=13, title_txt="kategori_status")
    L.note_strip(s, "Data sebenar JPD: PASCA PELAKSANAAN (949) · DALAM PELAKSANAAN (405). Seragamkan supaya visual status konsisten.", y=5.15)
    L.accent_bar(s); L.footer(s, 9)
    L.notes(s, "Applied Steps ialah kuasa Power Query — auto-ulang bila data dikemas kini. Tunjuk Conditional Column secara langsung.")


def integrasi():
    s = L.new_slide("SESI 4 · Integrasi")
    L.title(s, [[("Gabung ", {}), ("tiga fail", {"color": GOLD}), (" jadi satu pandangan", {})]])
    L.box(s, ML, 2.15, (CW-0.4)/2, 2.7, fill=CARD, line=BRD)
    L.text(s, ML+0.3, 2.4, 5, 0.4, "Append — susun baris", size=17, color=LGOLD, bold=True)
    L.text(s, ML+0.3, 2.95, (CW-0.4)/2-0.6, 1.7, [[("Cantum jadual struktur sama. Gabung ", {"color": INK}),
           ("JPD + BELB", {"color": WHITE, "bold": True}),
           (" → satu jadual Projek_Program dengan lajur ", {"color": INK}),
           ("program", {"color": CODEFG, "font": MONO}), (" = JPD/BELB.", {"color": INK})]],
           size=14, line_spacing=1.2)
    x2 = ML + (CW-0.4)/2 + 0.4
    L.box(s, x2, 2.15, (CW-0.4)/2, 2.7, fill=CARD, line=BRD)
    L.text(s, x2+0.3, 2.4, 5, 0.4, "Merge — gabung lajur", size=17, color=LGOLD, bold=True)
    L.text(s, x2+0.3, 2.95, (CW-0.4)/2-0.6, 1.7, [[("Bawa lajur dari jadual lain ikut kunci padanan ", {"color": INK}),
           ("kod_projek", {"color": CODEFG, "font": MONO}),
           (". Seperti VLOOKUP tetapi lebih berkuasa — kaitkan kewangan MyProjek.", {"color": INK})]],
           size=14, line_spacing=1.2)
    L.note_strip(s, "Hasil: satu pandangan projek yang boleh ditapis ikut program, negeri & status.", y=5.25)
    L.accent_bar(s); L.footer(s, 10)
    L.notes(s, "Append = tambah baris (JPD+BELB). Merge = tambah lajur (bawa kewangan MyProjek). Tekankan beza ini.")


def star():
    s = L.new_slide("SESI 5 · Pemodelan")
    L.title(s, [[("Star Schema", {"color": GOLD}), (" — bukan satu jadual besar", {})]])
    # center fact
    fx, fy, fw, fh = 5.4, 3.5, 2.6, 0.95
    L.box(s, fx, fy, fw, fh, fill=CARDD, line=GOLD, line_w=1.5)
    L.text(s, fx, fy+0.18, fw, 0.6, [[("Fakta_Projek", {})]], size=15, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    L.text(s, fx, fy+0.52, fw, 0.4, "kos · belanja · % kemajuan", size=10.5, color=MUTED, align=PP_ALIGN.CENTER)
    dims = [("Dim_Negeri", 2.2, 2.2), ("Dim_Status", 2.2, 4.6),
            ("Dim_Tarikh", 8.9, 2.2), ("Dim_Agensi", 8.9, 4.6)]
    for nm, dx, dy in dims:
        L.box(s, dx, dy, 2.2, 0.7, fill=CARD, line=BRD)
        L.text(s, dx, dy+0.18, 2.2, 0.4, nm, size=13, color=LGOLD, bold=True, align=PP_ALIGN.CENTER, font=MONO)
    L.text(s, ML, 5.7, CW, 0.5, [[("Fakta", {"color": GOLD, "bold": True}),
           (" = nombor diukur (satu baris = satu projek).  ", {"color": INK}),
           ("Dimensi", {"color": LGOLD, "bold": True}),
           (" = konteks untuk tapis/kumpul.  Relationship one-to-many.", {"color": INK})]], size=13.5)
    L.accent_bar(s); L.footer(s, 11)
    L.notes(s, "Star schema = prestasi + drill-down. Satu jadual raksasa = perlahan & bertindih. Dimensi mengelilingi fakta.")


def date_table():
    s = L.new_slide("SESI 5 · Date Table")
    L.title(s, [[("Date table ", {"color": GOLD}), ("— wajib untuk analisis masa", {})]])
    L.code(s, ML, 2.1, 6.2, 1.7, [
        'Dim_Tarikh =',
        'CALENDAR (',
        '   DATE ( 2015, 1, 1 ),',
        '   DATE ( 2030, 12, 31 ) )',
    ], size=13.5, title_txt="New Table")
    L.bullets(s, 7.3, 2.1, CW-6.55, 2.2, [
        [("Tambah lajur ", {}), ("Tahun = YEAR(Date)", {"font": MONO, "color": CODEFG})],
        "Mark as Date Table",
        "Berdasarkan tahun_jangka_mula / siap",
        "Membolehkan Time Intelligence (Hari 2)",
    ], size=13.5, gap=8)
    L.box(s, ML, 4.15, CW, 1.55, fill=CARD, line=BRD)
    L.text(s, ML+0.3, 4.35, CW-0.6, 0.4, "Amalan terbaik pemodelan", size=14, color=LGOLD, bold=True)
    L.bullets(s, ML+0.3, 4.8, CW-0.6, 0.9, [
        "Sembunyikan lajur teknikal (id, kunci) daripada paparan",
        "Elak relationship many-to-many melainkan perlu · satu Date table aktif",
    ], size=12.5, gap=4)
    L.accent_bar(s); L.footer(s, 12)
    L.notes(s, "Date table khusus supaya YoY & time intelligence berfungsi. Mark as Date Table penting.")


def lab():
    s = L.new_slide("Lab Hari 1")
    L.title(s, [[("Checklist ", {}), ("sebelum balik", {"color": GOLD})]])
    L.bullets(s, ML, 2.2, CW, 3.2, [
        "Ketiga-tiga set data dimuat & dibersihkan dalam Power Query",
        "Medan negeri, status_pelaksanaan & kewangan bertaip betul",
        "Jadual dimensi + Date table wujud (Mark as Date Table)",
        "Relationships dibina — star schema",
        [("Fail disimpan sebagai ", {}), ("hari-1.pbix", {"font": MONO, "color": CODEFG, "bold": True})],
    ], size=17, marker="☐  ", gap=12)
    L.accent_bar(s); L.footer(s, 13)
    L.notes(s, "Deliverable Hari 1 = hari-1.pbix dengan model bersepadu bersih. Lab penuh dalam hari-1/snippets/lab.md.")


def ringkasan():
    s = L.new_slide("Ringkasan Hari 1")
    L.title(s, [[("Anda telah bina ", {}), ("fondasi data", {"color": GOLD})]])
    L.bullets(s, ML, 2.05, CW, 2.0, [
        [("Faham ekosistem ", {}), ("Power BI · Fabric · Copilot", {"bold": True, "color": INK})],
        [("Muat & bersihkan ", {}), ("JPD, BELB, MyProjek", {"bold": True, "color": INK}), (" (Power Query)", {})],
        [("Gabung data ", {}), ("(Append + Merge)", {"bold": True, "color": INK}), (" jadi satu pandangan", {})],
        [("Bina ", {}), ("star schema + Date table + relationships", {"bold": True, "color": INK})],
    ], size=14.5, marker="✅  ", gap=7)
    data = [("📊", "Esok · Hari 2", "DAX, visual, drill-down & 4 halaman dashboard", True),
            ("🧮", "DAX", "Measures: Jumlah Projek, Peruntukan, % Utilisasi", False),
            ("🗺️", "Peta & drill", "Malaysia → Negeri → Daerah → Kampung → Projek", False)]
    w = (CW - 2*0.35)/3
    for i, (ico, hd, bd, dyn) in enumerate(data):
        L.card(s, ML + i*(w+0.35), 4.5, w, 1.85, ico, hd, bd, dyn=dyn, body_size=11)
    L.note_strip(s, "Simpan hari-1.pbix — esok kita hidupkan data ini dengan DAX & visual. AI membantu, anda memandu.", y=6.5)
    L.accent_bar(s); L.footer(s, 14)
    L.notes(s, "4 pencapaian Hari 1 + teaser Hari 2. Ingatkan simpan fail.")


def shots_setup():
    s = L.new_slide("Lampiran · Tangkapan Skrin Sebenar")
    L.title(s, [[("Persediaan Fabric ", {}), ("— skrin sebenar", {"color": GOLD})]], y=1.02, size=27)
    L.picture(s, "fabric-guide/01-workspace-kkdw-copilot.jpg", 0.78, 1.85, 5.6)
    L.picture(s, "fabric-guide/09-three-queries-loaded.jpg", 6.98, 1.85, 5.6)
    L.text(s, 0.78, 5.28, 5.6, 0.4, "Workspace KKDW Copilot (kapasiti Fabric)", size=12, color=MUTED)
    L.text(s, 6.98, 5.28, 5.6, 0.4, "Dataflow Gen2 KKDW_Ingest — JPD · BELB · MyProjek", size=12, color=MUTED)
    L.note_strip(s, "Aliran Data → Fabric dibina 100% dalam pelayar (tanpa Power BI Desktop) — data sebenar KKDW.", y=5.85)
    L.accent_bar(s); L.footer(s, 15)
    L.notes(s, "Tangkapan skrin sebenar dari tenant Fabric KKDW semasa persediaan kelas (SESI 2).")


def shots_model():
    s = L.new_slide("Lampiran · Tangkapan Skrin Sebenar")
    L.title(s, [[("Jadual bersepadu & ", {}), ("model KKDW_Model", {"color": GOLD})]], y=1.02, size=27)
    L.picture(s, "fabric-guide/11-lakehouse-projek-program.jpg", 0.78, 1.85, 5.6)
    L.picture(s, "fabric-guide/10-model-view.jpg", 6.98, 1.85, 5.6)
    L.text(s, 0.78, 5.28, 5.6, 0.4, "Lakehouse: Projek_Program (JPD∪BELB, 1,399 baris)", size=12, color=MUTED)
    L.text(s, 6.98, 5.28, 5.6, 0.4, "Model view: star schema (7 jadual + relationships)", size=12, color=MUTED)
    L.note_strip(s, "Model DirectLake KKDW_Model — 7 jadual, 4 relationships, 23 measures, semua diuji.", y=5.85)
    L.accent_bar(s); L.footer(s, 16)
    L.notes(s, "Jadual bersepadu Projek_Program + model bersepadu (SESI 4–5). Dibina tanpa Power BI Desktop.")


def penutup():
    s = L.new_slide()
    L.box(s, 0, 0, 0.18, SH, fill=GOLD, radius=False)
    L.text(s, ML, 2.7, CW, 1.0, [[("Terima kasih", {"color": WHITE})]], size=44, bold=True)
    L.text(s, ML, 3.9, CW, 0.6, "Hari 1 selesai — fondasi data siap. Jumpa esok untuk Power BI!", size=18, color=MUTED)
    L.text(s, ML, 4.9, CW, 0.5, "hari-1/README.md · hari-1/snippets/lab.md", size=14, color=LGOLD, font=MONO)
    L.accent_bar(s); L.footer(s, 17)
    L.notes(s, "Penutup Hari 1.")


for fn in [cover, aliran, konteks, kenapa, ekosistem, persediaan, fabric, import_dq,
           power_query, integrasi, star, date_table, lab, ringkasan,
           shots_setup, shots_model, penutup]:
    fn()

L.prs.save("day1-fondasi-data.pptx")
print(f"Wrote day1-fondasi-data.pptx ({len(L.prs.slides._sldIdLst)} slides)")
