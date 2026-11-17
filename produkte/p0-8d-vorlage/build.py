#!/usr/bin/env python3
"""Generator für p0-8d-vorlage – „8D-Report Vorlage (Excel)“.

Aufruf:
    python3 build.py           # baut dist/8D-Report-Vorlage.xlsx
    python3 build.py --test    # baut und testet (openpyxl + LibreOffice headless, falls vorhanden)

Anforderungen: Python 3.9+, openpyxl 3.1. Keine Makros, keine Matrixformeln.
"""
import datetime as dt
import os
import shutil
import subprocess
import sys
import tempfile

from openpyxl import Workbook, load_workbook
from openpyxl.formatting.rule import DataBarRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.worksheet.hyperlink import Hyperlink

HERE = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(HERE, "dist")
OUTFILE = os.path.join(DIST, "8D-Report-Vorlage.xlsx")

VERSION = "1.0"
STAND = "11/2026"
PRODUKT = "8D-Report Vorlage (Excel)"
# Vor Veröffentlichung durch den Inhaber konkretisieren (Name/Firma laut Impressum):
ANBIETER = "der Anbieter dieser Vorlage (siehe Impressum der Website, über die Sie die Datei bezogen haben)"
BEISPIEL = "Beispiel – löschen"

# ---------------------------------------------------------------- Design
NAVY = "1F3864"
SLATE = "44546A"
GREY_D = "595959"
GREY_M = "D9D9D9"
GREY_L = "F2F2F2"
EX_FILL = "E7E6E6"
EX_FONT = "7F7F7F"
WHITE = "FFFFFF"

F_TITLE = Font(name="Calibri", size=16, bold=True, color=WHITE)
F_SEC = Font(name="Calibri", size=12, bold=True, color=WHITE)
F_HEAD = Font(name="Calibri", size=10, bold=True, color=WHITE)
F_BODY = Font(name="Calibri", size=10)
F_BOLD = Font(name="Calibri", size=10, bold=True)
F_HINT = Font(name="Calibri", size=9, italic=True, color=GREY_D)
F_EX = Font(name="Calibri", size=10, italic=True, color=EX_FONT)
F_LINK = Font(name="Calibri", size=10, color="0563C1", underline="single")

FILL_NAVY = PatternFill("solid", fgColor=NAVY)
FILL_SLATE = PatternFill("solid", fgColor=SLATE)
FILL_GREY_L = PatternFill("solid", fgColor=GREY_L)
FILL_GREY_M = PatternFill("solid", fgColor=GREY_M)
FILL_EX = PatternFill("solid", fgColor=EX_FILL)
FILL_WHITE = PatternFill("solid", fgColor=WHITE)

THIN = Side(style="thin", color="A6A6A6")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")
WRAP_C = Alignment(wrap_text=True, vertical="center", horizontal="center")
DATE_FMT = "DD.MM.YYYY"

# Ampelfarben (Excel-Standardpalette „gut/neutral/schlecht“)
RED = (PatternFill("solid", fgColor="FFC7CE", bgColor="FFC7CE"), Font(color="9C0006", bold=True))
YEL = (PatternFill("solid", fgColor="FFEB9C", bgColor="FFEB9C"), Font(color="9C5700", bold=True))
GRN = (PatternFill("solid", fgColor="C6EFCE", bgColor="C6EFCE"), Font(color="006100", bold=True))
GRY = (PatternFill("solid", fgColor=GREY_M, bgColor=GREY_M), Font(color=GREY_D))
EXR = (PatternFill("solid", fgColor=EX_FILL, bgColor=EX_FILL), Font(color=EX_FONT, italic=True))

L_STATUS8D = ["offen", "in Arbeit", "erledigt", "n. a."]
L_STATUS = ["offen", "in Arbeit", "erledigt", "verworfen"]
L_JNO = ["ja", "nein", "offen"]
L_JNU = ["ja", "nein", "unklar"]
L_JNNA = ["ja", "nein", "n. a."]
L_ROLLE = ["Teamleiter", "Teammitglied", "Sponsor", "Experte"]
L_ORT = ["Kunde", "Transit", "Lager Lieferant", "Fertigung", "Unterlieferant"]
L_URS = ["Auftreten", "Nichtentdeckung"]
L_6M = ["Mensch", "Maschine", "Methode", "Material", "Messung", "Mitwelt"]
L_BEW = ["bestätigt", "wahrscheinlich", "möglich", "ausgeschlossen"]
L_BEZUG = ["D3", "D5", "D6", "D7", "sonstige"]
L_ART = ["Sofortmaßnahme", "Abstellmaßnahme", "Vorbeugemaßnahme"]


# ---------------------------------------------------------------- Helfer
def style_range(ws, rng, font=None, fill=None, border=None, align=None, fmt=None):
    for row in ws[rng]:
        for c in row:
            if font is not None:
                c.font = font
            if fill is not None:
                c.fill = fill
            if border is not None:
                c.border = border
            if align is not None:
                c.alignment = align
            if fmt is not None:
                c.number_format = fmt


def put(ws, r, c1, c2, value=None, font=F_BODY, fill=None, border=BORDER, align=WRAP, fmt=None):
    """Schreibt value in (r,c1) und verbindet bis c2 (gleiche Zeile)."""
    a = f"{get_column_letter(c1)}{r}"
    b = f"{get_column_letter(c2)}{r}"
    if c2 > c1:
        ws.merge_cells(f"{a}:{b}")
    style_range(ws, f"{a}:{b}", font=font, fill=fill, border=border, align=align, fmt=fmt)
    if value is not None:
        ws[a] = value
    return ws[a]


def title(ws, text, last_col, subtitle=None):
    put(ws, 1, 1, last_col, text, font=F_TITLE, fill=FILL_NAVY, border=None,
        align=Alignment(vertical="center", indent=1))
    ws.row_dimensions[1].height = 30
    if subtitle:
        put(ws, 2, 1, last_col - 1, subtitle, font=F_HINT, border=None,
            align=Alignment(vertical="center", wrap_text=True))
    c = ws.cell(row=2, column=last_col, value="← Start")
    c.hyperlink = Hyperlink(ref=c.coordinate, location="'Start'!A1")
    c.font = F_LINK
    c.alignment = Alignment(horizontal="right", vertical="center")
    ws.row_dimensions[2].height = 28


def section(ws, r, text, last_col, hint=None):
    put(ws, r, 1, last_col, text, font=F_SEC, fill=FILL_NAVY, border=None,
        align=Alignment(vertical="center", indent=1))
    ws.row_dimensions[r].height = 20
    if hint:
        put(ws, r + 1, 1, last_col, hint, font=F_HINT, fill=FILL_GREY_L, border=None,
            align=Alignment(wrap_text=True, vertical="center", indent=1))
        ws.row_dimensions[r + 1].height = 30
        return r + 2
    return r + 1


def header(ws, r, spans, height=30):
    """spans: Liste von (c1, c2, text)."""
    for c1, c2, text in spans:
        put(ws, r, c1, c2, text, font=F_HEAD, fill=FILL_SLATE, align=WRAP_C)
    ws.row_dimensions[r].height = height


def body_row(ws, r, spans, values=None, height=None, fmts=None):
    values = values or {}
    fmts = fmts or {}
    for c1, c2, _ in spans:
        put(ws, r, c1, c2, values.get(c1), fmt=fmts.get(c1))
    if height:
        ws.row_dimensions[r].height = height


def dv_list(ws, items, rng):
    dv = DataValidation(type="list", formula1='"' + ",".join(items) + '"', allow_blank=True,
                        showErrorMessage=True, errorTitle="Ungültige Eingabe",
                        error="Bitte einen Wert aus der Liste wählen.")
    dv.add(rng)
    ws.add_data_validation(dv)


def dv_date(ws, rng):
    dv = DataValidation(type="date", operator="greaterThan", formula1="36526", allow_blank=True,
                        showErrorMessage=True, errorTitle="Datum erwartet",
                        error="Bitte ein Datum eingeben (TT.MM.JJJJ).")
    dv.add(rng)
    ws.add_data_validation(dv)


def cf_text(ws, rng, col_abs_first, mapping):
    """Bedingte Formatierung: Zellwert-Text → (fill,font)."""
    for txt, (fill, font) in mapping.items():
        ws.conditional_formatting.add(
            rng, FormulaRule(formula=[f'{col_abs_first}="{txt}"'], fill=fill, font=font, stopIfTrue=True))


def cf_example(ws, rng, marker_cell):
    """Beispielzeile grau/kursiv, solange die Markierungszelle „Beispiel“ enthält."""
    ws.conditional_formatting.add(
        rng, FormulaRule(formula=[f'ISNUMBER(SEARCH("Beispiel",{marker_cell}))'],
                         fill=EXR[0], font=EXR[1], stopIfTrue=True))


def page(ws, print_rows=None, area=None):
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A4
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.print_options.horizontalCentered = True
    ws.page_margins.left = ws.page_margins.right = 0.4
    ws.page_margins.top = ws.page_margins.bottom = 0.5
    ws.oddFooter.left.text = f"{PRODUKT} v{VERSION}"
    ws.oddFooter.center.text = "&A"
    ws.oddFooter.right.text = "Seite &P von &N"
    if print_rows:
        ws.print_title_rows = print_rows
    if area:
        ws.print_area = area
    ws.sheet_view.showGridLines = False


def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w


AMPEL_MAP = {"überfällig": RED, "fällig ≤ 7 T": YEL, "kein Termin": YEL,
             "im Plan": GRN, "erledigt": GRN, "verworfen": GRY, "–": GRY}


# ---------------------------------------------------------------- Blätter
def build_start(wb, sheets):
    ws = wb.active
    ws.title = "Start"
    widths(ws, [4, 30, 70, 4])
    put(ws, 1, 1, 4, f"{PRODUKT}", font=F_TITLE, fill=FILL_NAVY, border=None,
        align=Alignment(vertical="center", indent=1))
    ws.row_dimensions[1].height = 34
    put(ws, 2, 1, 4, f"Version {VERSION} · Stand {STAND} · kostenlose Arbeitshilfe für die strukturierte "
        "Reklamationsbearbeitung nach der 8D-Methode", font=F_HINT, border=None,
        align=Alignment(vertical="center", indent=1))
    r = 4
    r = section(ws, r, "Zweck", 4)
    put(ws, r, 2, 3, "Mit dieser Arbeitsmappe bearbeiten Sie eine Reklamation Schritt für Schritt nach der "
        "8D-Methode: Sofortreaktion, Team, Problembeschreibung, Sofortmaßnahmen, Ursachenanalyse "
        "(Auftreten UND Nichtentdeckung), Abstellmaßnahmen, Wirksamkeitsnachweis, Vorbeugung und "
        "Abschluss. 5-Why, Ishikawa (6M) und ein Maßnahmentracker mit Terminampel sind integriert.",
        border=None)
    ws.row_dimensions[r].height = 58
    r += 2
    r = section(ws, r, "Inhaltsverzeichnis (Klick führt zum Blatt)", 4)
    for name, desc in sheets:
        c = ws.cell(row=r, column=2, value=name)
        c.hyperlink = Hyperlink(ref=c.coordinate, location=f"'{name}'!A1")
        c.font = F_LINK
        c.border = BORDER
        c.alignment = Alignment(vertical="center", indent=1)
        put(ws, r, 3, 3, desc, align=Alignment(wrap_text=True, vertical="center"))
        ws.row_dimensions[r].height = 30
        r += 1
    r += 1
    r = section(ws, r, "Kurzanleitung", 4)
    steps = [
        "1. Speichern Sie die Datei je Reklamation unter einem eigenen Namen (z. B. 8D_<8D-Nr>_<Teilenummer>.xlsx).",
        "2. 8D-Report: Kopfdaten ausfüllen, in der Statusübersicht Verantwortliche und Soll-Termine je Disziplin eintragen "
        "(Kundenvorgaben beachten).",
        "3. D2 sauber beschreiben (5W2H, Ist/Ist-nicht) – noch ohne Ursache. D3: Kunde schützen, alle Bestände erfassen.",
        "4. Ursachen auf den Blättern 5-Why (zwei Pfade: Auftreten + Nichtentdeckung) und Ishikawa ermitteln, "
        "verifizierte Ursachen in D4 übertragen.",
        "5. Alle Maßnahmen zusätzlich im Maßnahmentracker führen – die Ampel zeigt überfällige Termine (Basis: HEUTE()).",
        "6. Status je Disziplin pflegen; der Fortschrittsbalken zeigt den Bearbeitungsstand. Abschluss erst nach "
        "Wirksamkeitsnachweis (D6) und Kundenbestätigung (D8).",
    ]
    for s in steps:
        put(ws, r, 2, 3, s, border=None)
        ws.row_dimensions[r].height = 30
        r += 1
    r += 1
    r = section(ws, r, "Farblegende", 4)
    legend = [
        (FILL_WHITE, F_BODY, "Weiße Felder mit Rahmen", "Eingabefelder"),
        (FILL_GREY_L, F_BODY, "Hellgraue Felder", "Formeln – nicht überschreiben"),
        (FILL_EX, F_EX, BEISPIEL, "Fiktives Beispiel (grau, kursiv) – vor Nutzung löschen bzw. "
                                 "Beispielspalte ignorieren"),
        (RED[0], RED[1], "überfällig", "Termin überschritten"),
        (YEL[0], YEL[1], "fällig ≤ 7 T", "Termin in den nächsten 7 Tagen oder kein Termin gesetzt"),
        (GRN[0], GRN[1], "im Plan / erledigt", "Alles in Ordnung"),
    ]
    for fill, font, a, b in legend:
        put(ws, r, 2, 2, a, font=font, fill=fill)
        put(ws, r, 3, 3, b)
        r += 1
    r += 1
    r = section(ws, r, "Hinweise zu Normen und Kundenformularen", 4)
    put(ws, r, 2, 3, "Die Vorlage folgt der allgemein bekannten 8D-Methode, ist aber eigenständig formuliert und "
        "gestaltet. Sie enthält keine Normtexte und bildet keine offiziellen Formblätter (z. B. von VDA, AIAG oder "
        "einzelnen Kunden) nach. Schreibt Ihr Kunde ein eigenes 8D-Formular oder eigene Fristen vor, haben diese "
        "Vorrang – übertragen Sie die Inhalte dann in das Kundenformular.", border=None)
    ws.row_dimensions[r].height = 58
    r += 2
    r = section(ws, r, "Lizenzhinweis", 4)
    put(ws, r, 2, 3, f"© 2026 {ANBIETER}. Kostenlose Nutzung für eigene Zwecke im eigenen Unternehmen "
        "(beliebig viele Kopien für interne Reklamationen). Nicht gestattet: Weiterverkauf, Weitergabe der Datei an "
        "Dritte, Veröffentlichung oder Einbindung in eigene Produkte/Downloads. Ausgefüllte Reports dürfen Sie "
        "selbstverständlich an Ihre Kunden und Lieferanten senden.", border=None)
    ws.row_dimensions[r].height = 58
    r += 2
    r = section(ws, r, "Haftungsausschluss", 4)
    put(ws, r, 2, 3, "Diese Vorlage ist eine Arbeitshilfe und ersetzt keine fachliche Beratung, keine "
        "Kundenanforderung und keine Norm. Sie wurde sorgfältig erstellt und getestet (Excel-kompatibel, "
        "LibreOffice); eine Gewähr für Vollständigkeit, Richtigkeit und Eignung für Ihren Einzelfall wird nicht "
        "übernommen. Prüfen Sie Ergebnisse und Formeln eigenverantwortlich. Die Haftung ist – soweit gesetzlich "
        "zulässig – auf Vorsatz und grobe Fahrlässigkeit beschränkt.", border=None)
    ws.row_dimensions[r].height = 58
    r += 2
    put(ws, r, 2, 3, "Keine Makros · keine externen Verknüpfungen · Funktionsumfang: Excel 2010+, LibreOffice Calc, "
        "Google Sheets (Darstellung kann abweichen).", font=F_HINT, border=None)
    page(ws)


def build_8d(wb):
    ws = wb.create_sheet("8D-Report")
    LC = 8
    widths(ws, [8, 24, 24, 22, 16, 15, 15, 18])
    title(ws, "8D-Report", LC, "Weiße Felder ausfüllen · hellgrau = Formel · grau-kursiv = fiktives Beispiel. "
          "Leitfragen stehen unter jeder Disziplin.")
    ws.freeze_panes = "A3"
    r = 4

    # Kopfdaten
    r = section(ws, r, "Kopfdaten", LC)
    spans = [(1, 2, "Feld"), (3, 5, "Eintrag"), (6, 8, "Beispiel (fiktiv)")]
    header(ws, r, spans, 20)
    r += 1
    kopf = [
        ("8D-Nr.", "8D-2026-017", None),
        ("Datum Eröffnung", "04.11.2026", DATE_FMT),
        ("Kunde", "Muster GmbH (fiktiv)", None),
        ("Reklamationsnr. Kunde", "QR-55871", None),
        ("Lieferant", "Beispiel-Druckguss GmbH (fiktiv)", None),
        ("Lieferanten-Nr.", "L-1042", None),
        ("Teilenummer", "TN 100-2034", None),
        ("Teilebezeichnung", "Halter, Aluminium-Druckguss", None),
        ("Fehlerbezeichnung (kurz)", "Gewindebohrung M6 fehlt", None),
        ("Betroffene Menge", "12 von 2.400 Teilen (Lieferung vom 03.11.2026)", None),
        ("Erstmeldung am", "03.11.2026", DATE_FMT),
        ("Ansprechpartner (Name, E-Mail)", "M. Beispiel, qs@beispiel-druckguss.invalid", None),
    ]
    kopf_rows = {}
    for label, ex, fmt in kopf:
        put(ws, r, 1, 2, label, font=F_BOLD, fill=FILL_GREY_L)
        put(ws, r, 3, 5, None, fmt=fmt, fill=FILL_WHITE)
        put(ws, r, 6, 8, ex, font=F_EX, fill=FILL_EX)
        if fmt:
            dv_date(ws, f"C{r}")
        kopf_rows[label] = r
        r += 1
    r += 1

    # Statusübersicht
    r = section(ws, r, "Statusübersicht D0–D8 und Fortschritt", LC,
                "Status je Disziplin pflegen. Terminampel: überfällig = Soll-Termin < HEUTE(); fällig ≤ 7 T = in den "
                "nächsten 7 Tagen. Orientierung (kundenabhängig, keine Normvorgabe): D3 oft binnen 24 h, D4/D5 oft "
                "binnen 10 Arbeitstagen – maßgeblich sind die Vorgaben Ihres Kunden.")
    spans = [(1, 1, "Disziplin"), (2, 3, "Bezeichnung"), (4, 4, "Verantwortlich"), (5, 5, "Soll-Termin"),
             (6, 6, "Erledigt am"), (7, 7, "Status"), (8, 8, "Terminampel")]
    header(ws, r, spans, 22)
    r += 1
    disz = [("D0", "Notfall-/Sofortreaktion (optional)"), ("D1", "Team"), ("D2", "Problembeschreibung"),
            ("D3", "Sofortmaßnahmen"), ("D4", "Ursachen (Auftreten + Nichtentdeckung)"),
            ("D5", "Abstellmaßnahmen geplant"), ("D6", "Umsetzung & Wirksamkeitsnachweis"),
            ("D7", "Wiederholung verhindern / Lessons Learned"), ("D8", "Abschluss & Würdigung")]
    s_first = r
    for d, name in disz:
        put(ws, r, 1, 1, d, font=F_BOLD, fill=FILL_GREY_L, align=WRAP_C)
        put(ws, r, 2, 3, name, fill=FILL_GREY_L)
        put(ws, r, 4, 4, None)
        put(ws, r, 5, 5, None, fmt=DATE_FMT)
        put(ws, r, 6, 6, None, fmt=DATE_FMT)
        put(ws, r, 7, 7, None, align=WRAP_C)
        put(ws, r, 8, 8, f'=IF(G{r}="erledigt","erledigt",IF(G{r}="n. a.","–",IF(E{r}="","kein Termin",'
                         f'IF(E{r}<TODAY(),"überfällig",IF(E{r}<=TODAY()+7,"fällig ≤ 7 T","im Plan")))))',
            fill=FILL_GREY_L, align=WRAP_C)
        r += 1
    s_last = r - 1
    dv_list(ws, L_STATUS8D, f"G{s_first}:G{s_last}")
    dv_date(ws, f"E{s_first}:F{s_last}")
    cf_text(ws, f"H{s_first}:H{s_last}", f"H{s_first}", AMPEL_MAP)
    # Fortschritt
    put(ws, r, 1, 3, "Fortschritt (erledigt / anwendbare Disziplinen)", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 4, 4, f'=IFERROR(COUNTIF(G{s_first}:G{s_last},"erledigt")/(9-COUNTIF(G{s_first}:G{s_last},"n. a.")),0)',
        font=F_BOLD, fill=FILL_GREY_L, align=WRAP_C, fmt="0%")
    put(ws, r, 5, 6, f'=REPT("■",ROUND(D{r}*10,0))&REPT("□",10-ROUND(D{r}*10,0))',
        font=Font(name="Calibri", size=12, color=NAVY), fill=FILL_GREY_L, align=WRAP_C)
    put(ws, r, 7, 8, f'=COUNTIF(G{s_first}:G{s_last},"erledigt")&" von "&(9-COUNTIF(G{s_first}:G{s_last},"n. a."))'
                     f'&" erledigt"', fill=FILL_GREY_L, align=WRAP_C)
    ws.conditional_formatting.add(f"D{r}", DataBarRule(start_type="num", start_value=0, end_type="num",
                                                       end_value=1, color="2F5597"))
    prog_row = r
    r += 2

    # D0
    r = section(ws, r, "D0 – Notfall-/Sofortreaktion (optional)", LC,
                "Muss sofort etwas gestoppt, gesperrt oder gemeldet werden? Besteht Sicherheits- oder "
                "Gesetzesrelevanz? Falls D0 nicht nötig: Status „n. a.“ setzen.")
    put(ws, r, 1, 2, "Notfallreaktion erforderlich?", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 3, 3, None)
    dv_list(ws, L_JNU, f"C{r}")
    put(ws, r, 4, 5, "Sicherheits-/Gesetzesrelevanz?", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 6, 6, None)
    dv_list(ws, L_JNU, f"F{r}")
    put(ws, r, 7, 7, "Kunde informiert am", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 8, 8, None, fmt=DATE_FMT)
    dv_date(ws, f"H{r}")
    r += 1
    put(ws, r, 1, 2, "Beschreibung Notfallreaktion", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 3, 8, None)
    ws.row_dimensions[r].height = 45
    r += 2

    # D1
    r = section(ws, r, "D1 – Team", LC,
                "Wer hat Fachwissen über Produkt und Prozess, Entscheidungsbefugnis und Zeit? Ein Teamleiter, "
                "ein Sponsor mit Budgetverantwortung; Kunde/Lieferant bei Bedarf einbeziehen.")
    spans = [(1, 1, "Nr"), (2, 2, "Name"), (3, 3, "Funktion / Abteilung"), (4, 4, "Rolle"),
             (5, 8, "Kontakt (Telefon, E-Mail)")]
    header(ws, r, spans, 20)
    r += 1
    t_first = r
    body_row(ws, r, spans, {1: BEISPIEL, 2: "A. Muster", 3: "Qualitätsleitung", 4: "Teamleiter",
                            5: "+49 000 000000, a.muster@beispiel.invalid"})
    r += 1
    for i in range(6):
        body_row(ws, r, spans, {1: i + 1})
        r += 1
    dv_list(ws, L_ROLLE, f"D{t_first}:D{r - 1}")
    cf_example(ws, f"A{t_first}:H{r - 1}", f"$A{t_first}")
    r += 1

    # D2
    r = section(ws, r, "D2 – Problembeschreibung", LC,
                "Beschreiben Sie das Fehlerbild aus Kundensicht – messbar und ohne die Ursache vorwegzunehmen. "
                "Kann jemand Fremdes das Problem anhand Ihrer Beschreibung wiedererkennen?")
    put(ws, r, 1, 2, "Fehlerbild aus Kundensicht", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 3, 8, None)
    ws.row_dimensions[r].height = 45
    d2_row = r
    r += 2
    spans = [(1, 1, "5W2H"), (2, 3, "Leitfrage"), (4, 6, "Antwort"), (7, 8, "Beispiel (fiktiv)")]
    header(ws, r, spans, 20)
    r += 1
    w5 = [("Was?", "Welches Teil, welcher Fehler, welches Merkmal ist betroffen?", "TN 100-2034: Gewindebohrung M6 an "
           "Lasche 2 nicht vorhanden"),
          ("Wo?", "Wo wurde der Fehler entdeckt, wo am Teil tritt er auf?", "Montagelinie Muster GmbH, Station 3"),
          ("Wann?", "Seit wann? Welche Lieferung, Charge, Schicht, Fertigungsdatum?", "Lieferung 03.11.2026, "
           "Fertigungslos 26-44-B (Spätschicht)"),
          ("Wer?", "Wer hat den Fehler entdeckt bzw. ist betroffen?", "Werker beim Verschrauben"),
          ("Warum relevant?", "Welche Auswirkung hat der Fehler für den Kunden?", "Teil nicht montierbar, "
           "Linienstopp 20 Min."),
          ("Wie?", "Wie wurde der Fehler festgestellt (Methode, Prüfmittel)?", "Schraube nicht eindrehbar, "
           "Sichtprüfung bestätigt"),
          ("Wie viele?", "Wie viele Teile, welcher Anteil, Tendenz?", "12 von 2.400 Teilen (0,5 %)")]
    for q, lf, ex in w5:
        put(ws, r, 1, 1, q, font=F_BOLD, fill=FILL_GREY_L)
        put(ws, r, 2, 3, lf, font=F_HINT, fill=FILL_GREY_L)
        put(ws, r, 4, 6, None)
        put(ws, r, 7, 8, ex, font=F_EX, fill=FILL_EX)
        ws.row_dimensions[r].height = 30
        r += 1
    r += 1
    spans = [(1, 2, "Merkmal"), (3, 4, "IST betroffen"), (5, 6, "IST NICHT betroffen (obwohl möglich)"),
             (7, 8, "Unterschied / Auffälligkeit")]
    header(ws, r, spans, 30)
    r += 1
    t_first = r
    body_row(ws, r, spans, {1: f"{BEISPIEL}: Wann", 3: "Los 26-44-B (Spätschicht)",
                            5: "Lose 26-44-A und 26-45-A (Frühschicht)", 7: "Werkzeugwechsel nach Wartung "
                                                                          "in der Spätschicht"}, height=30)
    r += 1
    for m in ["Was (Objekt / Fehler)", "Wo (Ort am Teil / im Prozess)", "Wann (Zeitpunkt / Los)",
              "Ausmaß (Menge / Trend)"]:
        body_row(ws, r, spans, {1: m}, height=30)
        r += 1
    cf_example(ws, f"A{t_first}:H{r - 1}", f"$A{t_first}")
    r += 1

    # D3
    r = section(ws, r, "D3 – Sofortmaßnahmen (Kunde schützen)", LC,
                "Ist der Kunde ab sofort geschützt? Sind alle Bestände erfasst – auch Transit, Lager und "
                "Unterlieferant? Wie sind geprüfte Teile gekennzeichnet? Wie ist die Wirksamkeit belegt?")
    spans = [(1, 1, "Nr"), (2, 2, "Maßnahme"), (3, 3, "Ort"), (4, 4, "Verantwortlich"), (5, 5, "Termin"),
             (6, 6, "Status"), (7, 7, "Wirksamkeit belegt durch"), (8, 8, "Wirksam?")]
    header(ws, r, spans, 30)
    r += 1
    t_first = r
    body_row(ws, r, spans, {1: BEISPIEL, 2: "100-%-Sortierung aller Bestände mit Gewindelehrdorn", 3: "Kunde",
                            4: "M. Beispiel", 5: dt.date(2026, 11, 4), 6: "erledigt",
                            7: "Sortierprotokoll, 0 Fehler in Folgelieferungen", 8: "ja"},
             height=30, fmts={5: DATE_FMT})
    r += 1
    for i in range(6):
        body_row(ws, r, spans, {1: i + 1}, fmts={5: DATE_FMT})
        r += 1
    dv_list(ws, L_ORT, f"C{t_first}:C{r - 1}")
    dv_date(ws, f"E{t_first}:E{r - 1}")
    dv_list(ws, L_STATUS, f"F{t_first}:F{r - 1}")
    dv_list(ws, L_JNO, f"H{t_first}:H{r - 1}")
    cf_example(ws, f"A{t_first}:H{r - 1}", f"$A{t_first}")
    r += 1
    spans = [(1, 2, "Bestand / Ort"), (3, 3, "Menge geprüft"), (4, 4, "davon n.i.O."), (5, 6, "Prüfmethode"),
             (7, 8, "Kennzeichnung i.O.-Teile")]
    header(ws, r, spans, 20)
    r += 1
    b_first = r
    for o in ["Beim Kunden", "Transit / unterwegs", "Fertigwarenlager Lieferant", "In Fertigung (WIP)",
              "Unterlieferant"]:
        body_row(ws, r, spans, {1: o}, fmts={3: "#,##0", 4: "#,##0"})
        r += 1
    put(ws, r, 1, 2, "Summe", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 3, 3, f"=SUM(C{b_first}:C{r - 1})", font=F_BOLD, fill=FILL_GREY_L, fmt="#,##0")
    put(ws, r, 4, 4, f"=SUM(D{b_first}:D{r - 1})", font=F_BOLD, fill=FILL_GREY_L, fmt="#,##0")
    put(ws, r, 5, 8, f'=IF(C{r}=0,"",TEXT(D{r}/C{r}*1000000,"#,##0")&" ppm in geprüften Beständen")',
        fill=FILL_GREY_L)
    r += 2

    # D4
    r = section(ws, r, "D4 – Ursachen: Auftreten UND Nichtentdeckung", LC,
                "Lässt sich der Fehler mit der Ursache gezielt erzeugen und abstellen (verifiziert)? Warum hat "
                "die Prüfung den Fehler nicht erkannt? Analyse auf den Blättern 5-Why und Ishikawa.")
    for txt, sheet in [("→ zur 5-Why-Analyse", "5-Why"), ("→ zur Ishikawa-Analyse", "Ishikawa")]:
        c = ws.cell(row=r, column=2 if sheet == "5-Why" else 4, value=txt)
        c.hyperlink = Hyperlink(ref=c.coordinate, location=f"'{sheet}'!A1")
        c.font = F_LINK
    r += 1
    for kind, ex in [("Auftreten – warum ist der Fehler entstanden?",
                      {2: "Bohrer gebrochen; Werkzeugbruchkontrolle nach Wartung nicht wieder aktiviert",
                       4: "Maschinenprotokoll, Nachstellversuch: ohne Kontrolle läuft Zyklus weiter",
                       6: "ja", 7: "Hauptursache"}),
                     ("Nichtentdeckung – warum wurde der Fehler nicht entdeckt?",
                      {2: "Endprüfung nur als Stichprobe 1×/Schicht; fehlendes Gewinde bei Sichtprüfung "
                          "im Durchlauf nicht erkennbar",
                       4: "Prüfplan Rev. C, Prüfaufzeichnungen KW 44",
                       6: "ja", 7: "Hauptursache"})]:
        put(ws, r, 1, LC, kind, font=F_BOLD, fill=FILL_GREY_M, border=BORDER)
        r += 1
        spans = [(1, 1, "Nr"), (2, 3, "Ursache"), (4, 5, "Nachweis / Verifizierung"), (6, 6, "verifiziert?"),
                 (7, 8, "Anteil / Bemerkung")]
        header(ws, r, spans, 20)
        r += 1
        t_first = r
        ex[1] = BEISPIEL
        body_row(ws, r, spans, ex, height=30)
        r += 1
        for i in range(4):
            body_row(ws, r, spans, {1: i + 1}, height=24)
            r += 1
        dv_list(ws, L_JNO, f"F{t_first}:F{r - 1}")
        cf_example(ws, f"A{t_first}:H{r - 1}", f"$A{t_first}")
        r += 1

    # D5
    r = section(ws, r, "D5 – Abstellmaßnahmen geplant", LC,
                "Wirkt jede Maßnahme auf eine verifizierte Ursache aus D4 – für Auftreten UND Nichtentdeckung? "
                "Wurden Risiken/Nebenwirkungen geprüft? Alle Maßnahmen auch im Maßnahmentracker führen.")
    spans = [(1, 1, "Nr"), (2, 2, "Bezug Ursache"), (3, 4, "Maßnahme"), (5, 5, "Verantwortlich"),
             (6, 6, "Termin geplant"), (7, 7, "Risiko geprüft?"), (8, 8, "Nr. im Tracker")]
    header(ws, r, spans, 30)
    r += 1
    t_first = r
    body_row(ws, r, spans, {1: BEISPIEL, 2: "Auftreten", 3: "Werkzeugbruchkontrolle verriegeln; Freigabe nach "
                            "Wartung nur mit Checkliste und Unterschrift", 5: "Instandhaltung", 6: dt.date(2026, 11, 15),
                            7: "ja", 8: "2"}, height=30, fmts={6: DATE_FMT})
    r += 1
    for i in range(6):
        body_row(ws, r, spans, {1: i + 1}, fmts={6: DATE_FMT})
        r += 1
    dv_list(ws, L_URS, f"B{t_first}:B{r - 1}")
    dv_date(ws, f"F{t_first}:F{r - 1}")
    dv_list(ws, L_JNNA, f"G{t_first}:G{r - 1}")
    cf_example(ws, f"A{t_first}:H{r - 1}", f"$A{t_first}")
    r += 1

    # D6
    r = section(ws, r, "D6 – Umsetzung & Wirksamkeitsnachweis", LC,
                "Woran sehen Sie objektiv, dass der Fehler nicht mehr auftritt und entdeckt würde (Daten, Lose, "
                "Prüfergebnisse)? Sofortmaßnahmen erst nach Wirksamkeitsnachweis aufheben.")
    spans = [(1, 1, "Nr"), (2, 3, "Maßnahme"), (4, 4, "Umgesetzt am"), (5, 6, "Wirksamkeitsnachweis"),
             (7, 7, "Wirksam?"), (8, 8, "Sofortmaßn. aufgehoben am")]
    header(ws, r, spans, 30)
    r += 1
    t_first = r
    body_row(ws, r, spans, {1: BEISPIEL, 2: "Werkzeugbruchkontrolle verriegelt", 4: dt.date(2026, 11, 14),
                            5: "10 Lose ohne Befund; Bruchsimulation stoppt Maschine (Test 3/3 i.O.)", 7: "ja",
                            8: dt.date(2026, 12, 1)}, height=30, fmts={4: DATE_FMT, 8: DATE_FMT})
    r += 1
    for i in range(6):
        body_row(ws, r, spans, {1: i + 1}, fmts={4: DATE_FMT, 8: DATE_FMT})
        r += 1
    dv_date(ws, f"D{t_first}:D{r - 1}")
    dv_date(ws, f"H{t_first}:H{r - 1}")
    dv_list(ws, L_JNO, f"G{t_first}:G{r - 1}")
    cf_example(ws, f"A{t_first}:H{r - 1}", f"$A{t_first}")
    r += 1

    # D7
    r = section(ws, r, "D7 – Wiederholung verhindern / Lessons Learned", LC,
                "Wo könnte derselbe Fehler noch auftreten (ähnliche Teile, Maschinen, Standorte)? Welche "
                "Dokumente müssen angepasst werden, damit das Wissen nicht verloren geht?")
    spans = [(1, 3, "Prüfpunkt"), (4, 4, "Erledigt?"), (5, 6, "Dokument / Nr."), (7, 8, "Bemerkung")]
    header(ws, r, spans, 20)
    r += 1
    t_first = r
    for p in ["FMEA aktualisiert (Auftreten / Entdeckung neu bewertet)", "Produktionslenkungsplan / Prüfplan angepasst",
              "Arbeits- und Prüfanweisungen angepasst", "Mitarbeitende unterwiesen (Nachweis)",
              "Übertrag auf ähnliche Produkte / Prozesse / Standorte geprüft", "Lessons Learned dokumentiert und geteilt"]:
        put(ws, r, 1, 3, p, fill=FILL_GREY_L)
        put(ws, r, 4, 4, None, align=WRAP_C)
        put(ws, r, 5, 6, None)
        put(ws, r, 7, 8, None)
        r += 1
    dv_list(ws, L_JNNA, f"D{t_first}:D{r - 1}")
    cf_text(ws, f"D{t_first}:D{r - 1}", f"D{t_first}", {"ja": GRN, "nein": RED, "n. a.": GRY})
    r += 1

    # D8
    r = section(ws, r, "D8 – Abschluss & Würdigung", LC,
                "Sind alle Maßnahmen wirksam und dokumentiert? Hat der Kunde den Abschluss bestätigt? Wurde die "
                "Leistung des Teams gewürdigt?")
    put(ws, r, 1, 2, "Abschlussdatum", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 3, 3, None, fmt=DATE_FMT)
    dv_date(ws, f"C{r}")
    put(ws, r, 4, 4, "Abschluss durch", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 5, 6, None)
    put(ws, r, 7, 7, "Kunde bestätigt?", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 8, 8, None, align=WRAP_C)
    dv_list(ws, L_JNO, f"H{r}")
    r += 1
    put(ws, r, 1, 2, "Würdigung des Teams / Abschlussbemerkung", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 3, 8, None)
    ws.row_dimensions[r].height = 45
    page(ws, print_rows="1:2", area=f"A1:H{r}")
    return {"fehler_row": kopf_rows["Fehlerbezeichnung (kurz)"], "d2_row": d2_row,
            "status_first": s_first, "status_last": s_last, "prog_row": prog_row}


def build_5why(wb, refs):
    ws = wb.create_sheet("5-Why")
    LC = 6
    widths(ws, [8, 30, 36, 28, 12, 40])
    title(ws, "5-Why-Analyse – zwei Pfade: Auftreten und Nichtentdeckung", LC,
          "Fragen Sie so lange „Warum?“, bis Sie eine abstellbare, mit Fakten belegte Ursache erreichen – das kann "
          "vor oder nach dem 5. Warum sein. „Mitarbeiter hat nicht aufgepasst“ ist keine Grundursache.")
    ws.freeze_panes = "A3"
    r = 4
    fr = refs["fehler_row"]
    put(ws, r, 1, 2, "Problem (aus 8D-Report, überschreibbar)", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, r, 3, 6, f"=IF('8D-Report'!C{fr}=\"\",\"(Fehlerbezeichnung im 8D-Report eintragen)\","
                     f"'8D-Report'!C{fr})", fill=FILL_GREY_L)
    r += 2
    paths = [
        ("Pfad A – Warum ist der Fehler AUFGETRETEN?", "Grundursache Auftreten", [
            "Warum fehlt das Gewinde? → Weil die Bohrung M6 nicht gebohrt wurde.",
            "Warum wurde nicht gebohrt? → Weil der Bohrer gebrochen war.",
            "Warum lief die Maschine mit gebrochenem Bohrer weiter? → Weil die Werkzeugbruchkontrolle aus war.",
            "Warum war die Kontrolle aus? → Weil sie nach der Wartung nicht wieder aktiviert wurde.",
            "Warum nicht wieder aktiviert? → Weil die Wiederinbetriebnahme nach Wartung keinen Prüfschritt dafür "
            "vorsieht. ← Grundursache"]),
        ("Pfad B – Warum wurde der Fehler NICHT ENTDECKT?", "Grundursache Nichtentdeckung", [
            "Warum wurde das fehlende Gewinde nicht entdeckt? → Weil die Endprüfung es nicht erfasst hat.",
            "Warum nicht erfasst? → Weil das Gewinde nur per Stichprobe 1×/Schicht geprüft wird.",
            "Warum nur Stichprobe? → Weil das Merkmal im Prüfplan als „unkritisch“ eingestuft war.",
            "Warum unkritisch? → Weil Werkzeugbruch in der FMEA als „nicht möglich“ bewertet war "
            "(Bruchkontrolle vorausgesetzt). ← Grundursache",
            "(Kette endet hier – 5 Warums sind kein Muss.)"]),
    ]
    root_rows = []
    for head_txt, root_label, chain in paths:
        r = section(ws, r, head_txt, LC)
        spans = [(1, 1, "Nr"), (2, 2, "Warum …? (Frage)"), (3, 3, "Weil … (Antwort)"), (4, 4, "Nachweis / Fakt"),
                 (5, 5, "verifiziert?"), (6, 6, "Beispiel (fiktiv) – nur zur Orientierung")]
        header(ws, r, spans, 30)
        r += 1
        first = r
        for i, ex in enumerate(chain, start=1):
            put(ws, r, 1, 1, f"Warum {i}", font=F_BOLD, fill=FILL_GREY_L, align=WRAP_C)
            put(ws, r, 2, 2, None)
            put(ws, r, 3, 3, None)
            put(ws, r, 4, 4, None)
            put(ws, r, 5, 5, None, align=WRAP_C)
            put(ws, r, 6, 6, ex, font=F_EX, fill=FILL_EX)
            ws.row_dimensions[r].height = 45
            r += 1
        dv_list(ws, L_JNO, f"E{first}:E{r - 1}")
        cf_text(ws, f"E{first}:E{r - 1}", f"E{first}", {"ja": GRN, "nein": RED, "offen": YEL})
        put(ws, r, 1, 2, root_label, font=F_BOLD, fill=FILL_GREY_M)
        put(ws, r, 3, 5, None)
        put(ws, r, 6, 6, chain[-1].split("→ ")[-1] if "←" in chain[-1] else chain[-2].split("→ ")[-1],
            font=F_EX, fill=FILL_EX)
        ws.row_dimensions[r].height = 45
        root_rows.append(r)
        r += 1
        c = ws.cell(row=r, column=3, value="→ verifizierte Grundursache in D4 des 8D-Reports übertragen")
        c.hyperlink = Hyperlink(ref=c.coordinate, location="'8D-Report'!A1")
        c.font = F_LINK
        r += 2
    page(ws, print_rows="1:2", area=f"A1:F{r}")


def build_ishikawa(wb, refs):
    ws = wb.create_sheet("Ishikawa")
    LC = 7
    widths(ws, [14, 18, 40, 18, 34, 18, 18])
    title(ws, "Ishikawa – Ursachensammlung nach 6M (Tabellenform)", LC,
          "Erst sammeln (Brainstorming im Team), dann jede mögliche Ursache prüfen und bewerten. Bestätigte "
          "Ursachen in D4 übertragen. Die graue Beispielzeile zählt in der Übersicht mit, bis Sie sie löschen.")
    fr = refs["fehler_row"]
    put(ws, 3, 1, 2, "Wirkung / Problem", font=F_BOLD, fill=FILL_GREY_L)
    put(ws, 3, 3, 7, f"=IF('8D-Report'!C{fr}=\"\",\"(Fehlerbezeichnung im 8D-Report eintragen)\","
                     f"'8D-Report'!C{fr})", fill=FILL_GREY_L)
    # 6M-Übersicht (Matrix): Label in A, Kategorien in B–G
    put(ws, 4, 1, 1, "Kennzahl", font=F_HEAD, fill=FILL_SLATE, align=WRAP_C)
    for i, m in enumerate(L_6M):
        put(ws, 4, 2 + i, 2 + i, m, font=F_HEAD, fill=FILL_SLATE, align=WRAP_C)
    hints = ["Qualifikation, Einweisung, Belastung, Schichtwechsel",
             "Werkzeug, Verschleiß, Einstellung, Wartung, Überwachung",
             "Arbeitsanweisung, Reihenfolge, Prüfplan, Parameter",
             "Rohmaterial, Zukaufteile, Charge, Lagerung",
             "Prüfmittel, Messmethode, Kalibrierung, Prüfumfang",
             "Temperatur, Sauberkeit, Licht, Vibration, Feuchte"]
    put(ws, 5, 1, 1, "Denkanstöße", font=F_BOLD, fill=FILL_GREY_L, align=WRAP_C)
    for i, h in enumerate(hints):
        put(ws, 5, 2 + i, 2 + i, h, font=F_HINT, fill=FILL_GREY_L)
    ws.row_dimensions[5].height = 48
    T_FIRST, T_LAST = 10, 10 + 60
    kpis = [("Anzahl", None), ("bestätigt", "bestätigt"), ("wahrscheinlich", "wahrscheinlich"),
            ("ausgeschl.", "ausgeschlossen")]
    for j, (lab, crit) in enumerate(kpis):
        rr = 6 + j
        put(ws, rr, 1, 1, lab, font=F_BOLD, fill=FILL_GREY_L, align=WRAP_C)
        for i, m in enumerate(L_6M):
            col = get_column_letter(2 + i)
            rng_k = f"$B${T_FIRST + 1}:$B${T_LAST}"
            rng_b = f"$D${T_FIRST + 1}:$D${T_LAST}"
            if crit is None:
                f = f'=COUNTIF({rng_k},{col}$4)'
            else:
                f = f'=COUNTIFS({rng_k},{col}$4,{rng_b},"{crit}")'
            put(ws, rr, 2 + i, 2 + i, f, fill=FILL_GREY_L, align=WRAP_C)
    ws.conditional_formatting.add("B7:G7", FormulaRule(formula=["B7>0"], fill=RED[0], font=RED[1]))
    ws.conditional_formatting.add("B8:G8", FormulaRule(formula=["B8>0"], fill=YEL[0], font=YEL[1]))
    # Tabelle
    r = T_FIRST
    spans = [(1, 1, "Nr"), (2, 2, "6M-Kategorie"), (3, 3, "Mögliche Ursache"), (4, 4, "Bewertung"),
             (5, 5, "Prüfung / Nachweis"), (6, 6, "Verantwortlich"), (7, 7, "Termin")]
    header(ws, r, spans, 22)
    ws.freeze_panes = f"A{T_FIRST + 1}"
    r += 1
    body_row(ws, r, spans, {1: BEISPIEL, 2: "Maschine", 3: "Werkzeugbruchkontrolle deaktiviert",
                            4: "bestätigt", 5: "Maschinenlog, Nachstellversuch", 6: "Instandhaltung",
                            7: dt.date(2026, 11, 6)}, fmts={7: DATE_FMT}, height=30)
    r += 1
    while r <= T_LAST:
        body_row(ws, r, spans, {1: f'=IF(C{r}="","",COUNTA($C${T_FIRST + 2}:C{r}))'}, fmts={7: DATE_FMT})
        ws.cell(row=r, column=1).fill = FILL_GREY_L
        r += 1
    dv_list(ws, L_6M, f"B{T_FIRST + 1}:B{T_LAST}")
    dv_list(ws, L_BEW, f"D{T_FIRST + 1}:D{T_LAST}")
    dv_date(ws, f"G{T_FIRST + 1}:G{T_LAST}")
    cf_example(ws, f"A{T_FIRST + 1}:G{T_LAST}", f"$A{T_FIRST + 1}")
    cf_text(ws, f"D{T_FIRST + 1}:D{T_LAST}", f"D{T_FIRST + 1}",
            {"bestätigt": RED, "wahrscheinlich": YEL, "ausgeschlossen": GRY})
    page(ws, print_rows=f"{T_FIRST}:{T_FIRST}", area=f"A1:G{T_LAST}")


def build_tracker(wb):
    ws = wb.create_sheet("Maßnahmentracker")
    LC = 12
    widths(ws, [10, 10, 40, 18, 18, 12, 12, 12, 12, 14, 10, 30])
    title(ws, "Maßnahmentracker", LC, "Alle Maßnahmen aus D3, D5, D6 und D7 an einer Stelle. Ampel auf Basis "
          "HEUTE(): überfällig (rot), fällig ≤ 7 T / kein Termin (gelb), im Plan / erledigt (grün).")
    H, FIRST, LAST = 4, 5, 105
    rng = lambda col: f"${col}${FIRST}:${col}${LAST}"  # noqa: E731
    excl = f'{rng("A")},"<>{BEISPIEL}"'
    kpi = [("offen / in Arbeit", f'=COUNTIFS({rng("G")},"offen",{excl})+COUNTIFS({rng("G")},"in Arbeit",{excl})'),
           ("überfällig", f'=COUNTIFS({rng("J")},"überfällig",{excl})'),
           ("fällig ≤ 7 T", f'=COUNTIFS({rng("J")},"fällig ≤ 7 T",{excl})'),
           ("erledigt", f'=COUNTIFS({rng("G")},"erledigt",{excl})')]
    c = 1
    for lab, f in kpi:
        put(ws, 3, c, c + 1, lab, font=F_BOLD, fill=FILL_GREY_L, align=WRAP_C)
        put(ws, 3, c + 2, c + 2, f, font=F_BOLD, fill=FILL_GREY_L, align=WRAP_C)
        c += 3
    ws.conditional_formatting.add("F3", FormulaRule(formula=["F3>0"], fill=RED[0], font=RED[1]))
    ws.row_dimensions[3].height = 22
    spans = [(1, 1, "Nr"), (2, 2, "8D-Bezug"), (3, 3, "Maßnahme"), (4, 4, "Art"), (5, 5, "Verantwortlich"),
             (6, 6, "Termin"), (7, 7, "Status"), (8, 8, "Erledigt am"), (9, 9, "Wirksamkeit geprüft"),
             (10, 10, "Ampel"), (11, 11, "Tage überfällig"), (12, 12, "Bemerkung")]
    header(ws, H, spans, 30)
    ws.freeze_panes = f"A{FIRST}"
    ws.auto_filter.ref = f"A{H}:L{LAST}"
    for r in range(FIRST, LAST + 1):
        if r == FIRST:
            vals = {1: BEISPIEL, 2: "D5", 3: "Werkzeugbruchkontrolle verriegeln, Wartungs-Checkliste ergänzen",
                    4: "Abstellmaßnahme", 5: "Instandhaltung", 6: dt.date(2026, 11, 10), 7: "in Arbeit",
                    9: "offen", 12: "Beispiel zeigt Ampel „überfällig“"}
        else:
            vals = {1: f'=IF(C{r}="","",COUNTA($C${FIRST + 1}:C{r}))'}
        vals[10] = (f'=IF(C{r}="","",IF(G{r}="erledigt","erledigt",IF(G{r}="verworfen","verworfen",'
                    f'IF(F{r}="","kein Termin",IF(F{r}<TODAY(),"überfällig",IF(F{r}<=TODAY()+7,"fällig ≤ 7 T",'
                    f'"im Plan"))))))')
        vals[11] = f'=IF(J{r}="überfällig",TODAY()-F{r},"")'
        body_row(ws, r, spans, vals, fmts={6: DATE_FMT, 8: DATE_FMT, 11: "0"})
        for col in (1, 10, 11):
            ws.cell(row=r, column=col).fill = FILL_GREY_L
            ws.cell(row=r, column=col).alignment = WRAP_C
    dv_list(ws, L_BEZUG, f"B{FIRST}:B{LAST}")
    dv_list(ws, L_ART, f"D{FIRST}:D{LAST}")
    dv_date(ws, f"F{FIRST}:F{LAST}")
    dv_list(ws, L_STATUS, f"G{FIRST}:G{LAST}")
    dv_date(ws, f"H{FIRST}:H{LAST}")
    dv_list(ws, L_JNO, f"I{FIRST}:I{LAST}")
    cf_example(ws, f"A{FIRST}:I{LAST}", f"$A{FIRST}")
    cf_example(ws, f"K{FIRST}:L{LAST}", f"$A{FIRST}")
    cf_text(ws, f"J{FIRST}:J{LAST}", f"J{FIRST}", AMPEL_MAP)
    page(ws, print_rows=f"{H}:{H}", area=f"A1:L{LAST}")


def build():
    os.makedirs(DIST, exist_ok=True)
    wb = Workbook()
    sheets = [("Start", "Zweck, Inhaltsverzeichnis, Kurzanleitung, Lizenz und Haftung"),
              ("8D-Report", "Kopfdaten, Statusübersicht mit Fortschritt, Disziplinen D0–D8 mit Leitfragen"),
              ("5-Why", "Ursachenanalyse in zwei Pfaden: Auftreten und Nichtentdeckung"),
              ("Ishikawa", "6M-Ursachensammlung in Tabellenform mit Bewertung und Übersicht je M"),
              ("Maßnahmentracker", "Alle Maßnahmen mit Verantwortlich, Termin, Status und Terminampel")]
    build_start(wb, sheets)
    refs = build_8d(wb)
    build_5why(wb, refs)
    build_ishikawa(wb, refs)
    build_tracker(wb)
    wb.active = 0
    props = wb.properties
    props.title = PRODUKT
    props.subject = "8D-Reklamationsbearbeitung"
    props.creator = "Vorlagen-Generator build.py"
    props.keywords = "8D, 5-Why, Ishikawa, Reklamation, Lieferantenqualität"
    props.version = VERSION
    wb.save(OUTFILE)
    print(f"gebaut: {OUTFILE}")
    return refs


# ---------------------------------------------------------------- Test
ERRORS = ("#REF!", "#NAME?", "#DIV/0!", "#VALUE!", "#N/A", "#NUM!", "#NULL!", "Err:", "#WERT!", "#BEZUG!")


def recalc(src, outdir):
    """Rechnet die Datei mit LibreOffice headless neu (Konvertierung xlsx→xlsx). Gibt Pfad oder None zurück."""
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        return None
    profile = tempfile.mkdtemp(prefix="lo_profile_")
    subprocess.run([soffice, f"-env:UserInstallation=file://{profile}", "--headless", "--calc",
                    "--convert-to", "xlsx", "--outdir", outdir, src],
                   check=True, capture_output=True, timeout=180)
    return os.path.join(outdir, os.path.basename(src))


def scan(path):
    wb = load_workbook(path, data_only=True)
    errs, n_values = [], 0
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith(ERRORS):
                    errs.append(f"{ws.title}!{c.coordinate}={c.value}")
                if c.value is not None:
                    n_values += 1
    return wb, errs, n_values


def test(refs):
    print("== Test 1: openpyxl-Neuladen")
    wb = load_workbook(OUTFILE)
    names = wb.sheetnames
    print("Blätter:", names)
    assert names == ["Start", "8D-Report", "5-Why", "Ishikawa", "Maßnahmentracker"], names
    n_f = sum(1 for ws in wb.worksheets for row in ws.iter_rows() for c in row
              if isinstance(c.value, str) and c.value.startswith("="))
    n_dv = sum(len(ws.data_validations.dataValidation) for ws in wb.worksheets)
    n_cf = sum(len(list(ws.conditional_formatting)) for ws in wb.worksheets)
    links = [c.hyperlink.location for c in wb["Start"]["B"] if c.hyperlink]
    print(f"Formeln: {n_f} · Datenvalidierungen: {n_dv} · bedingte Formatierungsbereiche: {n_cf}")
    print("Hyperlinks Start:", links)
    for ws in wb.worksheets:
        print(f"  {ws.title}: freeze={ws.freeze_panes} orient={ws.page_setup.orientation} "
              f"paper={ws.page_setup.paperSize} fitW={ws.page_setup.fitToWidth} area={ws.print_area}")
        assert ws.page_setup.orientation == "landscape" and str(ws.page_setup.paperSize) == "9"
    assert len(links) == 5
    with open(OUTFILE, "rb") as fh:
        import zipfile
        z = zipfile.ZipFile(fh)
        assert not any("vba" in n.lower() for n in z.namelist()), "Makro-Projekt gefunden!"
    print("Keine Makros (vbaProject) enthalten.")

    tmp = tempfile.mkdtemp(prefix="test8d_")
    print("== Test 2: LibreOffice-Neuberechnung (Originaldatei)")
    out = recalc(OUTFILE, tmp)
    if not out:
        print("LibreOffice nicht gefunden – Test 2/3 übersprungen.")
        return
    wbv, errs, nv = scan(out)
    print(f"Zellen mit Wert: {nv} · Fehlerwerte: {len(errs)}", errs[:20])
    tr = wbv["Maßnahmentracker"]
    print("Tracker Beispielzeile Ampel/Tage:", tr["J5"].value, tr["K5"].value, "· Zähler:",
          tr["C3"].value, tr["F3"].value, tr["I3"].value, tr["L3"].value)
    pr = refs["prog_row"]
    print("8D Fortschritt leer:", wbv["8D-Report"][f"D{pr}"].value, wbv["8D-Report"][f"E{pr}"].value)
    print("Ishikawa Anzahl Maschine:", wbv["Ishikawa"]["C6"].value)
    assert not errs

    print("== Test 3: Funktionstest mit Testdaten (Kopie)")
    wbt = load_workbook(OUTFILE)
    s = wbt["8D-Report"]
    sf = refs["status_first"]
    today = dt.date.today()
    data = [("n. a.", None), ("erledigt", today), ("erledigt", today), ("erledigt", today),
            ("in Arbeit", today - dt.timedelta(days=3)), ("offen", today + dt.timedelta(days=3)),
            ("offen", today + dt.timedelta(days=30)), ("offen", None), ("offen", None)]
    for i, (st, soll) in enumerate(data):
        s[f"G{sf + i}"] = st
        if soll:
            s[f"E{sf + i}"] = soll
            s[f"E{sf + i}"].number_format = DATE_FMT
    s[f"C{refs['fehler_row']}"] = "Testfehler"
    t = wbt["Maßnahmentracker"]
    t["C6"], t["F6"], t["G6"] = "Test überfällig", today - dt.timedelta(days=5), "offen"
    t["C7"], t["F7"], t["G7"] = "Test bald", today + dt.timedelta(days=2), "in Arbeit"
    t["C8"], t["F8"], t["G8"] = "Test erledigt", today - dt.timedelta(days=5), "erledigt"
    t["C9"], t["G9"] = "Test ohne Termin", "offen"
    t["C10"], t["F10"], t["G10"] = "Test im Plan", today + dt.timedelta(days=30), "offen"
    i = wbt["Ishikawa"]
    i["B12"], i["C12"], i["D12"] = "Messung", "Lehrdorn verschlissen", "ausgeschlossen"
    i["B13"], i["C13"], i["D13"] = "Methode", "Prüfplan Stichprobe", "bestätigt"
    tpath = os.path.join(tmp, "funktionstest.xlsx")
    wbt.save(tpath)
    out_dir2 = os.path.join(tmp, "calc")
    os.makedirs(out_dir2)
    out2 = recalc(tpath, out_dir2)
    wbv2, errs2, _ = scan(out2)
    s2, t2, i2 = wbv2["8D-Report"], wbv2["Maßnahmentracker"], wbv2["Ishikawa"]
    amp = [s2[f"H{sf + k}"].value for k in range(9)]
    prog = s2[f"D{pr}"].value
    print("Ampeln D0–D8:", amp)
    print("Fortschritt:", prog, s2[f"E{pr}"].value, s2[f"G{pr}"].value)
    tamp = [(t2[f"A{r}"].value, t2[f"J{r}"].value, t2[f"K{r}"].value) for r in range(6, 11)]
    print("Tracker:", tamp, "Zähler offen/überf./≤7/erl.:", t2["C3"].value, t2["F3"].value, t2["I3"].value,
          t2["L3"].value)
    print("5-Why Problem:", wbv2["5-Why"]["C4"].value, "· Ishikawa Methode bestätigt:", i2["D7"].value,
          "· Messung Anzahl:", i2["F6"].value)
    expect_amp = ["–", "erledigt", "erledigt", "erledigt", "überfällig", "fällig ≤ 7 T", "im Plan", "kein Termin",
                  "kein Termin"]
    assert amp == expect_amp, amp
    assert abs(prog - 3 / 8) < 1e-9, prog
    assert [x[1] for x in tamp] == ["überfällig", "fällig ≤ 7 T", "erledigt", "kein Termin", "im Plan"], tamp
    assert tamp[0][2] == 5 and [x[0] for x in tamp] == [1, 2, 3, 4, 5]
    assert (t2["C3"].value, t2["F3"].value, t2["I3"].value, t2["L3"].value) == (4, 1, 1, 1)
    assert wbv2["5-Why"]["C4"].value == "Testfehler"
    assert i2["D7"].value == 1 and i2["F6"].value == 1
    assert not errs2, errs2
    print("ALLE TESTS BESTANDEN")


if __name__ == "__main__":
    refs = build()
    if "--test" in sys.argv:
        test(refs)
