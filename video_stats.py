from pyyoutube import api
api_key = 'your_api_key'
channel_id = UCpnBlAPe8qz5JDM36nOqyTA
api = Api(api_key=api_key)
channel_info = api.get_channel_info(channel_id=channel_id)


playlist_info = api.get_playlists(channel_id=channel_id)

playlist_info_by_id = api.get_playlist_by_id(playlist_id=playlist_info.items[0].id)
one_playlist_info = playlist_info_by_id.items[0].to_dict()
item_by_playlist_id = api.get_playlist_items(playlist_id=playlist_info.items[0].id)
item_by_playlist_id.items[0].to_dict()
playlist_item_by_id = api.get_playlist_item_by_id(playlist_item_id = item_by_playlist_id.items[0].to_dict())

v = playlist_item_by_id.items[0].to_dict()
videoID = v['snippet']['resourceId']['videoId']

video_by_id = api.get_video_by_id(video_id = videoID)
video_details = video_by_id.items[0].to_dict()
video_details
print('title of the video : ', video_details['snippet']['title'])
print('number of views : ', video_details['statistics']['viewCount'])
print('number of likes : ', video_details['statistics']['likeCount'])
print('number of dislikes : ', video_details['statistics']['dislikeCount'])
print('number of comments : ', video_details['statistics']['commentCount'])
