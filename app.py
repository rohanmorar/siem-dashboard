from flask import Flask, render_template
from parser import parse_log
from detector import detect

app = Flask(__name__)

LOG_FILE = "auth.log"

@app.route("/")
def index():
    entries = parse_log(LOG_FILE)
    alerts = detect(entries)

    stats = {
        "total_entries": len(entries),
        "total_failed": len([e for e in entries if e["status"] == "failed"]),
        "total_accepted": len([e for e in entries if e["status"] == "accepted"]),
        "total_alerts": len(alerts)
    }

    return render_template("index.html", alerts=alerts, stats=stats)

if __name__ == "__main__":
    app.run(debug=True)