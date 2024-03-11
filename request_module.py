import requests
import json
import string
import random

# base url
base_url = "https://gorest.co.in"

# autorization
auth_token = "Bearer 3e6cc7350b04c6d1ce3ffea7cf130a61de660f3fc89bac015ec64acf27b77169"

#get random email id:
def generate_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email = random_string + "@" + domain
    return email


# get request

def get_function():

    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers= headers)
    assert response.status_code == 200
    # data = json.loads(response.text)
    
    a = response.json()
    a = json.loads(response.text)
    print(a)
    json_str = json.dumps(a, indent=10)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")


# post method

def post_function():
    url = base_url + "/public/v2/users"
    headers = {"Authorization": auth_token}
    data = {
        "name": "Dr. Adityanandana Menon",
        "email": "menon_dr_adityanandana_06@gerhold.example",
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    a = response.json()
    json_str = json.dumps(a, indent=4)
    print("json POST response body: ", json_str)

    user_id = a["id"]
    assert response.status_code == 201
    assert "name" in a
    assert a["name"] == "Dr. Adityanandana Menon"
    print(".......POST/Create USER IS DONE.......")
    print(".......=====================.......")
    return user_id

# put method
def put_function(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers = {"Authorization": auth_token}
    data = {
        "name": "Dr. Nirav Menon",
        "email": "menon_dr_adityanandana_96@gerhold.example",
        "gender": "male",
        "status": "active"
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    a = response.json()
    json_str = json.dumps(a, indent=4)
    print("json PUT response body: ", json_str)
    assert a["id"] == user_id
    assert a["name"] == "Dr. Nirav Menon"
    print(".......PUT/Update USER IS DONE.......")
    print(".......=====================.......")

# DELETE method 

def delete_function(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print(".......DELETE USER IS DONE.......")
    print(".......=====================.......")



# call requests

get_function()
# user_id = post_function()
# put_function(user_id)
# delete_function(user_id)
