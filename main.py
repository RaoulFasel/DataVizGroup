__author__ = 'raoul'
import urllib3
import json
import csv
results = []

def get_request(url):
    http = urllib3.PoolManager()
    r =  http.request('GET', url)
    return json.loads(r.data.decode('utf8'))

header = "name, price, genres, metacritic, release, likes, achievements, linux, mac, windows"
print(header)

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
        genres = []
        for y in bb[x]['data']["genres"]:
            genres.append(y["description"])
        data.append(genres)

        data.append(bb[x]['data']["metacritic"]["score"])
        data.append(bb[x]['data']["release_date"]["date"])
        data.append(bb[x]['data']["recommendations"]["total"])
        data.append(bb[x]['data']["achievements"]["total"])
        data.append(bb[x]['data']["platforms"]["linux"])
        data.append(bb[x]['data']["platforms"]["mac"])
        data.append(bb[x]['data']["platforms"]["windows"])
        print(data)
        results.append(data)



    except (KeyError,TypeError):
        pass
        print("error")
print(results)
print(type(results))
csvwriter.writerows(results)
