#  Cybercrime Time Machine — Digital Forensics Lab

<p align="center">
  <strong>Investigate Events. Reconstruct Attacks. Discover Evidence.</strong>
  <br/>
  A Python-based digital forensics learning platform that analyzes security events, reconstructs chronological timelines, and identifies potentially suspicious activity using explainable, rule-based detection.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Status-Educational%20Prototype-success?style=for-the-badge" />
</p>

---

##  Overview

**Cybercrime Time Machine** is a digital forensics learning platform designed to demonstrate how security events can be analyzed and reconstructed into meaningful investigation timelines.

The application processes security event records, organizes them chronologically, and applies transparent detection rules to identify potentially suspicious patterns.

Instead of simply displaying raw security logs, the platform connects related events, highlights investigation findings, assigns severity labels, and provides access to the underlying evidence.

The goal is to make security event investigation more understandable through an interactive browser-based workspace.

##  Key Features

| Feature | Description |
|---|---|
|  Event Timeline | Reconstruct security activities in chronological order |
|  Login Monitoring | Identify repeated failed login attempts |
|  Privilege Monitoring | Highlight privilege-change activities |
|  File Activity Analysis | Detect downloads involving sensitive-looking filenames |
|  Malware Alerts | Display malware-related indicators present in event records |
|  Risk Classification | Assign severity labels to investigation findings |
|  Evidence Inspector | Examine individual events behind each finding |
|  Investigation Dashboard | Visualize security activity through a dark-themed interface |
|  Flask JSON API | Retrieve timeline and investigation data through API endpoints |

##  Technology Stack

| Layer | Technology |
|---|---|
| Programming Language | Python |
| Backend Framework | Flask |
| Frontend | HTML5, CSS3, JavaScript |
| API | Flask JSON API |
| Data Format | JSON |
| Analysis | Rule-based event detection |

##  How It Works

```text
         Security Event Records
                   |
                   ▼
            Event Processing
                   |
                   ▼
          Chronological Sorting
                   |
                   ▼
           Forensic Analysis
                   |
        ┌──────────┼──────────┐
        ▼          ▼          ▼
     Login      Privilege   File Activity
    Analysis    Monitoring   Analysis
        |          |          |
        └──────────┼──────────┘
                   |
                   ▼
          Suspicious Pattern
              Detection
                   |
                   ▼
          Severity Classification
                   |
                   ▼
          Evidence Correlation
                   |
                   ▼
          Investigation Dashboard
                   |
                   ▼
          Timeline & Findings
```

##  Detection Capabilities

Cybercrime Time Machine uses transparent, rule-based detection techniques to highlight activities that may require further investigation.

### 1. Repeated Failed Login Attempts

Identifies repeated unsuccessful authentication attempts that may indicate password guessing or brute-force behaviour.

### 2. Privilege-Change Monitoring

Highlights recorded privilege-related activities that may require additional security review.

### 3. Sensitive File Download Detection

Identifies downloads involving filenames that match configured sensitive-file indicators.

### 4. Malware Alert Reporting

Displays malware-related indicators recorded in the available security evidence.

### 5. Severity Classification

Organizes investigation findings using severity labels to help prioritize manual review.

**Important:** Detection results depend on the available event data and configured rules. A suspicious pattern is an investigation indicator, not proof of an attack or malicious intent.

##  Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python 3.10 or later
- pip
- Git
- Windows PowerShell or a compatible terminal

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd FunkCrime
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```powershell
py -m venv .venv
```

### 3. Activate the Environment

```powershell
.venv\Scripts\activate
```

### 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

### 5. Start the Application

```powershell
python app.py
```

### 6. Open the Dashboard

Visit:

**http://127.0.0.1:5000**

The investigation dashboard will be available in your browser.

##  API Documentation

The application provides JSON endpoints for accessing investigation data.

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Load the investigation dashboard |
| GET | `/api/sample` | Retrieve the event timeline and investigation findings |

##  Security & Privacy

Cybercrime Time Machine is currently an educational digital forensics prototype.

- The current project uses fictional sample evidence.
- Detection results are based on configured rules.
- No production-grade authentication or access-control system is provided.
- Real security logs may contain sensitive personal and organizational information.
- Avoid uploading confidential evidence to public environments.
- Do not expose the development server directly to the public internet.

##  Current Limitations

- The current implementation uses fictional sample evidence.
- Detection is based on predefined rules rather than advanced behavioural analytics.
- Findings depend on the completeness and quality of available event records.
- Malware alerts are indicators from the supplied evidence, not independent malware verification.
- The application is not a certified digital forensic investigation platform.
- Live Windows Event Log integration is a planned enhancement, not an existing feature.

##  Future Enhancements

Potential improvements for future versions include:

- **Windows Event Log Integration:** Collect actual security events from authorized Windows systems.
- **Live Log Monitoring:** Receive and analyze events continuously.
- **Advanced Detection:** Improve suspicious activity detection with time-window-based rules.
- **Attack Reconstruction:** Correlate related events into more detailed investigation timelines.
- **IP Intelligence:** Integrate external threat-intelligence sources.
- **Evidence Management:** Preserve original event records and investigation references.
- **PDF Reports:** Generate downloadable forensic investigation reports.
- **Multi-System Monitoring:** Collect logs from authorized Linux servers and web applications.
- **Advanced Analytics:** Introduce statistical and behavioural anomaly detection.

##  Project Objectives

- Explore digital forensics and cybersecurity concepts.
- Understand security event analysis and investigation workflows.
- Identify potentially suspicious patterns using Python.
- Reconstruct chronological security event timelines.
- Improve visibility into security-related activities.
- Demonstrate practical Flask, Python and frontend development skills.

##  License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>🛡️ Cybercrime Time Machine</strong>
  <br/>
  <em>Every Event Tells a Story. Every Timeline Reveals Evidence.</em>
  <br/><br/>
  Built with Python, Flask, HTML, CSS and JavaScript.
</p>
