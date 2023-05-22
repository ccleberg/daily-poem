# Daily Poem

This is a simple Python program to request a random poem from the 
[PoetryDB API](https://github.com/thundercomb/poetrydb) and email it to 
configurable email addresses.

## Prerequisites

In order to run this program, you must have a compatible version of Python 
installed. You must also have a way to send emails, such as the `mailutils` 
package on Debian.

## Set-Up & Running

First, clone the repository and enter the directory:

```bash
git clone <REPO_URL>
cd daily-poem
```

Next, install the required Python packages:

```bash
pip install -r requirements.txt
```

Finally, you will need to edit the `main.py` file and replace the following 
variables with your own values:

- `sender_email`: Enter the email address you want the emails to be sent 
from; e.g., `my_user@server.local`
- `recipient_emails`: Enter the email addresses that the poem will be sent to, 
in the form of a list; e.g., `['user1@example.com', 'user2@example.com']`
- `smtp_server`: The SMTP server you want to user, defaults to `localhost`.

Once the variables are updated, you may run the script:

`python main.py`
