from web_main import app


def test_root():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200