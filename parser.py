def parse_log(filepath):
    entries = []

    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()

                if len(line.split()) < 13:
                    continue

                parts = line.split()

                entry = {
                    "timestamp": f"{parts[0]} {parts[1]} {parts[2]}",
                    "status": "failed" if "Failed password" in line else "accepted",
                    "user": parts[10] if "invalid user" in line else parts[8],
                    "ip": parts[12] if "Failed password" in line else parts[10],
                    "raw": line
                }

                entries.append(entry)

    except FileNotFoundError:
        print(f"Error: {filepath} not found")

    return entries

"""
**What each part does:**

- `parse_log(filepath)` — takes a file path and returns a list of log entries
- `entries = []` — we'll collect every parsed line in here as a dictionary
- `entry = {...}` — each line becomes a dictionary with timestamp, status, user, ip, and the raw line
- `"failed" if "Failed password" in line else "accepted"` — determines the status in one line
- We return `entries` so other files like `detector.py` and `app.py` can use it
"""