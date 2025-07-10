from pyyoutube import api
api_key = 'your_api_key'
channel_id = UCpnBlAPe8qz5JDM36nOqyTA
api = Api(api_key=api_key)
channel_info = api.get_channel_info(channel_id=channel_id)


playlist_info = api.get_playlists(channel_id=channel_id)
# playlist_info.items[1].to_dict()
# playlist_info.items[0].id
for i in range(0, len(playlist_info.items)):
    playlist_info_by_id = api.get_playlist_by_id(playlist_id=playlist_info.items[i].id)
    one_playlist_info = playlist_info_by_id.items[0].to_dict()
    print('name of playlist: ',one_playlist_info['snippet']['title'])
    print('number of videos: ' , one_playlist_info['contentDetails']['itemCount'])
