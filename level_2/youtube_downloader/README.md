# YouTube Downloader

A simple command-line YouTube downloader built with Python and `yt-dlp`.

## Features

* Download YouTube videos
* Choose video quality
* Download audio as MP3
* Choose an output directory
* Display download progress
* Handle download errors

## Requirements

* Python 3
* `yt-dlp`
* `tqdm`
* FFmpeg

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Install FFmpeg separately and make sure it is available in your `PATH`.

## Usage

The main program is `src/main.py`.

### Download a video

```bash
python src/main.py -u "YOUTUBE_URL"
```

By default, the maximum quality is 720p.

### Choose quality

```bash
python src/main.py -u "YOUTUBE_URL" -q 1080
```

### Download audio

```bash
python src/main.py -u "YOUTUBE_URL" -a
```

Audio is converted to MP3 at 320 kbps.

### Choose output directory

```bash
python src/main.py -u "YOUTUBE_URL" -o "downloads"
```

Options can also be combined:

```bash
python src/main.py -u "YOUTUBE_URL" -q 1080 -o "downloads"
```



## Project Structure

```text
.
├── argparse/
├── pbar/
├── src/
│   ├── main.py
│   └── test.ipynb
├── README.md
└── requirements.txt
```

`argparse/` and `pbar/` contain experiments and tests developed during the project.
