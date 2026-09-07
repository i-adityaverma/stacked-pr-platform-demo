from app import create_app


def test_liveness():
    client = create_app().test_client()
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json == {"status": "alive"}


def test_readiness():
    client = create_app().test_client()
    response = client.get("/health/ready")
    assert response.status_code == 200
    assert response.json == {"status": "ready"}
