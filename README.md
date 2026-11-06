# Cybercrime Time Machine

A digital forensics learning prototype that reconstructs chronological security event timelines and flags potentially suspicious patterns using explainable, rule-based detection.

## Features

- Chronological security event timeline
- Detection of repeated failed logins
- Privilege-change monitoring
- Detection of sensitive-looking file downloads
- Malware alert reporting
- Severity-labelled investigation findings
- Evidence inspector for individual events
- Interactive dark-themed dashboard
- Flask JSON API

## Technology

- Python
- Flask
- HTML
- CSS
- JavaScript

## Getting started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd FunkCrime
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create a virtual environment

Windows:

```powershell
py -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## API

- `GET /` — dashboard
- `GET /api/sample` — timeline and investigation findings

## Detection limitations

The engine uses simple, transparent rules. A finding indicates activity worth reviewing; it does not prove malicious intent or establish that a crime occurred.

This project uses fictional sample evidence. It is an educational prototype, not a production forensic investigation platform. Do not upload real sensitive logs or expose the development server publicly.

