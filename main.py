__author__ = 'raoul'
import urllib3
import json
import csv
results = []

def get_request(url):
    http = urllib3.PoolManager()
    r =  http.request('GET', url)
    return json.loads(r.data.decode('utf8'))

header = "name, price, genres, metacritic, release, likes, achievements, linux, mac, windows, owners, players_forever, players_2weeks, average_forever, average_2weeks,median_forever,median_2weeks"
print(header)

top = get_request("http://steamspy.com/api.php?request=top100forever")

csvfile = open('test.csv', 'w', newline='')
csvwriter = csv.writer(csvfile, dialect='excel')

for x in top:
    data = []

    bb = get_request("http://store.steampowered.com/api/appdetails/?appids="+x)
    try:

        data.append(bb[x]['data']["name"])
        data.append(bb[x]['data']["price_overview"]["initial"])
        genres = []
        for y in bb[x]['data']["genres"]:
            genres.append(y["description"])
        print(genres)
        data.append(genres)

        data.append(bb[x]['data']["metacritic"]["score"])
        data.append(bb[x]['data']["release_date"]["date"])
        data.append(bb[x]['data']["recommendations"]["total"])
        data.append(bb[x]['data']["achievements"]["total"])
        data.append(bb[x]['data']["platforms"]["linux"])
        data.append(bb[x]['data']["platforms"]["mac"])
        data.append(bb[x]['data']["platforms"]["windows"])
        data.append(top[x]["owners"])
        data.append(top[x]["players_forever"])
        data.append(top[x]["players_2weeks"])
        data.append(top[x]["average_forever"])
        data.append(top[x]["average_2weeks"])
        data.append(top[x]["median_forever"])
        data.append(top[x]["median_2weeks"])
        print(data)
        results.append(data)



    except (KeyError,TypeError):
        pass
        print("error")
print(results)
print(type(results))
csvfile.write(header)
csvwriter.writerows(results)
