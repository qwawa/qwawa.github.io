import requests

def test_homepage_load():
    url = "https://qwawa.github.io"

    response = requests.get(url) # Send a GET request to the specified URL
    assert response.status_code == 200 # Check if the response status code is 200
    assert 'qwawa.github.io' in response.text # Check if 'qwawa.github.io' is present in the response text
