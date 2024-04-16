import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.

outfile = open('hn.json', 'w')

json.dump(r.json(),outfile,indent=4)

submission_ids = r.json()

url = 'https://hacker-news.firebaseio.com/v0/item/40053774.json'
r = requests.get(url)

outfile = open('hn2.json','w')

json.dump(r.json(), outfile, indent=4)

response_dict = r.json()

print(f"Title: {response_dict['title']}")
print(f"URL: {response_dict['url']}")
print(f"Comments: {response_dict['descendants']}")


for subid in submission_ids[:10]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{subid}.json'
    r = requests.get(url)
    response_dict = r.json()
    print(f"Title: {response_dict['title']}")
    print(f"URL: {response_dict['url']}")
    if 'descendants' in response_dict:
        print(f"Comments: {response_dict['descendants']}")

    print()
    print()

