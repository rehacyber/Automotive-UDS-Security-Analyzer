import random

def generate_uds_message():

    return {
        "SID": "0x27",
        "DATA": [
            hex(random.randint(0, 255))
            for _ in range(8)
        ]
    }