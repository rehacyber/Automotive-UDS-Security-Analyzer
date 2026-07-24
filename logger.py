from datetime import datetime

def write_log(message):
    current_time = datetime.now().strftime("%H:%M:%S")

    with open("logs/uds_security.log", "a") as file:
        file.write(f"[{current_time}] {message}\n")