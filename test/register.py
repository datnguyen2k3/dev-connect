import requests

url = "http://127.0.0.1:8000/api/register/"
username = "thanhdatuet2003"
password = "fuckyoubitch"

for id in range(110, 1000):
    curr_username = username + str(id)
    curr_password = password + str(id)
    curr_email = username + str(id) + "@gmail.com"

    data = {
        'username':username + str(id), 
        'first_name' : "Dat" + str(id),
        'last_name': "Nguyen", 
        'email':username + str(id) + "@gmail.com", 
        'password1':password + str(id), 
        'password2':password + str(id),
    }

    requests.put(url, data=data)
    