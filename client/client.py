import base64
import json
import requests

username = 'admin'
password = 'admin'

host = 'localhost'
port = 8000
base_url = 'http://' + host + ':' + str(port)

def get_auth_header():
    credentials = f"{username}:{password}".encode('utf-8')
    base64_credentials = base64.b64encode(credentials).decode('utf-8')
    headers = {
        'Authorization': f'Basic {base64_credentials}'
    }
    return headers


def get(url):
    response = requests.get(url, headers = get_auth_header())

    if response.status_code == 200:
        print("GET request was successful.")
        parsed_data = json.loads(response.text)
        print(json.dumps(parsed_data, indent=4))

    else:
        print(f"GET request failed with status code {response.status_code}")
    


def get_todo_list():
    get(base_url + '/api/todos')

def get_todo_item(id):
    get(base_url + '/api/todos/' + str(id))



def post(url, data):
    json_data = json.dumps(data)
    headers = get_auth_header()
    headers['Content-Type'] =  'application/json'
    response = requests.post(url, data=json_data, headers=headers)

    if response.status_code == 201:
        print("POST request was successful.")
        print(response.text)
    else:
        print(f"POST request failed with status code {response.status_code}")

def post_todo_item(id):
    
    data = {
        "task": "New Task" + str(id),
        "completed": True,
    }
    post(base_url + '/api/todos', data)

def put(url, data):
    json_data = json.dumps(data)
    headers = get_auth_header()
    headers['Content-Type'] =  'application/json'
    response = requests.put(url, data=json_data, headers=headers)

    if response.status_code == 200:
        print("PUT request was successful.")
        print(response.text)
    else:
        print(f"PUT request failed with status code {response.status_code}")

def modify_item_id(id):
    data = {
        "task": "Old Task" + '-modified', 
        "completed": True,
    }
    put(base_url + '/api/todos/' + str(id) + '/', data)

def delete(url):
    response = requests.delete(url, headers=get_auth_header())
    if response.status_code == 200:
        print("DELETE request was successful.")
        print(response.text)
    else:
        print(f"DELETE request failed with status code {response.status_code}")

def delete_item(id):
    delete(base_url + '/api/todos/' + str(id) + '/')


# get_todo_list()

# get_todo_item(id)
# modify_item_id(id)
# get_todo_item(id)


#delete_item(id)
