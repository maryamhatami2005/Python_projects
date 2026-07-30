import argparse
from pathlib import Path

from tqdm import tqdm
from yt_dlp import YoutubeDL


class YouTubeDownloader:
    def __init__(self, output_path= None, quality= None):
        self.output_path = output_path or Path.cwd()
        self.quality = quality or "720"
        self.pbar = None

    def progress_hook(self, d):
        if d['status'] == "downloading":

            if self.pbar is None:
                total = d.get("total_bytes")
                self.pbar = tqdm(total=total, desc="Downloading...", unit="B", unit_scale= True)
                
            self.pbar.n = d["downloaded_bytes"]
            self.pbar.refresh()
            
        elif d["status"] == "finished":
                    if self.pbar:
                        self.pbar.close()
                        self.pbar = None
        
                    tqdm.write("Download complete!")


    def download_video(self, url):
        ydl_opts = {
            "format" : f"bestvideo[height<={self.quality}]+bestaudio", 
            "outtmpl" : f"{self.output_path}/%(title)s.%(ext)s", 
            "merge_output_format": "mp4",
            "progress_hooks": [self.progress_hook],
            "cookiefile": "cookies.txt", 
            "noprogress": True,
            #"quiet": True
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


    def download_audio(self, url):
        ydl_opts = {
            "format": "bestaudio",
            "outtmpl": f"{self.output_path}/%(title)s.%(ext)s",
            "progress_hooks": [self.progress_hook],
            "cookiefile": "cookies.txt",
            "noprogress": True,
            #"quiet": True,
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

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(
        description= "YouTube Downloader"
    )


    parser.add_argument( "-u", "--url",  help= "YouTube video URL", default=None)
    parser.add_argument("-q", "--quality", help= "Video quality",type=int,  default= 720)
    parser.add_argument("-o", "--output", help="Output path", default=None)
    parser.add_argument("-a", "--audio",action="store_true", help="Download audio only")

    args= parser.parse_args()
    downloader= YouTubeDownloader(
    quality= args.quality,
    output_path=args.output)

    if args.audio:
        downloader.download_audio(args.url)
    else:
        downloader.download_video(args.url)