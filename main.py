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

from risk_engine import (
    get_statistics,
    get_threat_level
)

from dashboard import show_dashboard

import time


print("=" * 60)
print(" Automotive UDS Security Analyzer")
print("=" * 60)

try:

    # Gerçek UDS log dosyasını oku
    messages = read_uds_log("logs/uds_test_log.txt")

    print(f"\nToplam UDS Mesajı : {len(messages)}")

    for message in messages:

        print("\n----------------------------")
        print(f"SID  : {message['SID']}")
        print(f"DATA : {message['DATA']}")

        analyze_uds_message(message)

        time.sleep(0.5)

except KeyboardInterrupt:

    print("\nProgram kullanıcı tarafından durduruldu.")

finally:

    # TXT / CSV / PDF raporlarını oluştur
    generate_report(
        diagnostic_session_count,
        ecu_reset_count,
        read_data_count,
        security_access_count,
        brute_force_count
    )

    (
        security_access,
        ecu_reset,
        write_data,
        brute_force,
        risk_score
    ) = get_statistics()

    # Dashboard
    show_dashboard(
        diagnostic_session_count,
        ecu_reset_count,
        read_data_count,
        write_data,
        security_access,
        brute_force,
        risk_score,
        get_threat_level()
    )