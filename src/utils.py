import requests

def get_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        return False