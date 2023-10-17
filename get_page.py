import requests
from pprintpp import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("user", help="Enter the github user to query")
args = parser.parse_args()
print(f"Using gihub user: {args.user}")

gists = []
# Test gihub user PlugFox
github_user = args.user
gist_api = 'https://api.github.com/users/' + github_user + '/gists'
response = requests.get(gist_api)
print(f"The response is: {response.status_code}")
#json_response = r.json()
#r.json()
# print(response)
#pprint(response.json())

pages = response.json()

# #    print("The") 
if response.status_code != 200:
    if response.status_code == 404:
        print("The page was not found")
else:
    for page in pages:
        print(f"The gist was created on: {page['created_at']} and the Gist URL is: {page['html_url']}")

# pprint(pages[0]['created_at'])
# pprint(pages[0]['html_url'])
# print(pages[0]['created_at'])
# print(f"The gist was created on: {pages[0]['created_at']} and the Gist URL is: {pages[0]['html_url']}")