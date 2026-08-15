import os
import yagmail


def send_email(to, subject, contents, attachments=None):
    """
    Send an email using yagmail, with sender credentials from environment variables.

    Parameters:
    - to (str or list): The email address(es) of the to(s)
    - subject (str): The subject of the email
    - contents (str or list): The contents of the email
    - attachments (str or list, optional): Path(s) to file(s) to be attached

    Returns:
    - bool: True if the email was sent successfully, False otherwise
    """
    try:
        # Get sender credentials from environment variables
        sender_email = os.environ.get('EMAIL_SENDER')
        sender_password = os.environ.get('EMAIL_PASSWORD')

        if not sender_email or not sender_password:
            raise ValueError("Sender email or password not found in environment variables")

        # Initialize the SMTP
        yag = yagmail.SMTP(sender_email, sender_password)


        # Send the email
        yag.send(
            to=to,
            subject=subject,
            contents=contents,
            attachments=attachments
        )

        print("Email sent successfully")
        return True

    except Exception as e:
        print(f"An error occurred while sending the Email: {str(e)}")
        return False

    finally:
        # close the connection
        if "yag" in locals():
            yag.close()