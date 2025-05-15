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

### Local Development
```bash
# 1. Clone the repo
git clone https://github.com/your-username/Url_shortener.git
cd Url_shortener

# 2. Set up environment
cp .env.example .env  # Update with your credentials

# 3. Start services
docker-compose up -d

# 4. Access API at http://localhost:8000
📚 API Documentation
Endpoints
Method	Endpoint	Description
POST	/links	Create short URL
GET	/{code}	Redirect to original URL
Example Request:

bash
curl -X POST "http://localhost:8000/links" \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://example.com/very-long-url"}'
🛠️ Tech Stack
Backend: FastAPI

Database: SQLite (SQLAlchemy ORM)

Auth: Admin credentials via environment variables

Infra: Dockerized deployment

CI/CD: GitHub Actions with pytest
