import requests

url="https://jsonplaceholder.typicode.com/posts"


data={
    "userId": 10,
    "id": 100000,
    "title":"Tests",
    "body": "Testing ways they do not know he very pleasure is therefore called an error in\the sailor who is less great and distinguished him\let us accuse him by reason of error or"
  }

response=requests.post(url, json=data)

if response.status_code == 201:
    new_post = response.json()
    print("New Post created: ",new_post)
    
else:
    print("Failed to create a post")