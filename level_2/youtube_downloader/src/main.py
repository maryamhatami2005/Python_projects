from yt_dlp import YoutubeDL
from pathlib import Path

class YouTubeDownloader:
    def __init__(self, output_path= None, quality= None):
        self.output_path = output_path or Path.cwd()
        self.quality = quality or "720"

    def download_video(self, url):
        ydl_opts = {
            "format" : f"bestvideo[height<={self.quality}]+bestaudio", 
            "outtmpl" : f"{self.output_path}/%(title)s.%(ext)s", 
            "merge_output_format": "mp4",
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


    def download_audio(self, url):
        ydl_opts = {
            "format": "bestaudio",
            "outtmpl": f"{self.output_path}/%(title)s.%(ext)s",
            "postprocessors":
            [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

if __name__ == "__main__":
    url = "https://youtu.be/GTWqwSNQCcg?si=zlC9j28Pu7G_pnEb"
    output_path = r"/mnt/c/Users/Dell/Downloads"
    yt = YouTubeDownloader(output_path=output_path)
    yt.download_audio(url)