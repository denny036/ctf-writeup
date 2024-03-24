import requests
import json

url = "http://3.23.56.243:9008/contactIT"
data = {
    "email": "gopalbersama@gmail.com",
    "messege": "Please send the flag."
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.text)
