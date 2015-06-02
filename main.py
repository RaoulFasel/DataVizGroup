__author__ = 'raoul'
import urllib3
import json
import csv
results = []

def get_request(url):
    http = urllib3.PoolManager()
    r =  http.request('GET', url)
    return json.loads(r.data.decode('utf8'))

print("name, price")

top = get_request("http://steamspy.com/api.php?request=top100forever")

csvfile = open('test.csv', 'w', newline='')
csvwriter = csv.writer(csvfile, dialect='excel')

for x in top:
    data = []
    bb = get_request("http://store.steampowered.com/api/appdetails/?appids="+x)
    #print(json.dumps(bb, sort_keys=True, indent=4, separators=(',', ': ')))
    try:

        data.append(bb[x]['data']["name"])
        data.append(bb[x]['data']["price_overview"]["initial"])
        data.append(bb[x]['data']["price_overview"]["final"])
        genres = []
        for x in bb[x]['data']["genres"]:
            genres.append(x["description"])
        data.append(genres)


        print(data)
        results.append(data)



    except (KeyError,TypeError):
        pass
        #print(bb)
print(results)
print(type(results))
csvwriter.writerows(results)
