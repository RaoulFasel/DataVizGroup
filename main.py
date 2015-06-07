__author__ = 'raoul'
import urllib3
import json
import csv
results = []

def get_request(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return json.loads(r.data.decode('ISO-8859-1'))

header = "name, price, genres, metacritic, release, likes, achievements, linux, mac, windows, image, owners, players_forever, players_2weeks, average_forever, average_2weeks,median_forever,median_2weeks"

top = get_request("http://steamspy.com/api.php?request=top100forever")

csvfile = open('test.csv', 'w', newline='')
csvwriter = csv.writer(csvfile, dialect='excel')

for x in top:
    data = []

    bb = get_request("http://store.steampowered.com/api/appdetails/?appids="+x)
    try:

        data.append(bb[x]['data']["name"])
        if bb[x]['data']['is_free']:
            data.append("free")
        else:
            data.append(bb[x]['data']["price_overview"]["initial"])
        genres = []
        for y in bb[x]['data']["genres"]:
            genres.append(y["description"])
        data.append(genres)
        if "metacritic" in bb[x]['data']:
            data.append(bb[x]['data']["metacritic"]["score"])
        else:
            data.append("Unkown")
        if "release_date" in bb[x]['data']:
            data.append(bb[x]['data']["release_date"]["date"])
        else:
            data.append("Unkown")
        data.append(bb[x]['data']["recommendations"]["total"])
        if "achievements" in bb[x]['data']:
            data.append(bb[x]['data']["achievements"]["total"])
        else:
            data.append("None")
        data.append(bb[x]['data']["platforms"]["linux"])
        data.append(bb[x]['data']["platforms"]["mac"])
        data.append(bb[x]['data']["platforms"]["windows"])
        if "header_image" in bb[x]['data']:
            data.append(bb[x]['data']["header_image"])
        else:
            data.append("none")






    except (KeyError, TypeError):
        print("error steam")
        print(x)

    try:
        data.append(top[x]["owners"])
        data.append(top[x]["players_forever"])
        data.append(top[x]["players_2weeks"])
        data.append(top[x]["average_forever"])
        data.append(top[x]["average_2weeks"])
        data.append(top[x]["median_forever"])
        data.append(top[x]["median_2weeks"])
    except (KeyError, TypeError):
        print("error steampsy")
        print(x)
    print(data)
    results.append(data)
print(results)
csvfile.write(header)
csvfile.write("\n")
csvwriter.writerows(results)
