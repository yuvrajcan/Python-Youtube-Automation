import pandas as pd
from pyyoutube import api
api_key = 'your_api_key'
channel_id = UCpnBlAPe8qz5JDM36nOqyTA
api = Api(api_key=api_key)
channel_info = api.get_channel_info(channel_id=channel_id)

def get_all_video_links(api,channel_id):
    total_links = []
    total_playlist = api.get.playlists(channel_id=channel_id , count=None)
    playlist_size = len(total_playlist.items)
    
    playlists = total_playlist.items
    for i in range(0,playlist_size):
        all_playlist_videos = api.get_playlist_items(playlist_id=playlists[i].id, count=None)
        num_of_items = len(all_playlist_videos.items)
        for j in range(0,num_of_items):
            item_by_id = api.get_playlist_item_by_id(playlist_item_id = all_playlist_videos.items[j].id)
            for k in range (0,len(item_by_id.items)):
                total_links.append(item_by_id.items[k].snippet.resourceId.videoId)
    return total_links   

def video_data(api , total_links):
    df = pd.dataframe(columns = ['title',  'viewCount', 'likeCount', 'commentCount' , 'video_links'])
    for i in total_links:
        video_by_id = api.get_video_by_id(video_id = i)
        if video_by_id.items != []:
            video_details = video_by_id.items[0].to_dict()
            df = df.append({
                'title': video_details['snippet']['title'],
                'viewCount': video_details['statistics']['viewCount'],
                'likeCount': video_details['statistics']['likeCount'],
                'commentCount': video_details['statistics']['commentCount'],
                'video_links': video_details['snippet']['resourceId']['videoId']
            }, ignore_index=True)
    return df

total_links = get_all_video_links(api, channel_id)
df = video_data(api, total_links)
df.to_csv('video_data.csv') 

            
        
        