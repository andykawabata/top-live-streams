from googleapiclient.discovery import build
from flask import Flask, render_template


IDS = [ "hHW1oY26kxQ",
        "SmbdY5FpRwA",
        "bebuiaSKtU4",
        "NAzwWDX1PMU",
        "yPLLhlX0YXM",
        "2atQnvunGCo",
        "W9CLdkkNn20",
        "DHB42n9n6pA",
        "F0IbjVq-fgs",
        "udj7MHnXfcI",
        "KC3sfZBmn-o",
        "pYxOqlyIRpI",
        "pOxXgtLdvG8",
        "IjMESxJdWkg",
        "qK9OLRbAW30",
        "B8tQ8RUbTW8",
        "B2Y1IWddruk",
        "3cPoR04BJsA",
        "o_2mx5oFOqQ",
        "mBuPu09IdkQ",
        "g-pqmuYPHPs"]

#put id's int a single string separated by commas. remove the comma from the end of final string.

ID_string = ""
for this_id in IDS:
    ID_string += this_id + ", "
ID_string = ID_string[:-2]


app = Flask(__name__)

@app.route('/')
def home():
    api_key = "AIzaSyBK8ibmhkd_q4MZz2O-rQk_t7fYMkvv9G4"
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.videos().list(id= ID_string, part='snippet, liveStreamingDetails')
    response = request.execute()
    items = response['items']

    custom_item_list = []

    index = 0
    for item in items:
        title = item['snippet']['title']
        viewers = item['liveStreamingDetails']['concurrentViewers']
        thumb = item['snippet']['thumbnails']['default']['url']
        channel = item['snippet']['channelTitle']
        url = "https://www.youtube.com/watch?v=" + IDS[index]
        custom_item_list.append({'title': title, 
                                 'viewers': int(viewers), 
                                 'thumb': thumb, 
                                 'channel': channel, 
                                 'url': url})
        index += index

    def item_sort(video):
        return video['viewers']

    custom_item_list.sort(key=item_sort, reverse=True)

    return render_template('template.html', len=len(custom_item_list), stream_list=custom_item_list)


app.run(debug=True)


