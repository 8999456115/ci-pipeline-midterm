# CI Pipeline Midterm Project

## 🚀 Overview

This project is a Python Flask application with a complete CI pipeline built using GitHub Actions. It includes:

- Multi-environment support (dev & prod)
- Automated build, lint, test stages
- Docker image creation and publishing to a registry (Docker Hub or GHCR)
- Clean and PEP8-compliant code using flake8
- Configurable environment using .env files

---

## 📁 Project Structure

```
ci-pipeline-midterm/
├── app.py
├── requirements.txt
├── Dockerfile
├── .env.dev
├── .env.prod
├── tests/
│   └── test_app.py
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## 🧰 Requirements

- Python 3.9+
- pip
- Docker (optional, for containerization)

---

## 📦 Setup & Run

```bash
pip install -r requirements.txt
ENV=development python app.py
```

Or use:

```bash
export $(cat .env.dev | xargs)
python app.py
```

Visit: http://localhost:5000/

---

## 🧪 Run Unit Tests

```bash
PYTHONPATH=. pytest tests/
```

---

## 🧹 Run Linter

```bash
flake8 .
```

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t ci-pipeline-midterm .
```

### Run Container

```bash
docker run -p 5000:5000 ci-pipeline-midterm
```

### Optional: Push to DockerHub

```bash
docker tag ci-pipeline-midterm yourusername/ci-pipeline-midterm:dev
docker push yourusername/ci-pipeline-midterm:dev
```

---

## 🔁 CI/CD Pipeline Details

- **Auto Trigger:** on push or PR to `develop`
- **Manual Trigger:** on `main` branch or via workflow_dispatch
- **Stages:** Lint → Test → Docker Build → Docker Push

---

## 📝 Notes

- Uses `python-dotenv` to load `.env.dev` and `.env.prod`
- Make sure you set `ENV=development` to activate development mode
- Successfully tested in GitHub Codespace