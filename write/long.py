import requests

API = 'https://single-developers.herokuapp.com/write'

text="""Anonymous Devaloper """

body = {
  "text":f"{text}"
}

req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)

print(req.history[1].url)
