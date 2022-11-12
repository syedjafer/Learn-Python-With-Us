import requests
import json

url='https://api.qrserver.com/v1/create-qr-code/'
texttoprint=input("Enter the text you want to create QR: ")
query = {
    'size': '600x600',
    'data':texttoprint
}

data = requests.get(url, params=query)
data=list(data)
with open('content.jpg', 'wb') as f:
    for line in data:
        f.write(line)
