from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime


def generate_report(
    diagnostic_session_count,
    ecu_reset_count,
    read_data_count,
    security_access_count,
    brute_force_count
):

    print("PDF rapor fonksiyonu çalıştı")

    report_text = [
        "========== UDS SECURITY REPORT ==========",
        f"Report Date            : {datetime.now()}",
        "",
        f"Diagnostic Session     : {diagnostic_session_count}",
        f"ECU Reset              : {ecu_reset_count}",
        f"Read Data Identifier   : {read_data_count}",
        f"Security Access        : {security_access_count}",
        f"Brute Force Attacks    : {brute_force_count}",
        "",
        "========================================="
    ]


    # TXT Rapor
    with open("reports/uds_security_report.txt", "w", encoding="utf-8") as file:

        for line in report_text:
            file.write(line + "\n")


    # PDF Rapor
    pdf_file = "reports/UDS_Security_Report.pdf"

    pdf = canvas.Canvas(pdf_file, pagesize=letter)

    y = 750

    for line in report_text:

        pdf.drawString(50, y, line)
        y -= 25

    pdf.save()


    print("\n✅ TXT raporu oluşturuldu: uds_security_report.txt")
    print("✅ PDF raporu oluşturuldu: UDS_Security_Report.pdf")