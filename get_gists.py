import requests
from pprintpp import pprint
import argparse
import os
from datetime import datetime

def get_gists(username):
    gist_api = 'https://api.github.com/users/' + username + '/gists'
    print(f"The url in the function is: {gist_api}")
    gists = []

    page_number = 1
    while True:        
        params = {'page': page_number}
        response = requests.get(gist_api, params=params)
        print(f"The response is: {response.status_code}")
        #pprint(response.json())

        if response.status_code != 200:
            if response.status_code == 404:
                print("The page was not found")
            else:
                response.raise_for_status()
                exit(255)
        
        pages = response.json()
        #pprint(pages)
        if not pages:
            print("No pages")
            break

        gists.extend(pages)
        #print(f"Page number before increase {page_number}")
        page_number += 1
    
    return gists

def creat_configfile(config_file,first_time_stamp):
    with open(config_file, 'w') as open_file:
        open_file.write(first_time_stamp)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="Enter the github user to query")
    args = parser.parse_args()
    print(f"Using gihub user: {args.user}")

    gists = get_gists(args.user)
    #first_time_stamp = gists[0]['created_at']
    gist_creation_time = gists[0]['created_at']

    config_file = "./gist_" + args.user

    if not os.path.isfile(config_file):
        print("File doesn't exist, creating file")
       # creat_configfile(config_file,first_time_stamp)
        creat_configfile(config_file, gist_creation_time)
        # Loop through gists and print to the screen
        for page in gists:
            created_at = page['created_at']
            html_url = page['html_url']
            print(f"The gist was created on: {created_at} and the Gist URL is: {html_url}")
    else:
        print("File exists")
        with open(config_file, "r") as read_file:
            last_query = read_file.read()
            print(last_query)
        last_query = datetime.strptime(last_query,'%Y-%m-%dT%H:%M:%SZ')
        pprint(f"This is the last query: {last_query}")
        gist_created_date = datetime.strptime(gist_creation_time,'%Y-%m-%dT%H:%M:%SZ')
        pprint(f"This is the last query: {gist_created_date}")

        if gist_created_date > last_query:
            pprint("New gists")
            for page in gists:
                created_at = page['created_at']
                html_url = page['html_url']
                print(f"The gist was created on: {created_at} and the Gist URL is: {html_url}")
        else:
            pprint("No new gists")



    #print(gists)
"""
    for page in gists:
            created_at = page['created_at']
            html_url = page['html_url']
            #print(f"The gist was created on: {page['created_at']} and the Gist URL is: {page['html_url']}")
            print(f"The gist was created on: {created_at} and the Gist URL is: {html_url}")
"""

"""
    gists = []
    # Test gihub user PlugFox
    github_user = args.user
    gist_api = 'https://api.github.com/users/' + github_user + '/gists'
    response = requests.get(gist_api)
    print(f"The response is: {response.status_code}")


    pages = response.json()
    print(f"The creation time is: {pages[0]['created_at']}")

    # #    print("The") 
    if response.status_code != 200:
        if response.status_code == 404:
            print("The page was not found")
    else:
        for page in pages:
            created_at = page['created_at']
            html_url = page['html_url']
            print(f"The gist was created on: {page['created_at']} and the Gist URL is: {page['html_url']}")
            print(f"The gist was created on: {created_at} and the Gist URL is: {html_url}")
"""

if __name__ == "__main__":
    main()