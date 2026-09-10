# RecoverAI

AI-Powered Mobile Data Recovery & Digital Forensics Platform.

> RecoverAI is designed for authorized recovery and analysis of data from devices and storage media owned by the user or explicitly authorized for inspection.

## Architecture

Web Dashboard → Recovery Agent → Recovery Engine → AI Analyzer → Forensics Engine → Reports

Supported/planned sources:
- Android devices through officially authorized ADB connections
- iPhone/iPad backups
- SD cards and removable storage
- File signatures, metadata and hashing
- Evidence/case tracking and audit logs

## Backend

Python + FastAPI

Run locally:

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API:
- `GET /`
- `GET /api`
- `GET /api/health`
- `GET /api/devices`
- `GET /api/devices/android`

## Responsible use

RecoverAI must only be used with devices, storage and data that the operator owns or is authorized to inspect.

It does not bypass device locks, passwords, authentication, encryption, or platform security controls.

Modern Android/iOS encryption, TRIM, secure erase and vendor restrictions can make recovery technically impossible.

## Roadmap

- v0.1 Foundation
- v0.2 Device Manager
- v0.3 Recovery Engine
- v0.4 AI Analyzer
- v0.5 Digital Forensics
- v0.6 iOS/Backup Analysis
- v1.0 Production Platform
