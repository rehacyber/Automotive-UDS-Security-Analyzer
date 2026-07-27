from datetime import datetime
import os


def add_event(event):

    os.makedirs("logs", exist_ok=True)

    with open(
        "logs/threat_timeline.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            f"{datetime.now()} | {event}\n"
        )