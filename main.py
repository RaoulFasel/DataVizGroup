__author__ = 'raoul'
import urllib3
import json
import csv
results = []

def get_request(url):
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    return json.loads(r.data.decode('ISO-8859-1'))

header = "name, price, genre1, genre2, genre3, genre4, metacritic, release, likes, achievements, linux, mac, windows, image, owners, players_forever, players_2weeks, average_forever, average_2weeks,median_forever,median_2weeks"

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

        genre_length = len(bb[x]['data']['genres'])
        if genre_length>4:
            genre_length=4

        for y in range(genre_length):
            data.append(bb[x]['data']['genres'][y]["description"])
        for y in range(4-genre_length):
            data.append("")

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
    #print(data)
    results.append(data)
#print(results)
csvfile.write(header)
csvfile.write("\n")
csvwriter.writerows(results)
json_data = []
for x in results:
    #print(x)
    if len(x) > 18:
        item = {}
        item["name"] = x[0]
        item["price"] = x[1]
        item["genre"] = x[2]
        item["genre2"] = x[3]
        item["genre3"] = x[4]
        item["genre4"] = x[5]
        item["metacritic"] = x[6]
        item["release"] = x[7]
        item["likes"] = x[8]
        item["achievements"] = x[9]
        item["linux"] = x[10]
        item["mac"] = x[11]
        item["windows"] = x[12]
        item["image"] = x[13]
        item["owners"] = x[14]
        item["players_forever"] = x[15]
        item["players_2weeks"] = x[16]
        item["average_forever"] = x[17]
        item["average_2weeks"] = x[18]
        item["median_forever"] = x[19]
        item["median_2weeks"] = x[20]
        item["waste"] = (x[1]*(x[14]-x[15]))
        json_data.append(item)
for x in json_data:
    for y in x:
        if isinstance( x[y], str):
            if len(x[y])> 80:
                x[y] = ""

with open('data.json', 'w') as outfile:
    json.dump(json_data, outfile)