from logger import write_log
from csv_report import export_to_csv
from threat_timeline import add_event

from risk_engine import (
    add_security_access,
    add_ecu_reset,
    add_write_data,
    add_brute_force
)

import time


# Sayaçlar
security_access_counter = 0
first_attempt_time = None
brute_force_count = 0

diagnostic_session_count = 0
ecu_reset_count = 0
read_data_count = 0
security_access_count = 0
write_data_count = 0


def analyze_uds_message(message):
    global security_access_counter
    global first_attempt_time
    global brute_force_count
    global diagnostic_session_count
    global ecu_reset_count
    global read_data_count
    global security_access_count
    global write_data_count

    sid = message["SID"]

    if sid == "0x10":

        diagnostic_session_count += 1
        add_security_access()

        print("🔵 Diagnostic Session Control")

        write_log("Diagnostic Session Control")
        add_event("Diagnostic Session Control")

        export_to_csv(
            sid,
            "Diagnostic Session Control"
        )

    elif sid == "0x11":

        ecu_reset_count += 1
        add_ecu_reset()

        print("🟠 ECU Reset Request")

        write_log("ECU Reset Request")
        add_event("ECU Reset Request")

        export_to_csv(
            sid,
            "ECU Reset Request"
        )

    elif sid == "0x22":

        read_data_count += 1

        print("🟢 Read Data By Identifier")

        write_log("Read Data By Identifier")
        add_event("Read Data By Identifier")

        export_to_csv(
            sid,
            "Read Data By Identifier"
        )

    elif sid == "0x27":

        security_access_count += 1
        add_security_access()

        print("🔒 Security Access Detected")

        write_log("Security Access Detected")
        add_event("Security Access Detected")

        export_to_csv(
            sid,
            "Security Access Detected"
        )

        current_time = time.time()

        if first_attempt_time is None:
            first_attempt_time = current_time

        security_access_counter += 1

        if current_time - first_attempt_time <= 5:

            if security_access_counter >= 3:

                brute_force_count += 1
                add_brute_force()

                print("🚨 Brute Force Attack Detected!")
                print(
                    f"Toplam Brute Force Saldırısı: {brute_force_count}"
                )

                write_log(
                    f"Brute Force Attack Detected ({brute_force_count})"
                )

                add_event(
                    f"Brute Force Attack Detected ({brute_force_count})"
                )

                export_to_csv(
                    sid,
                    f"Brute Force Attack Detected ({brute_force_count})"
                )

        else:

            security_access_counter = 1
            first_attempt_time = current_time

    elif sid == "0x2E":

        write_data_count += 1
        add_write_data()

        print("📝 Write Data By Identifier")

        write_log("Write Data By Identifier")
        add_event("Write Data By Identifier")

        export_to_csv(
            sid,
            "Write Data By Identifier"
        )

    else:

        print("⚪ Unknown UDS Service")

        write_log("Unknown UDS Service")
        add_event("Unknown UDS Service")

        export_to_csv(
            sid,
            "Unknown UDS Service"
        )