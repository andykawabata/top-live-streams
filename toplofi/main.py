from apiclient.discovery import build

toplofi_api_key = ""

def getStreams(api_key=toplofi_api_key, maxResults=25):
    streams = []
    youtube = build("youtube", "v3", developerKey=api_key)

    thisPageResponse = youtube.search().list(
        part="snippet",
        eventType="live",
        maxResults=maxResults,
        order="viewCount",
        q="lofi",
        type="video"
    ).execute()

    streamsResponse = thisPageResponse["items"]

    rank = 1

    for stream in streamsResponse:
        title = stream["snippet"]["title"]
        channelTitle = stream["snippet"]["channelTitle"]
        videoId = stream["id"]["videoId"]
        URL = "https://www.youtube.com/watch?v=" + videoId
        channelId = stream["snippet"]["channelId"]
        channelURL = "https://www.youtube.com/channel/" + channelId
        fullDate = stream["snippet"]["publishedAt"]
        date = fullDate[:10]

        viewerDetailsResponse = youtube.videos().list(
            id=videoId,
            part="snippet, liveStreamingDetails"
        ).execute()

        detailsResponse = viewerDetailsResponse["items"]

        for detail in detailsResponse:
            try:
                viewers = "{:,}".format(int(detail["liveStreamingDetails"]["concurrentViewers"]))
                thumbnail = detail["snippet"]["thumbnails"]["maxres"]["url"]
                liveChatId = detail["liveStreamingDetails"]["activeLiveChatId"]
                liveChatURL = "https://www.youtube.com/live_chat?v=" + liveChatId
            except KeyError as e:
                viewers = 0
                thumbnail = "None"
                liveChatURL = "None"


        streamData = {
            "Rank": rank,
            "Title": title,
            "Channel": channelTitle,
            "URL": URL,
            "ChannelURL": channelURL,
            "Viewers": viewers,
            "PublishedAt": date,
            "Thumbnail": thumbnail,
            "liveChatURL": liveChatURL
        }

        streams.append(streamData)

        rank += 1

    return streams
