import re

def parse_log(filepath):
    entries = []

    try:
        with open(filepath, "r") as file:
            for line in file:
                line = line.strip()

                if "Failed password" not in line and "Accepted password" not in line:
                    continue

                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                user_match = re.search(r'for (?:invalid user )?(\w+) from', line)
                time_match = re.search(r'^(\w+\s+\d+\s+[\d:]+)', line)

                if not ip_match or not user_match or not time_match:
                    print(f"Warning: skipping malformed line: {line}")
                    continue

                entry = {
                    "timestamp": time_match.group(1),
                    "status": "failed" if "Failed password" in line else "accepted",
                    "user": user_match.group(1),
                    "ip": ip_match.group(1),
                    "raw": line
                }

                entries.append(entry)

    except FileNotFoundError:
        print(f"Error: {filepath} not found")

    return entries

"""
**What changed and why:**

- `re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)` — finds the IP by looking for the word `from` followed by four numbers separated by dots. Doesn't matter what position it's at.
- `re.search(r'for (?:invalid user )?(\w+) from', line)` — finds the username by looking for the pattern `for [optional: invalid user] username from`
- `re.search(r'^(\w+\s+\d+\s+[\d:]+)', line)` — finds the timestamp at the start of the line
- If any of these fail to match, we skip the line with a warning instead of crashing

"""