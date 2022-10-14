# JSON = JavaScript Object Notation (currently language agnostic)
import json #comes from Python native library, no need to pip install
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#print(response.json())
#print(json.dumps(response.json(), indent=2))    # pretty print for JSON results

o = response.json()
for result in o["results"]:
    print(result["trackName"])
