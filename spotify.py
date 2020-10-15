import requests
import startup

def getTopArtists(): 
    (token, headers, scopes, expiration) = startup.getAccessToken()
    api_url = "https://api.spotify.com/v1/me/top/{}".format("artists") 
    bearer_token = "Bearer {}".format(token)     
    headers = {"authorization": bearer_token}
    r = requests.get(api_url, headers=headers)
    return r.json()  