def read_uds_log(filename):

    messages = []

    with open(filename, "r") as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            parts = line.split()

            sid = parts[0]

            data = parts[1:]

            messages.append({
                "SID": sid,
                "DATA": data
            })

    return messages