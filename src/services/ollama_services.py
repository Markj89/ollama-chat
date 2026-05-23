import requests
from requests.exceptions import RequestException
from ollama import Client

def check_url(url) -> bool:
    try:
        response = requests.get(url, allow_redirects=True, timeout=5)
        response.raise_for_status()
        return True
    except RequestException:
        return False
    
def ollama_client(url) -> Client:
    return Client(host=url)
