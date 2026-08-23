# Fetch a random poem from PoetryDB and mail it.
import smtplib
from email.mime.text import MIMEText

import requests

POETRY_URL = "https://poetrydb.org/random"
SMTP_SERVER = "localhost"

# Fill these in before running.
SENDER_EMAIL = ""
RECIPIENT_EMAILS = ""


def fetch_poem(url=POETRY_URL):
    """Return (title, author, line_count, body) for a random poem."""
    json_data = requests.get(url, timeout=30).json()
    poem = json_data[0]
    lines = ""
    for line in poem["lines"]:
        lines = lines + line + "\n"
    return poem["title"], poem["author"], poem["linecount"], lines


def build_message(title, author, line_count, lines, sender, recipient):
    """Return a plaintext MIMEText message for one poem."""
    msg = MIMEText(title + "\n" + author + "\n\n" + lines)
    msg["Subject"] = "Your Daily Poem (" + line_count + " lines)"
    msg["From"] = sender
    msg["To"] = recipient
    return msg


def main():
    title, author, line_count, lines = fetch_poem()
    msg = build_message(
        title, author, line_count, lines, SENDER_EMAIL, RECIPIENT_EMAILS
    )

    # Send via the local SMTP server, without the envelope header.
    s = smtplib.SMTP(SMTP_SERVER)
    s.sendmail(SENDER_EMAIL, [RECIPIENT_EMAILS], msg.as_string())
    s.quit()


if __name__ == "__main__":
    main()
