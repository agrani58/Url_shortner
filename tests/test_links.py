import sys
from pathlib import Path

# Add project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_create_link():
    response = client.post("/links/", json={"original_url": "https://example.com"})
    assert response.status_code == 200
    assert "short_code" in response.json()
