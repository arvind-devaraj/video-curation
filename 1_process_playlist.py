import googleapiclient.discovery
from urllib.parse import parse_qs, urlparse

#extract playlist id from url
url = 'https://www.youtube.com/playlist?list=PL4nM95iGmzlRNdkrxhfO3jeomV4F50VIJ'
query = parse_qs(urlparse(url).query, keep_blank_values=True)
playlist_id = query["list"][0]

#print(f'get all playlist items links from {playlist_id}')
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = "AIzaSyBaEPvee-oQ2VL0aK0zQ2fZgUlX7EFzXjY")

request = youtube.playlistItems().list(
    part = "snippet",
    playlistId = playlist_id,
    maxResults = 10000
)
response = request.execute()

playlist_items = []
while request is not None:
    response = request.execute()
    playlist_items += response["items"]
    request = youtube.playlistItems().list_next(request, response)

#print(f"total: {len(playlist_items)}")
# print([ 
#     f'https://www.youtube.com/watch?v={t["snippet"]["resourceId"]["videoId"]}&list={playlist_id}&t=0s'
#     for t in playlist_items
# ])
res=[f'{t["snippet"]["resourceId"]["videoId"]}' for t in playlist_items]

for item in res:
    print(item)

