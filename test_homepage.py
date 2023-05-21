import requests

def test_homepage_load():
    url = "https://qwawa.github.io"

    response = requests.get(url)
    assert response.status_code == 200
    assert 'Welcome to My Website' in response.text
