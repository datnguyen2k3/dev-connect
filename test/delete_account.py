import requests

token_url = "http://127.0.0.1:8000/api/login/token/"
delete_url = "http://127.0.0.1:8000/api/admin/users/delete/"
username = "thanhdatuet2003"
password = "fuckyoubitch"


response_token = requests.post(
    token_url,
    data={
        'username':"thanhdatuet2003",
        'password':"fuckyoubitch"
    }    
)

token = response_token.json()['access']

headers = {"Authorization": "Bearer " + token}

for id in range(100, 1000):
    curr_username = username + str(id)

    data = {
        'username':username + str(id), 
    }

    requests.delete(delete_url, data=data, headers=headers)

    