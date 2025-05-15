# URL Shortener Service

A FastAPI-based URL shortening service with Docker support, automated testing, and CI/CD.

## Features

- Shorten long URLs to compact codes
- Redirect short codes to original URLs
- REST API documentation (Swagger)
- Docker containerization
- Automated testing with pytest
- GitHub Actions CI/CD pipeline

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
API: http://localhost:8000
Docs: http://localhost:8000/docs

Testing
Run tests with:
bash
docker-compose exec web pytest -v
Test coverage:

bash
docker-compose exec web pytest --cov=app --cov-report=term-missing
