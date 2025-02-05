import requests
from django.conf import settings

GOOGLE_API_KEY = getattr(settings, "GOOGLE_API_KEY", "")
SEARCH_ENGINE_ID = getattr(settings, "SEARCH_ENGINE_ID", "")

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID
    }
    response = requests.get(url, params=params)
    return response.json()
