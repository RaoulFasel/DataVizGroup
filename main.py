__author__ = 'raoul'
import urllib3
import json

def get_request(url):
    http = urllib3.PoolManager()
    r =  http.request('GET', url)
    return json.loads(r.data.decode('utf8'))

top = get_request("http://steamspy.com/api.php?request=top100forever")

for x in top:
    bb = get_request("http://store.steampowered.com/api/appdetails/?appids="+x)
    print(json.dumps(bb, sort_keys=True, indent=4, separators=(',', ': ')))

