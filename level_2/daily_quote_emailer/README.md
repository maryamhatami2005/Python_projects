# Daily Inspirational Quotes Emailer

This project is a Python script that automatically sends inspirational quotes to a list of subscribers via email. It reads recipient information from a CSV file, loads quotes from a text file, randomly selects a quote, and sends a personalized email to each recipient.

## Project Objective

The objective is to demonstrate a practical application of Python for email automation, including:

* Loading inspirational quotes from a `quotes.txt` file.
* Reading subscriber details from a CSV file.
* Randomly selecting a quote for each recipient.
* Personalizing emails with the recipient's name.
* Sending emails through Gmail's SMTP server.

## Requirements

* **Python 3.x**
* A **Gmail account**
* A Gmail **App Password**
* A `recipients.csv` file with the following format:

```csv
name,email
John Doe,johndoe@example.com
Jane Smith,janesmith@example.com
```

* A `quotes.txt` file containing one quote per line:

```text
Start where you are. Build from there.
Small steps still move you forward.
Progress matters more than perfection.
```

No external Python packages are required. The project uses Python's standard library.

## Setup and Configuration

### 1. Configure Gmail

Use a Gmail App Password for SMTP authentication rather than your regular Gmail password.

### 2. Set the Password

The script retrieves the password from the `PASSWORD` environment variable:

```python
password = os.getenv("PASSWORD")
```

Set this variable in your operating system before running the script.

### 3. Project Structure

```text
daily_quote_emailer/
├── main.py
├── recipients.csv
├── quotes.txt
└── README.md
```

## Running the Script

Run the following command from the project directory:

```bash
python main.py
```

The script will read the subscribers, randomly select a quote for each recipient, and send the personalized emails through Gmail's SMTP server.
