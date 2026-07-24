import csv
import os
from datetime import datetime


def export_to_csv(sid, description):

    file_exists = os.path.isfile("reports/uds_security_report.csv")

    with open("reports/uds_security_report.csv", "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Date",
                "Time",
                "SID",
                "Description"
            ])

        now = datetime.now()

        writer.writerow([
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S"),
            sid,
            description
        ])

        if __name__ == "__main__":
            export_to_csv(
            "0x27",
            "Test Security Access"
        )