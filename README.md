# SIEM Dashboard

A lightweight Security Information and Event Management (SIEM) dashboard built with Python and Flask. Parses Linux auth logs, detects brute force login attempts, and displays flagged IPs with forensic detail in a web interface.

![Dashboard Preview](static\siem-dashboard.png)

## Features

- Parses raw `auth.log` files using regex-based pattern matching
- Detects brute force attempts by counting failed logins per IP
- Alerts on any IP exceeding a configurable threshold (default: 5)
- Displays first seen / last seen timestamps per flagged IP
- Tracks which usernames were attempted from each IP
- Clean dark-themed web dashboard built with Flask

## Project Structure
```
siem-dashboard/
├── app.py            # Flask server — wires parser and detector to web route
├── parser.py         # Regex-based log parser — structures raw log lines
├── detector.py       # Brute force detector — counts failures and returns alerts
├── auth.log          # Sample auth log file
├── NOTES.md          # Development notes — mistakes, resolutions, lessons learned
├── static/
│   └── styles.css    # Dashboard styles
└── templates/
    └── index.html    # Dashboard UI
```

## How It Works

1. `parser.py` reads `auth.log` line by line and extracts timestamp, status, username, and IP using regex
2. `detector.py` receives the parsed entries, counts failed attempts per IP, and returns alerts for any IP above the threshold
3. `app.py` runs both on each request and passes the results to the dashboard
4. `index.html` renders stats and alert cards in the browser

## Setup and Installation

**Prerequisites:** Python 3, Flask
```bash
# Clone the repo
git clone https://github.com/rohanmorar/siem-dashboard.git
cd siem-dashboard

# Install Flask
pip install flask

# Run the dashboard
python3 app.py
```

Then visit `http://127.0.0.1:5000` in your browser.

## Configuration

To change the alert threshold, update `THRESHOLD` in `detector.py`:
```python
THRESHOLD = 5  # alert if an IP has this many or more failed attempts
```

## Skills Demonstrated

- Python scripting and modular code design
- Regex-based log parsing
- Brute force / anomaly detection logic
- Flask web framework
- HTML/CSS dashboard UI
- Git version control with incremental commits
- Defensive coding — error handling, no hardcoded indexes

## Context

Built as part of a hands-on SOC analyst learning path. Part of a larger series of security tooling projects.