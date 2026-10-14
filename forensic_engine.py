import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
SAMPLE_FILE = BASE_DIR / "sample_evidence" / "sample_logs.json"


def load_sample_events():
    with SAMPLE_FILE.open("r", encoding="utf-8") as file:
        events = json.load(file)

    if not isinstance(events, list):
        raise ValueError("Evidence must be a JSON list.")

    for event in events:
        if not isinstance(event, dict) or "timestamp" not in event:
            raise ValueError("Each event must have a timestamp.")

        datetime.fromisoformat(
            event["timestamp"].replace("Z", "+00:00")
        )

    return events


def analyze_events(events):
    timeline = sorted(
        events,
        key=lambda event: datetime.fromisoformat(
            event["timestamp"].replace("Z", "+00:00")
        ),
    )

    findings = []
    failed_logins = {}

    for event in timeline:
        if event.get("event_type") == "login_failed":
            ip = event.get("source_ip", "Unknown")
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

    for ip, count in failed_logins.items():
        if count >= 3:
            findings.append({
                "severity": "High",
                "title": "Repeated failed logins",
                "description": f"{count} failed login attempts from {ip}.",
                "source_ip": ip,
                "recommendation": "Review authentication logs and verify the source.",
            })

    for event in timeline:
        kind = event.get("event_type")

        if kind == "privilege_change":
            findings.append({
                "severity": "High",
                "title": "Privilege change detected",
                "description": (
                    f"Privilege change for {event.get('username', 'unknown user')}."
                ),
                "source_ip": event.get("source_ip", "Unknown"),
                "recommendation": "Verify the account change was authorized.",
            })

        elif kind == "file_download":
            filename = event.get("filename", "")
            sensitive_words = ("password", "secret", "backup", "confidential")

            if any(word in filename.lower() for word in sensitive_words):
                findings.append({
                    "severity": "Medium",
                    "title": "Sensitive-looking file downloaded",
                    "description": f"Review the download of {filename}.",
                    "source_ip": event.get("source_ip", "Unknown"),
                    "recommendation": "Check file access records and authorization.",
                })

        elif kind == "malware_alert":
            findings.append({
                "severity": "Critical",
                "title": "Malware alert recorded",
                "description": (
                    f"Alert on {event.get('hostname', 'unknown device')}."
                ),
                "source_ip": event.get("source_ip", "Unknown"),
                "recommendation": "Investigate the alert using incident response procedures.",
            })

    return {
        "total_events": len(timeline),
        "total_findings": len(findings),
        "timeline": timeline,
        "findings": findings,
    }