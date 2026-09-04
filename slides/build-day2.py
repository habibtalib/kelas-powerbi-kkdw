#!/usr/bin/env python
"""Build the Hari 2 deck — Power BI: DAX, Visualisasi & Dashboard (SESI 6-10).

    cd slides && python build-day2.py     # writes day2-power-bi.pptx
"""
import _pbi_lib as L
from _pbi_lib import (ML, MR, MT, CW, SW, SH, MONO, SANS,
                      WHITE, INK, MUTED, GOLD, LGOLD, BLUE, CARD, CARDD, BRD,
                      CODEFG, GOOD, AMBER, BG0)
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

L.TOTAL = 15


def cover():
    s = L.new_slide()
    L.box(s, 0, 0, 0.18, SH, fill=GOLD, radius=False)
    L.text(s, ML, 1.5, CW, 0.5, "Power BI · Microsoft Fabric · Copilot", size=15, color=LGOLD, bold=True)
    L.title(s, [[("Hari 2 — Power BI", {})]], y=2.1, size=46)
    L.text(s, ML, 3.15, CW, 0.9, [[("DAX · Visualisasi · ", {"color": INK}), ("Dashboard", {"color": GOLD})]], size=26, bold=True)
    L.text(s, ML, 4.2, CW, 0.6, "Menukar model data kepada dashboard pengurusan interaktif", size=16, color=MUTED)
    L.pipeline(s, ML, 5.15, CW, ["DAX", "Visual", "Drill-down", "4 Halaman", "Publish"])
    L.note_strip(s, "Hari ini: 8 measure teras + 4 halaman dashboard, diterbit ke Power BI Service.", y=6.3)
    L.accent_bar(s); L.footer(s, 1)
    L.notes(s, "Pembukaan Hari 2. Semalam data; hari ini kita hidupkannya.")


def recap():
    s = L.new_slide("Sambungan Hari 1")
    L.title(s, [[("Kita ada ", {}), ("model data bersepadu", {"color": GOLD})]])
    L.bullets(s, ML, 2.1, CW, 2.0, [
        [("hari-1.pbix", {"font": MONO, "color": CODEFG, "bold": True}), (" — JPD + BELB + MyProjek, bersih & bermodel", {})],
        "Star schema: Fakta_Projek + Dim_Negeri/Status/Tarikh",
        "Medan bertaip betul, status diseragamkan",
    ], size=15, gap=9)
    L.box(s, ML, 4.4, CW, 1.2, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML+0.3, 4.65, CW-0.6, 0.7, [[("Hari ini: ", {"color": GOLD, "bold": True}),
           ("kira KPI (DAX) → bina visual → drill-down & peta → 4 halaman → publish.", {"color": INK})]], size=15.5)
    L.accent_bar(s); L.footer(s, 2)
    L.notes(s, "Pastikan semua peserta ada hari-1.pbix sebelum mula. Yang ketinggalan boleh guna fail rujukan.")


def dax_apa():
    s = L.new_slide("SESI 6 · DAX")
    L.title(s, [[("Apa itu ", {}), ("DAX", {"color": GOLD}), ("?", {})]])
    L.text(s, ML, 2.05, CW, 0.9, [[("Data Analysis Expressions", {"color": WHITE, "bold": True}),
           (" — bahasa formula Power BI. Seperti formula Excel, tetapi bekerja atas ", {"color": INK}),
           ("jadual & relationships", {"color": LGOLD, "bold": True}), (", bukan sel.", {"color": INK})]],
           size=17, line_spacing=1.2)
    L.box(s, ML, 3.3, (CW-0.4)/2, 2.4, fill=CARD, line=BRD)
    L.text(s, ML+0.3, 3.55, 5, 0.4, "Calculated Column", size=16, color=INK, bold=True)
    L.bullets(s, ML+0.3, 4.1, (CW-0.4)/2-0.6, 1.5, [
        "Dikira baris demi baris, disimpan", "Guna memori",
        "Contoh: kategori status per projek",
    ], size=13, gap=6)
    x2 = ML + (CW-0.4)/2 + 0.4
    L.box(s, x2, 3.3, (CW-0.4)/2, 2.4, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, x2+0.3, 3.55, 5, 0.4, "Measure  ✓ utamakan", size=16, color=GOLD, bold=True)
    L.bullets(s, x2+0.3, 4.1, (CW-0.4)/2-0.6, 1.5, [
        "Dikira masa nyata, ikut konteks visual", "Tidak guna memori",
        "Contoh: Jumlah Peruntukan, % Utilisasi",
    ], size=13, gap=6)
    L.note_strip(s, "Prestasi: utamakan measure; jika perlu lajur baru, buat di Power Query (bukan calculated column). Guna VAR untuk measure kompleks (Hari 3).", y=6.0)
    L.accent_bar(s); L.footer(s, 3)
    L.notes(s, "Utamakan measure untuk KPI. Calculated column hanya bila perlu nilai per-baris — dan jika boleh, buat di Power Query/sumber supaya model kecil. "
               "📘 Buku Bab 9: calc column vs measure ms 210, VAR untuk kekemasan & prestasi.")


def filter_context():
    s = L.new_slide("SESI 6 · Filter Context")
    L.title(s, [[("Satu measure, ", {}), ("banyak konteks", {"color": GOLD})]])
    L.text(s, ML, 2.05, CW, 0.8, [[("Nilai measure ", {"color": INK}),
           ("berubah ikut konteks", {"color": LGOLD, "bold": True}),
           (" visual — inilah kuasa DAX.", {"color": INK})]], size=17)
    L.code(s, ML, 3.0, 5.9, 0.95, ['Jumlah Kos = SUM ( Fakta[kos_projek] )'], size=13.5)
    L.bullets(s, ML, 4.2, CW, 1.6, [
        [("Pada satu ", {}), ("Card", {"bold": True, "color": INK}), (" → jumlah keseluruhan semua projek", {})],
        [("Dalam carta ", {}), ("\"ikut negeri\"", {"bold": True, "color": INK}), (" → automatik dikira per negeri", {})],
        [("Ditapis ", {}), ("slicer Tahun = 2024", {"bold": True, "color": INK}), (" → hanya projek 2024", {})],
    ], size=14.5, gap=8)
    L.note_strip(s, "Tulis measure sekali; Power BI kira semula ikut setiap visual, slicer & drill. Tak perlu ulang formula.", y=6.0)
    L.accent_bar(s); L.footer(s, 4)
    L.notes(s, "Konsep paling penting DAX untuk pemula. Tunjuk measure sama pada card vs bar chart.")


def kpi():
    s = L.new_slide("SESI 6 · KPI KKDW")
    L.title(s, [[("8 measure ", {"color": GOLD}), ("teras", {})]])
    L.code(s, ML, 2.05, CW, 3.4, [
        'Jumlah Projek     = COUNTROWS ( Projek_Program )',
        'Jumlah Peruntukan = SUM ( MyProjek[peruntukan_disemak_janm] )',
        'Jumlah Belanja    = SUM ( MyProjek[belanja_janm] )',
        'Baki              = [Jumlah Peruntukan] - [Jumlah Belanja]',
        '% Utilisasi       = DIVIDE ( [Jumlah Belanja], [Jumlah Peruntukan] )',
        'Projek Siap       = CALCULATE ( [Jumlah Projek],',
        '                       Projek_Program[kategori_status] = "Siap" )',
    ], size=13)
    L.note_strip(s, "Guna DIVIDE(a,b) bukan a/b — ia elak ralat bahagi-dengan-sifar. Letak semua dalam jadual _Measures.", y=5.7)
    L.accent_bar(s); L.footer(s, 5)
    L.notes(s, "Bina measure secara langsung. Tekankan DIVIDE & CALCULATE. Sesuaikan nama medan ikut model.")


def pilih_visual():
    s = L.new_slide("SESI 7 · Visualisasi")
    L.title(s, [[("Pilih ", {}), ("visual yang betul", {"color": GOLD})]])
    L.table(s, ML, 2.15, CW, [
        ("Satu nombor penting (jumlah projek, peruntukan)", "Card / KPI"),
        ("Perbandingan antara kategori (projek ikut negeri)", "Bar / Column"),
        ("Trend ikut masa (belanja ikut tahun)", "Line"),
        ("Nilai berperingkat + drill (negeri → daerah)", "Matrix"),
        ("Bahagian daripada keseluruhan (status)", "Donut"),
        ("Lokasi geografi projek", "Map"),
    ], col_w=[0.68, 0.32], header=["Nak tunjuk", "Visual"], row_h=0.56, size=14)
    L.accent_bar(s); L.footer(s, 6)
    L.notes(s, "Bukan setiap data sesuai setiap carta. Elak pie/donut bila kategori banyak.")


def reka_bentuk():
    s = L.new_slide("SESI 7 · Reka Bentuk")
    L.title(s, [[("Prinsip ", {}), ("dashboard pengurusan", {"color": GOLD})]])
    data = [("🎯", "Fokus", "Nombor paling penting di atas-kiri (mata mula baca di situ)"),
            ("🧹", "Kurangkan bunyi", "Buang grid berlebihan, warna melampau, 3D"),
            ("🎨", "Konsisten", "Satu palet · warna status seragam (Hijau/Kuning/Merah)"),
            ("🏷️", "Konteks", "Setiap visual ada tajuk & unit (RM, %, km)")]
    w = (CW - 0.35)/2
    for i, (ico, hd, bd) in enumerate(data):
        L.card(s, ML + (i % 2)*(w+0.35), 2.2 + (i//2)*1.7, w, 1.5, ico, hd, bd, body_size=12)
    L.note_strip(s, "Conditional Formatting: warnakan nilai automatik ikut syarat — asas indikator risiko Hari 3.", y=5.9)
    L.accent_bar(s); L.footer(s, 7)
    L.notes(s, "Reka bentuk = kejelasan, bukan hiasan. Warna status mesti seragam sepanjang laporan.")


def interaktif():
    s = L.new_slide("SESI 8 · Interaktiviti")
    L.title(s, [[("Drill-down ", {"color": GOLD}), ("hierarki KKDW", {})]])
    L.box(s, ML, 2.15, CW, 0.85, fill=CARDD, line=GOLD, line_w=1.25)
    L.text(s, ML, 2.4, CW, 0.4, "Malaysia → Negeri → Parlimen → DUN → Kampung → Projek",
           size=18, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    L.bullets(s, ML, 3.4, CW, 2.2, [
        [("Slicer", {"bold": True, "color": INK}), (" — penapis Negeri / Tahun / Program di atas halaman", {})],
        [("Cross-filter", {"bold": True, "color": INK}), (" — klik satu bar → semua visual lain ditapis", {})],
        [("Drill-down", {"bold": True, "color": INK}), (" — turun peringkat dalam satu visual (Negeri → Daerah)", {})],
        [("Drill-through", {"bold": True, "color": INK}), (" — klik kanan projek → lompat ke halaman butiran", {})],
    ], size=14.5, gap=9)
    L.accent_bar(s); L.footer(s, 8)
    L.notes(s, "Hierarki lokasi ialah cadangan rasmi KKDW. Drill-down dalam satu visual; drill-through antara halaman.")


def peta():
    s = L.new_slide("SESI 8 · Peta")
    L.title(s, [[("Lokasi projek ", {}), ("pada peta", {"color": GOLD})]])
    L.bullets(s, ML, 2.1, CW, 2.0, [
        [("JPD", {"bold": True, "color": INK}), (" ada koordinat ", {}),
         ("lat_1, long_1", {"font": MONO, "color": CODEFG}), (" → Map (titik lokasi jalan)", {})],
        [("BELB / MyProjek", {"bold": True, "color": INK}), (" → Filled Map ikut Negeri / Daerah", {})],
        [("Saiz titik", {"bold": True, "color": INK}), (" = kos projek → nampak projek besar sekilas", {})],
    ], size=15, gap=9)
    L.box(s, ML, 4.4, CW, 1.2, fill=CARD, line=BRD)
    L.text(s, ML+0.3, 4.6, CW-0.6, 0.8, [[("Tip: ", {"color": GOLD, "bold": True}),
           ("set Data Category medan lokasi (Modeling → Data Category → State/Province, City) supaya Power BI kenal tempat dengan tepat.", {"color": INK})]],
           size=13.5, line_spacing=1.2)
    L.accent_bar(s); L.footer(s, 9)
    L.notes(s, "Data Category penting untuk peta ikut nama tempat. Koordinat JPD terus boleh dipeta.")


def dashboard():
    s = L.new_slide("SESI 9 · Dashboard")
    L.title(s, [[("Empat halaman ", {"color": GOLD}), ("bersepadu", {})]])
    data = [("1", "Executive Overview", "Jumlah projek, peruntukan, status, kemajuan, projek berisiko"),
            ("2", "JPD Performance", "Projek & kos ikut negeri, panjang jalan, kos/km, peta"),
            ("3", "BELB Performance", "Kampung terlibat, sambungan siap vs sasaran, kos/sambungan"),
            ("4", "Financial & Physical", "Peruntukan vs belanja vs baki, % utilisasi, ketidakpadanan")]
    y = 2.15; h = 0.82
    for i, (n, hd, bd) in enumerate(data):
        yy = y + i*(h+0.13)
        L.numbered(s, ML, yy+0.16, n, color=GOLD)
        L.box(s, ML+0.7, yy, CW-0.7, h, fill=CARD, line=BRD, line_w=1)
        L.text(s, ML+0.95, yy+0.13, 3.6, 0.5, hd, size=16, color=WHITE, bold=True)
        L.text(s, ML+4.7, yy+0.16, CW-5.3, 0.5, bd, size=12.5, color=MUTED)
    L.note_strip(s, "Halaman ke-5 (AI Project Risk & Early Warning) dibina esok, Hari 3. Simpan hari-2.pbix.", y=5.85)
    L.accent_bar(s); L.footer(s, 10)
    L.notes(s, "Struktur sasaran projek. Slicer Negeri/Tahun/Program pada setiap halaman.")


def publish():
    s = L.new_slide("SESI 10 · Publish")
    L.title(s, [[("Terbit & ", {}), ("kongsi selamat", {"color": GOLD})]])
    L.bullets(s, ML, 2.05, CW, 2.5, [
        [("Publish", {"bold": True, "color": INK}), (" → pilih Workspace KKDW → laporan naik ke Power BI Service", {})],
        [("Report vs Dashboard vs App", {"bold": True, "color": INK}), (" — laporan penuh, papan pin, pakej dikongsi", {})],
        [("Scheduled refresh", {"bold": True, "color": INK}), (" — dashboard sentiasa terkini", {})],
        [("RLS + OLS", {"bold": True, "color": INK}), (" — sekat baris (Sabah → projek Sabah) & lajur sensitif (kos)", {})],
        [("Endorsement", {"bold": True, "color": INK}), (" — model rasmi ditanda ", {}), ("Certified", {"bold": True, "color": GOOD}), (" supaya pegawai kenal sumber sebenar", {})],
    ], size=14, gap=7)
    L.box(s, ML, 4.65, CW, 1.05, fill=CARDD, line=AMBER, line_w=1.25)
    L.text(s, ML+0.3, 4.85, CW-0.6, 0.7, [[("Keselamatan data KKDW: ", {"color": AMBER, "bold": True}),
           ("kongsi hanya kepada pengguna dibenarkan · RLS/OLS untuk data sensitif · sahkan residensi data dengan IT.", {"color": INK})]],
           size=13.5, line_spacing=1.15)
    L.accent_bar(s); L.footer(s, 11)
    L.notes(s, "RLS (baris) + OLS (lajur/jadual) konsep ringkas sahaja hari ini; laksana penuh ikut dasar KKDW. "
               "Endorsement 'Certified' menandakan sumber rasmi. Untuk pasukan besar ada deployment pipelines (Dev→Test→Prod) & Git — di luar skop kursus. "
               "📘 Buku Bab 10 (OLS ms 240, RLS ms 243), Bab 11 (endorsement ms 250, pipelines ms 252).")


def lab():
    s = L.new_slide("Lab Hari 2")
    L.title(s, [[("Checklist ", {}), ("sebelum balik", {"color": GOLD})]])
    L.bullets(s, ML, 2.2, CW, 3.2, [
        "8 measure teras siap & betul",
        "4 halaman dashboard lengkap",
        "Drill-down (Negeri → Daerah → Kampung) & peta berfungsi",
        "Slicer Negeri/Tahun/Program merentas visual",
        [("Laporan diterbit ke Service · disimpan ", {}), ("hari-2.pbix", {"font": MONO, "color": CODEFG, "bold": True})],
    ], size=16.5, marker="☐  ", gap=11)
    L.accent_bar(s); L.footer(s, 12)
    L.notes(s, "Deliverable Hari 2 = dashboard 4 halaman diterbit. Lab penuh: hari-2/snippets/lab.md.")


def ringkasan():
    s = L.new_slide("Ringkasan Hari 2")
    L.title(s, [[("Dashboard anda ", {}), ("berfungsi", {"color": GOLD})]])
    L.bullets(s, ML, 2.05, CW, 2.0, [
        [("Kuasai ", {}), ("DAX", {"bold": True, "color": INK}), (" — measure, CALCULATE, filter context", {})],
        [("Bina ", {}), ("visual berkesan", {"bold": True, "color": INK}), (" + conditional formatting", {})],
        [("Interaktiviti ", {}), ("drill-down, drill-through & peta", {"bold": True, "color": INK})],
        [("Terbit ", {}), ("4 halaman dashboard", {"bold": True, "color": INK}), (" ke Power BI Service", {})],
    ], size=14.5, marker="✅  ", gap=7)
    data = [("🤖", "Esok · Hari 3", "Analitik risiko + Copilot/AI + capstone", True),
            ("🚦", "Early Warning", "Varians jadual vs sebenar · Hijau/Kuning/Merah", False),
            ("🧠", "Copilot", "Tanya data bahasa biasa, ringkasan eksekutif", False)]
    w = (CW - 2*0.35)/3
    for i, (ico, hd, bd, dyn) in enumerate(data):
        L.card(s, ML + i*(w+0.35), 4.5, w, 1.85, ico, hd, bd, dyn=dyn, body_size=11)
    L.note_strip(s, "Esok kita tambah kecerdasan — kesan risiko & keutamaan. AI membantu, anda memandu.", y=6.5)
    L.accent_bar(s); L.footer(s, 13)
    L.notes(s, "4 pencapaian + teaser Hari 3.")


def kuiz():
    s = L.new_slide("Kuiz Recap · Kahoot")
    L.title(s, [[("Kuiz recap ", {}), ("Hari 2", {"color": GOLD}), (" — Kahoot (12 soalan)", {})]])
    L.text(s, ML, 1.98, CW, 0.5,
           "Main sebagai kumpulan untuk semak kefahaman — jawapan betul ditebalkan.",
           size=13.5, color=MUTED)
    w = (CW - 0.4) / 2
    top = 2.65; ch = 3.25
    # DAX column
    L.box(s, ML, top, w, ch, fill=CARD, line=BRD)
    L.text(s, ML+0.3, top+0.18, w-0.6, 0.4, "DAX", size=15, color=GOLD, bold=True)
    L.bullets(s, ML+0.3, top+0.75, w-0.6, ch-0.9, [
        [("DAX = ", {}), ("Data Analysis Expressions", {"bold": True, "color": INK})],
        [("Measure vs column → ", {}), ("measure ikut konteks, tak disimpan", {"bold": True, "color": INK})],
        [("Filter context → ", {}), ("nilai berubah ikut visual", {"bold": True, "color": INK})],
        [("Kira bilangan baris → ", {}), ("COUNTROWS", {"bold": True, "color": INK})],
        [("Ubah filter context → ", {}), ("CALCULATE", {"bold": True, "color": INK})],
        [("Multi-syarat (ganti IF) → ", {}), ("SWITCH", {"bold": True, "color": INK})],
        [("% Utilisasi / elak ÷0 → ", {}), ("DIVIDE", {"bold": True, "color": INK})],
    ], size=11.5, gap=6)
    # Visualisasi column
    x2 = ML + w + 0.4
    L.box(s, x2, top, w, ch, fill=CARD, line=BRD)
    L.text(s, x2+0.3, top+0.18, w-0.6, 0.4, "Visualisasi & Dashboard", size=15, color=GOLD, bold=True)
    L.bullets(s, x2+0.3, top+0.75, w-0.6, ch-0.9, [
        [("Hierarki drill-down → ", {}), ("Malaysia→Negeri→…→Projek", {"bold": True, "color": INK})],
        [("Drill-down vs drill-through → ", {}), ("1 visual vs halaman butiran", {"bold": True, "color": INK})],
        [("Warna status seragam → ", {}), ("Hijau/Kuning/Merah", {"bold": True, "color": INK})],
        [("Peta ikut nama tempat → ", {}), ("set Data Category", {"bold": True, "color": INK})],
    ], size=11.5, gap=6)
    L.note_strip(s, "Kahoot: “Kuiz Hari 2 KKDW — DAX & Visualisasi” (12 soalan) — host dari Library Kahoot. Bermain ~10 min.", y=6.1)
    L.accent_bar(s); L.footer(s, 14)
    L.notes(s, "Kuiz recap interaktif. Jawapan penuh: "
               "1) DAX = Data Analysis Expressions. "
               "2) Measure dikira masa nyata ikut konteks (tak disimpan); calculated column disimpan baris demi baris. "
               "3) Filter context = nilai measure berubah ikut konteks visual (cth per negeri). "
               "4) COUNTROWS untuk kira bilangan baris. "
               "5) CALCULATE untuk mengubah/menimpa filter context. "
               "6) SWITCH untuk menggantikan IF berbilang cabang. "
               "7) % Utilisasi = DIVIDE([Jumlah Belanja], [Jumlah Peruntukan]). "
               "8) Guna DIVIDE bukan / untuk elak ralat bahagi-dengan-sifar. "
               "9) Hierarki: Malaysia→Negeri→Parlimen→DUN→Kampung→Projek. "
               "10) Drill-down turun hierarki dalam 1 visual; drill-through lompat ke halaman butiran. "
               "11) Warna status: Hijau=Siap, Kuning=Risiko, Merah=Lewat. "
               "12) Untuk peta ikut nama tempat, set Data Category (State/Province, City). "
               "Host dari Library Kahoot; plan percuma = 15 min / 20 pemain setiap sesi.")


def penutup():
    s = L.new_slide()
    L.box(s, 0, 0, 0.18, SH, fill=GOLD, radius=False)
    L.text(s, ML, 2.7, CW, 1.0, [[("Terima kasih", {"color": WHITE})]], size=44, bold=True)
    L.text(s, ML, 3.9, CW, 0.6, "Hari 2 selesai — dashboard hidup. Esok: analitik & AI!", size=18, color=MUTED)
    L.text(s, ML, 4.9, CW, 0.5, "hari-2/README.md · hari-2/snippets/lab.md", size=14, color=LGOLD, font=MONO)
    L.accent_bar(s); L.footer(s, 15)
    L.notes(s, "Penutup Hari 2.")


for fn in [cover, recap, dax_apa, filter_context, kpi, pilih_visual, reka_bentuk,
           interaktif, peta, dashboard, publish, lab, ringkasan, kuiz, penutup]:
    fn()

L.prs.save("day2-power-bi.pptx")
print(f"Wrote day2-power-bi.pptx ({len(L.prs.slides._sldIdLst)} slides)")
