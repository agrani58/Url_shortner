# 🔗 URL Shortener - FastAPI Microservice

A high-performance URL shortening service built with FastAPI, Docker, and GitHub Actions CI/CD.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

## ✨ Features

- Convert long URLs to short, memorable codes
- Redirect visitors to original URLs
- Admin-protected API endpoints
- SQLite database persistence
- Docker containerization
- Automated testing with GitHub Actions

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker & Docker Compose

## Prerequisites

- Python 3.9+
- Docker Desktop
- Git

## Local Development

### Without Docker

1. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\Activate  # Windows
Install dependencies:
pip install -r requirements.txt
Configure environment:
Create .env file:

Run the application:

bash
uvicorn app.main:app --reload

With Docker
Build and run:

bash
docker-compose up --build
Access services:
Docs: http://localhost:8000/docs

Testing
Run tests with:
bash
docker-compose exec web pytest -v
Test coverage:
