from report import generate_report
from uds_log_parser import read_uds_log
from uds_analyzer import (
    analyze_uds_message,
    diagnostic_session_count,
    ecu_reset_count,
    read_data_count,
    security_access_count,
    brute_force_count
)

import time


print("=" * 50)
print(" Automotive UDS Security Analyzer")
print("=" * 50)


try:

    # Gerçek UDS log dosyasını oku
    messages = read_uds_log("logs/uds_test_log.txt")


    for message in messages:

        print(f"\nSID: {message['SID']}  DATA: {message['DATA']}")

        analyze_uds_message(message)

        time.sleep(0.5)


except KeyboardInterrupt:

    print("\nProgram durduruldu.")


finally:

    generate_report(
        diagnostic_session_count,
        ecu_reset_count,
        read_data_count,
        security_access_count,
        brute_force_count
    )