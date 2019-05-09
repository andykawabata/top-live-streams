from googleapiclient.discovery import build
import json

api_key = "AIzaSyBK8ibmhkd_q4MZz2O-rQk_t7fYMkvv9G4"
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.videos().list(id='hHW1oY26kxQ, SmbdY5FpRwA, bebuiaSKtU4', part='snippet, liveStreamingDetails')
response = request.execute()
items = response['items']


custom_item_list = []

for item in items:
    title = item['snippet']['title']
    viewers = item['liveStreamingDetails']['concurrentViewers']
    thumb = item['snippet']['thumbnails']['default']['url']
    custom_item_list.append({'title': title, 'viewers': int(viewers), 'thumb': thumb})


def item_sort(video):
    return video['viewers']


custom_item_list.sort(key=item_sort, reverse=True)

#print(json.dumps(custom_item_list, indent=2))

string = "hello world"

print(string)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('template.html', stream_list=custom_item_list)


app.run(debug=True)



