"""
Module for Licensing a PDF File.
"""

from io import BytesIO

import base64

from fpdf import FPDF
from PyPDF2 import PdfWriter, PdfReader

class PDFLicenser:
    """
    Class for licensing music sheets.
    """

    def __init__(self, company_logo_pic_path, order):
        self.company_logo_pic_path = company_logo_pic_path
        self.order = order
    
    def license_articles(self):
        """
        License all articles of an order.
        """
        licensed_articles = {}

        for article in self.order.articles:
            license_obj = PdfReader(self._create_license_agreement_pdf())
            license_page = license_obj.pages[0]

            watermark_obj = PdfReader(self._create_watermark_pdf())
            watermark_page = watermark_obj.pages[0]

            pdf_reader = PdfReader(BytesIO(article.music_sheet))
            pdf_writer = PdfWriter()

            pdf_writer.add_page(license_page)

            for page in pdf_reader.pages:
                page.merge_page(watermark_page)
                pdf_writer.add_page(page)

            bytes_memory = BytesIO()
            pdf_writer.write(bytes_memory)
            licensed_articles[article.article_number] = base64.b64encode(bytes_memory.getvalue()).decode()

        return True, licensed_articles

    def _create_license_agreement_pdf(self):
        license_agreement_pdf = FPDF()
        license_agreement_pdf.add_font('ebrima', '', r"c:\WINDOWS\Fonts\ebrima.ttf", uni=True)
        license_agreement_pdf.add_page()
        license_agreement_pdf.image(self.company_logo_pic_path, 10, 8, 33)
        license_agreement_pdf.ln(25)
        license_agreement_pdf.set_font("ebrima", "U", 16)
        license_agreement_pdf.cell(0, 10, "Lizenzvereinbarung")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.set_font("ebrima", "", 12)
        license_agreement_pdf.cell(0, 10, "Zum Download über www.melicus-musikverlag.de mit der Bestellnummer " + self.order.order_number + " am " + self.order.order_date)
        license_agreement_pdf.ln(10)
        license_agreement_pdf.cell(0, 10, "Die folgenden Bestimmungen regeln die Nutzungsbedingungen zwischen")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.cell(0, 10, "melicus.musikverlag - Neunburger Str. 11 - D-92431 Neunburg")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_font("ebrima", "", 8)
        license_agreement_pdf.cell(0, 10, "(nachfolgend Verlag)")
        license_agreement_pdf.set_font("ebrima", "", 12)
        license_agreement_pdf.ln(10)
        license_agreement_pdf.cell(0, 10, "und")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.cell(0, 10, self.order.name() + ", " + self.order.address.street + ", " + self.order.address.postcode + ", " + self.order.address.place)
        license_agreement_pdf.set_font("ebrima", "", 8)
        license_agreement_pdf.ln(5)
        license_agreement_pdf.cell(0, 10, "(nachfolgend Käufer)")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.set_font("ebrima", "", 12)
        license_agreement_pdf.cell(0, 10, "für das Werk: ")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.set_x(20)
        license_agreement_pdf.cell(0, 10, "1. Der Käufer erhält das Recht, das korrekt lizensierte Werk aufzuführen.")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(28)
        license_agreement_pdf.cell(0, 10, "1.1 Orchester- und Ensemblewerke gelten nur mit der Nennung des Musikvereins, Musikkapelle")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(35)
        license_agreement_pdf.cell(0, 10, "Ensembles oder des Orchesters im Lizenzhinweis als korrekt lizensiert. Ausnahmen hiervon")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(35)
        license_agreement_pdf.cell(0, 10, "können nur vom Verlag genehmigt werden.")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(28)
        license_agreement_pdf.cell(0, 10, "1.2 Solo- bis Quintettwerke gelten mit dem Namen des Käufers als lizensiert.")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(28)
        license_agreement_pdf.cell(0, 10, "1.3 Als Nachweis für die rechtmäßige Lizensierung muss der Lizenzhinweis auf jeder")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(35)
        license_agreement_pdf.cell(0, 10, "ausgedruckten Notenseite vorhanden sein und darf nicht entfernt werden.")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.set_x(20)
        license_agreement_pdf.cell(0, 10, "2. Der Käufer ist verpflichtet, die Verwendung (z.B. Aufführungen oder Aufnahmen) zuständigen")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(25)
        license_agreement_pdf.cell(0, 10, "Stelle zu melden (GEMA, SUISA, AKM usw.).")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.set_x(20)
        license_agreement_pdf.cell(0, 10, "3. Die Vervielfältigung, der Verleih und die Weiterverlneitung des vorliegenden Werkes oder")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(25)
        license_agreement_pdf.cell(0, 10, "Reproduktionen jeglicher Art davon sind untersagt.")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.set_x(20)
        license_agreement_pdf.cell(0, 10, "4. Keine Teile des Werkes dürfen (auch nicht auszugsweise) ohne die ausdrückliche schriftliche ")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(25)
        license_agreement_pdf.cell(0, 10, "Zustimmung auf elektronische oder sonstige Weise an Dritte übermittelt, vervielfältigt oder so ")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.set_x(25)
        license_agreement_pdf.cell(0, 10, "gespeichert werden, dass Dritte auf sie zugreifen können.")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.set_x(20)
        license_agreement_pdf.cell(0, 10, "5. Das Vervielfältigen von Werken – auch auszugsweise – ist grundsätzlich verboten.")
        license_agreement_pdf.ln(15)
        license_agreement_pdf.set_font("ebrima", "U", 12)
        license_agreement_pdf.cell(0, 10, "Der Käufer hat jedoch folgende Befugnisse:")
        license_agreement_pdf.set_font("ebrima", "", 12)
        license_agreement_pdf.ln(5)
        license_agreement_pdf.cell(0, 10, "Das Erstellen von Ausdrucken zum Studium, für Proben und Aufführungen in der Anzahl der Besetzung ")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.cell(0, 10, "des lizensierten Musikvereins, der Musikkapelle oder des Orchesters. Jegliche darüber hinausgehende")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.cell(0, 10, "Verwendungen und Nutzungen des Werkes bedarf der ausdrücklichen schriftlichen Zustimmung des")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.cell(0, 10, "Verlags.")
        license_agreement_pdf.ln(10)
        license_agreement_pdf.cell(0, 10, "6. Diese Bestimmungen treten in Kraft, sobald der Käufer das Werk erworben und damit begonnen hat")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.cell(0, 10, "diese von seinem Computer auszudrucken oder auf diesem zu speichern. Außerdem gelten die ")
        license_agreement_pdf.ln(5)
        license_agreement_pdf.cell(0, 10, "Allgemeinen Geschäftsbedingungen des Verlags.")

        return BytesIO(license_agreement_pdf.output(dest="S").encode('latin-1'))

    def _create_watermark_pdf(self):
        watermark_pdf = FPDF()
        watermark_pdf.set_auto_page_break(False)
        watermark_pdf.add_font('ebrima', '', r"c:\WINDOWS\Fonts\ebrima.ttf", uni=True)
        watermark_pdf.add_page()
        watermark_pdf.set_font("ebrima", "", 8)
        watermark_pdf.set_xy(-5,80)
        watermark_pdf.rotate(-90)
        watermark_pdf.cell(0, 0, self.order.get_license_name(), 0, 0)
        
        return BytesIO(watermark_pdf.output(dest="S").encode('latin-1'))
