import requests

class FeedlyClient:
    def __init__(self, client_id, client_secret, access_token=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
    
    def get_access_token(self, redirect_uri, code):
        url = "https://cloud.feedly.com/v3/auth/token"
        headers = {"Content-Type": "application/json"}
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
            "code": code
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        self.access_token = response.json()["access_token"]
        return self.access_token
    
    def api_request(self, endpoint, params=None):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        url = f"https://cloud.feedly.com/v3/{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
