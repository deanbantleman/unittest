import requests
from pprintpp import pprint

gists = []
github_user = 'PlugFox'
gist_api = 'https://api.github.com/users/' + github_user + '/gists'
response = requests.get(gist_api)
#json_response = r.json()
#r.json()
# print(response)
# pprint(response.json())

pages = response.json()
pprint(pages[0]['created_at'])