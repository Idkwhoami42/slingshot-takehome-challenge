import requests
from requests.models import Response

serverip = 'localhost:5000'

def insert(keyword):
    response = requests.post(rf'http://{serverip}/insert?keyword={keyword}')
    return response.json()

def delete(keyword):
    response = requests.post(rf'http://{serverip}/delete?keyword={keyword}')
    return response.json()

def deleteall():
    response = requests.post(rf'http://{serverip}/deleteall')
    return response.json()

def search(keyword):
    response = requests.get(rf'http://{serverip}/search?keyword={keyword}')
    return response.json()

def get_keywords(prefix = ""):
    if(prefix == ""):
        response = requests.get(rf'http://{serverip}/keywords')
        return response.json()
    response = requests.get(rf'http://{serverip}/keywords?keyword={prefix}')
    return response.json()

def auth(name, passw):
    response = requests.get(rf'http://{serverip}/auth?name={name}&pass={passw}')
    response = response.json()
    if response['response'] == 'True':
        return True
    return False

def authname(name):
    response = requests.get(rf'http://{serverip}/authname?name={name}')
    response = response.json()
    if response['response'] == 'True':
        return True
    return False

def createtrie(name, passw):
    response = requests.post(rf'http://{serverip}/createtrie?name={name}&pass={passw}')
    return response.json()