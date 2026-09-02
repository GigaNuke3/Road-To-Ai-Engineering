import requests

def get_github_info():
    try:
        response = requests.get("https://api.gitthub.com")
        data = response.json()   
        return data["repository_url"]
    except requests.exceptions.RequestException:
        return "Could not reach the API"

print(get_github_info())
