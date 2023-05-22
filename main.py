# Import Python packages
from email.mime.text import MIMEText
import smtplib
import json
import requests

# Send API request for a random poem
json_data = requests.get('https://poetrydb.org/random').json()

# Extract the poem details from the JSON response
title = json_data[0]['title']
author = json_data[0]['author']
line_count = json_data[0]['linecount']
lines = ''
for line in json_data[0]['lines']:
  lines = lines + line + "\n"

# A test print() statement to ensure the request and parsing processed the data 
# correctly
# print(title, "\n", author, "\n\n", lines)

msg_body = title + "\n" + author + "\n\n" + lines

# Create plaintext message container
msg = MIMEText(msg_body)

# Prepare the metadata of the message
sender_email = ''
recipient_emails = ''
msg['Subject'] = 'Your Daily Poem (' + line_count + ' lines)'
msg['From'] = sender_email
msg['To'] = recipient_email

# Send the message via our own SMTP server, but don't include the
# envelope header.
smtp_server = 'localhost'
s = smtplib.SMTP(smtp_server)
s.sendmail(sender_email, [recipient_emails], msg.as_string())
s.quit()
