# Python SMTP Email Sender

This Python program demonstrates how to send SMTP emails using Python. It utilizes the smtplib library to establish a connection to an SMTP server, and the email.mime modules to create and format the email message.

## Features

- Loads email credentials from environment variables using dotenv.
- Reads email content from a template file and substitutes variables using string.Template.
- Attaches plain text content to the email message using email.mime.text.
- Sends the email message using the specified SMTP server and port.
- Uses TLS encryption for secure communication with the SMTP server.

## Usage

- Install the required Python packages listed in requirements.txt.
- Set up environment variables for the email sender address and password.
- Customize the email template and content in the file100.txt.
- Run the Python script to send the email.
