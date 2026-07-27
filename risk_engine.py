risk_score = 0

security_access_count = 0
ecu_reset_count = 0
write_data_count = 0
brute_force_count = 0


def add_security_access():
    global security_access_count, risk_score

    security_access_count += 1
    risk_score += 2


def add_ecu_reset():
    global ecu_reset_count, risk_score

    ecu_reset_count += 1
    risk_score += 3


def add_write_data():
    global write_data_count, risk_score

    write_data_count += 1
    risk_score += 4


def add_brute_force():
    global brute_force_count, risk_score

    brute_force_count += 1
    risk_score += 6


def get_threat_level():

    if risk_score < 5:
        return "LOW"

    elif risk_score < 10:
        return "MEDIUM"

    elif risk_score < 20:
        return "HIGH"

    return "CRITICAL"


def get_statistics():

    return (
        security_access_count,
        ecu_reset_count,
        write_data_count,
        brute_force_count,
        risk_score
    )