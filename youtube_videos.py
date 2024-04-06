import yt_dlp
import os


def download_youtube_videos(playlist_url):
    download_videos = "downloads_videos"
    os.makedirs(download_videos, exist_ok=True)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': os.path.join("download_videos", '%(playlist_title)s', '%(title)s.%(ext)s')
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
        print("Video downloaded")
