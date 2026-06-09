# Look API (Application Programming Interface) - It goes to a file in browser and fetches a particular data from a website already existing on a browser. But it can only be done on a browser. So we use the requests package which helps us pretends as a browser by our code and make http requests for api to fetch data. The fetched data is in JSON format.

# to install requests - pip install requests

# json is also a module that comes already when python was dounloaded hence no need to pip install. It formats the json document into a more pretty format thats understandable.

import json 
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1-50&term=" + sys.argv[1])

# print(json.dumps(response.json(), indent = 2))

o = response.json()

for result in o["results"]:
    print(result["trackName"])

