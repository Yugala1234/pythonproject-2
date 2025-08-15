from app import get_status

def test_google_status():
    assert get_status("https://example.com") == 200
