import requests

def test_homepage_load():
    url = "https://qwawa.github.io"

    response = requests.get(url)
    assert response.status_code == 200
    assert 'qwawa.github.io' in response.text
