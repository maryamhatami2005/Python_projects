# Currency Converter

A simple currency converter built with Python and `Streamlit` using real-time exchange rates from ExchangeRate-API.

## Features

* Convert between different currencies
* Use real-time exchange rates
* Automatically update conversions
* Cache exchange rates for 3 hours

## Requirements

* Python 3
* `streamlit`
* `requests`
* `cachetools`

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Run the Streamlit app

```bash
streamlit run src/app.py
```


### Command Line

You can also run the converter directly from the terminal:

```bash
python src/currency_converter.py
```


## Project Structure

```text
.
├── src/
│   ├── app.py
│   ├── constants.py
│   ├── currency_converter.py
│   └── image.jpg
├── README.md
└── requirements.txt
```
