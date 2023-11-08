# main.py
import pandas as pd
from jinja2 import Template
import requests

api_key = 'YOUR-API-KEY-HERE'
from_name = 'YOUR-COMPANY'
from_address = 'YOUR-EMAIL-ADDRESS'

customers = pd.read_excel('list.xlsx')

with open('content.html', 'r', encoding='utf-8') as file:
    html_template = Template(file.read())

def send_email(recipient_email, recipient_name, subject, html_content, unsubscribe_link):
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json',
    }
    data = {
        "subject": subject,
        "fromName": from_name,
        "fromAddress": from_address,
        "content": html_content,
        "unsubscribedLink": unsubscribe_link,
        "recipients": [{"address": recipient_email, "name": recipient_name}]
    }
    response = requests.post('https://mail.surenotifyapi.com/v1/messages', headers=headers, json=data)
    return response.json()

for index, customer in customers.iterrows():
    unsubscribe_link = "YOUR-LINK"
    personalized_content = html_template.render(
        name=customer['Name'],
        email=customer['Email']
    )
    subject = 'YOUR-EMAIL-TITLE'
    response = send_email(customer['Email'], customer['Name'], subject, personalized_content, unsubscribe_link)
    if 'success' in response:
        success_info = response['success'][0]
        print(f"Email to {customer['Email']}: Sent successfully with ID {success_info['id']}")
    elif 'failure' in response:
        failure_info = response['failure']
        print(f"Email to {customer['Email']}: Failed to send email, reason: {failure_info}")
    else:
        print(f"Email to {customer['Email']}: Failed to send email, unexpected response")
