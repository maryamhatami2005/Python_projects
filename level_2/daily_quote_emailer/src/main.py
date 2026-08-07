import csv
import os
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = "maryhatami2005@gmail.com"
password = os.getenv("PASSWORD")

csv_file_path = "recipients.csv"
quotes_file_path = "quotes.txt"


def load_quotes(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

quotes = load_quotes(quotes_file_path)


def send_email(recipient_name, recipient_email, quote):
    sbj = "Your Daily Inspirational quote"
    body = f"Hello {recipient_name}, here is your daily inspirational quote:\n\n {quote}"


    msg = MIMEMultipart()
    msg["From"] = sender
    msg['To'] = recipient_email
    msg["Subject"] = sbj

    msg.attach(MIMEText(body, "plain"))

    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender, password)
        text = msg.as_string()
        session.sendmail(sender, recipient_email, text)
        session.quit()
        print(f"Mail Sent Successfully to {recipient_name} ({recipient_email})")

    except Exception as e:
        print(f"Failed to send email to {recipient_name} ({recipient_email}). Error: {e}")


if __name__ == "__main__":

    quotes = load_quotes(quotes_file_path)

    with open(csv_file_path, mode="r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            recipient_name = row["name"]
            recipient_email = row["email"]

            quote_of_the_day = random.choice(quotes)
            send_email(
                recipient_name,
                recipient_email,
                quote_of_the_day
            )


