# Website Availability Checker

A Streamlit app that checks whether a list of websites are reachable. Paste in URLs, one per line, and get a table showing which ones respond with HTTP 200 and which don't.

## Features

- Bulk URL input via a text area (one URL per line)
- Concurrent checks using a thread pool (up to 20 workers) for fast results on large lists
- Results displayed in a sortable table (Website / Status)

## Requirements

- Python 3.8+
- `streamlit`
- `requests`
- `pandas`

## Installation

```bash
pip install streamlit requests pandas
```

## Usage

```bash
streamlit run app.py
```


## How it works

1. Input is split into lines, trimmed of whitespace, and blank lines are discarded.
2. Any URL without `http://` or `https://` gets `https://` prepended.
3. Each URL is checked via a `GET` request (5-second timeout, browser-like `User-Agent` header) in a separate thread.
4. A site is marked **Available** if the response status code is 200; any other status code, or any request exception (timeout, connection error, DNS failure, etc.), marks it **Unavailable**.
5. Results are collected into a pandas DataFrame and rendered as a table.
