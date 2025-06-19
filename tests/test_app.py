from app import app


def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200


def test_home_data():
    tester = app.test_client()
    response = tester.get('/')
    assert b"Hello from CI Pipeline!" in response.data


def test_app_exists():
    assert app is not None


def test_app_debug_mode():
    assert app.debug is False
