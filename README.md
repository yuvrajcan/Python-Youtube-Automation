#  YouTube Channel Analytics Extractor 📊

Python scripts to extract video, playlist, and channel data using the YouTube Data API.

## 🔍 Features

- **Channel Info** (`channel_info.py`)  
  Fetch subscriber count, total views, and video count.

- **Playlist Info** (`playlist_info.py`)  
  List all playlists, number of videos, and their titles.

- **Video Statistics** (`video_stats.py`)  
  View counts, likes, comments, and titles from playlists.

- **Bulk Data Export** (`data_extraction.py`)  
  Extracts video metadata and exports it to `video_data.csv`.

## 📦 Requirements

- Python 3.7+
- `pyyoutube`, `pandas`

```bash
pip install pyyoutube pandas
🔐 Setup
Replace your_api_key and channel_id in each script:

python
Copy
Edit
api_key = 'YOUR_YOUTUBE_DATA_API_KEY'
channel_id = 'UCxxxxxxxxxxxxxxxxx'
📈 Output
Clean CSV with video titles, views, likes, and comments

Readable print outputs for quick debugging

⚠️ Notes
Make sure the API key has access to YouTube Data v3

Use .env and dotenv for key security in production

📜 License
Open-source under MIT.
