import requests

username = "thanhdatuet2003"
password = "fuckyoubitch"

login_url = "http://127.0.0.1:8000/api/login/"


for id in range(110, 1000):
    curr_username = username + str(id)
    curr_password = password + str(id)
    
    response = requests.post(
        url=login_url, 
        data = {
            'username':curr_username,
            'password':curr_password
        }
    )
    
    # print(response.json())

    