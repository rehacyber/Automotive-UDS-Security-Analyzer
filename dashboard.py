def show_dashboard(
    diagnostic_session,
    ecu_reset,
    read_data,
    write_data,
    security_access,
    brute_force,
    risk_score,
    threat_level
):

    print("\n" + "=" * 60)
    print("      AUTOMOTIVE UDS SECURITY DASHBOARD")
    print("=" * 60)

    print(f"Diagnostic Session : {diagnostic_session}")
    print(f"ECU Reset          : {ecu_reset}")
    print(f"Read Data          : {read_data}")
    print(f"Write Data         : {write_data}")
    print(f"Security Access    : {security_access}")
    print(f"Brute Force        : {brute_force}")

    print("-" * 60)

    print(f"Risk Score         : {risk_score}")
    print(f"Threat Level       : {threat_level}")

    print("=" * 60)