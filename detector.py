THRESHOLD = 5

def detect(entries):
    failed_logins = {}

    for entry in entries:
        if entry["status"] != "failed":
            continue

        ip = entry["ip"]

        if ip not in failed_logins:
            failed_logins[ip] = {"count": 0, "timestamps": [], "users": []}

        failed_logins[ip]["count"] += 1
        failed_logins[ip]["timestamps"].append(entry["timestamp"])

        if entry["user"] not in failed_logins[ip]["users"]:
            failed_logins[ip]["users"].append(entry["user"])

    alerts = []

    for ip, data in failed_logins.items():
        if data["count"] >= THRESHOLD:
            alerts.append({
                "ip": ip,
                "count": data["count"],
                "first_seen": data["timestamps"][0],
                "last_seen": data["timestamps"][-1],
                "users": data["users"]
            })

    return alerts