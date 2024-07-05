import json, os 
from django.conf import settings 

def setdata(data):
    path = 'event_manager_app/data_json/event.json'
    with open(path, 'w') as file:
        data = json.dump(data, file, indent=4, sort_keys=True, default=str)
    return data

def getdata():
    path = 'event_manager_app/data_json/event.json'
    
    try:
        print('file not empty ')
        with open(path, 'r') as file:
            data = json.load(file)
           
        return data
    except:
        print('file empty ')
        return []
