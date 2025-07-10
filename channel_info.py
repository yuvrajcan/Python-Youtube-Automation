from pyyoutube import api
api_key = 'your_api_key'
channel_id = UCpnBlAPe8qz5JDM36nOqyTA
api = Api(api_key=api_key)
channel_info = api.get_channel_info(channel_id=channel_id)
print(channel_info.items[0].to_dict())
channel_data = channel_info.items[0].to_dict()
print(channel_data['statistics']['viewCount'])
print(channel_data['statistics']['subscriberCount'])
print(channel_data['statistics']['videoCount'])
print('channel description: ', channel_data['statistics']['description'])