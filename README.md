# 🚀 CI Pipeline Midterm Project – Flask + Docker + GitHub Actions

## 🧾 Overview

This project is a Python Flask web application built as part of a CI/CD pipeline assignment. It includes:

- A sample REST API (`/`) returning a debug status message
- Full CI pipeline using GitHub Actions with Build, Lint, Test, Docker Build & Push stages
- Environment-based config using `.env.dev` and `.env.prod`
- Docker image build & run instructions
- Multi-environment workflow (`develop` → dev, `main` → prod)

---

## 📂 Project Structure

```
ci-pipeline-midterm/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker image definition
├── .env.dev                  # Development environment variables
├── .env.prod                 # Production environment variables
├── tests/
│   └── test_app.py           # Unit tests (pytest)
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI workflow
└── README.md                 # Project documentation
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ci-pipeline-midterm.git
cd ci-pipeline-midterm
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Run Tests

```bash
PYTHONPATH=. pytest tests/
```

---

## 🧹 Run Linter

```bash
flake8 .
```

If nothing prints, all checks passed. If there are issues, follow flake8 messages to fix.

---

## 🌐 Run the App (Locally)

### 1. Using default environment:

```bash
ENV=development python app.py
```

Or load the `.env.dev` file manually:

```bash
export $(cat .env.dev | xargs)
python app.py
```

Then visit: `http://localhost:5000`

### Expected Output:
```
Hello from CI Pipeline! Debug Mode: True
```

---

## 🐳 Docker Instructions

### 1. Build the image

```bash
docker build -t ci-pipeline-midterm .
```

### 2. Run the container

```bash
docker run -p 5000:5000 ci-pipeline-midterm
```

Visit: `http://localhost:5000`

### 3. Tag the image for Docker Hub (optional)

```bash
docker tag ci-pipeline-midterm yourusername/ci-pipeline-midterm:dev
```

### 4. Push to Docker Hub

```bash
docker push yourusername/ci-pipeline-midterm:dev
```

> Replace `yourusername` with your actual Docker Hub username.

---

## 🔁 CI/CD Pipeline (GitHub Actions)

The GitHub Actions pipeline is triggered by:

- ✅ Push or PR to `develop` → triggers CI, tags image as `:dev`
- ✅ Manual or push to `main` → triggers production CI, tags image as `:latest`

### Workflow steps:
1. Checkout code
2. Set up Python 3.9
3. Install dependencies
4. Run linter (flake8)
5. Run unit tests (pytest)
6. Build Docker image
7. Push Docker image to GHCR or Docker Hub

You can find the workflow in: `.github/workflows/ci.yml`

---

## 📥 Environment Files

You may configure runtime behavior via:

### `.env.dev`
```
ENV=development
DEBUG=True
```

### `.env.prod`
```
ENV=production
DEBUG=False
```

These are used by `python-dotenv` in `app.py` to load proper configs.

---

## ✅ Status

- [x] CI pipeline working on GitHub Actions
- [x] Linting with flake8 passes cleanly
- [x] Unit tests cover multiple cases
- [x] Docker image builds and runs
- [x] Multi-env support via .env files
- [x] Compatible with GitHub Codespaces

---

## 📎 Final Notes

You can run this project offline using:

```bash
./run_all.sh
```

Or manually follow steps listed above.

To submit, share your GitHub repo URL and include screenshots of:
- CI/CD pipeline run (green checkmarks)
- Local browser output (`Hello from CI Pipeline!`)

---

Created by: Sahil Sorathiya
