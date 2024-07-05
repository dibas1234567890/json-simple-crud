from django.db import models
from event_manager_app.utils import getdata, setdata

# Create your models here.
class Event: 
    file = 'event.json'

    def __init__(self, id, title, description, total_participants, start_date, 
                 end_date, location, contact_person, contact_number):
        self.id = id 
        self.title = title 
        self.description = description 
        self.total_participants = total_participants
        self.start_date = start_date 
        self.end_date = end_date
        self.location = location 
        self.contact_person = contact_person
        self.contact_number = contact_number

    @classmethod
    def all(cls):
        data = getdata()
        return data 
    
    @classmethod 
    def get(cls, id):
        print('id is', repr(id))
        data = getdata()
        id = int(id)
        for item in data: 
            print('inside for loop')
    
            print('id of item', repr(item['id']))
            if item['id'] == id:
              
                try: 
                    return cls(**item)
                    
                except:
                    print('to debug:- error, class returned as empty')    

    @classmethod
    def save(self, event):
        data = getdata()
        
        for item in data: 
            print('debug gardai id chai', event.id )
            if item['id']==event.id:
                 item['title'] = event.title 
                 item['description'] = event.description 
                 item['total_participants'] = event.total_participants 
                 item['start_date'] = event.start_date 
                 item['end_date'] = event.end_date 
                 item['location'] = event.location 
                 item['contact_person'] = event.contact_person 
                 item['contact_number'] = event.contact_number
                 print('working')
                 break 
        if item['id']!= event.id: 
                data.append({
                    'id': self.id, 
                    'title': self.title, 
                    'description': self.description, 
                    'total_participants': self.total_participants, 
                    'start_date': self.start_date, 
                    'end_date': self.end_date, 
                    'location': self.location, 
                    'contact_person': self.contact_person, 
                    'contact_number': self.contact_number, 
                    
                })

        setdata(data)
                
    def to_dict(self):
        return {
                    'id': self.id, 
                    'title': self.title, 
                    'description': self.description, 
                    'total_participants': self.total_participants, 
                    'start_date': self.start_date, 
                    'end_date': self.end_date, 
                    'location': self.location, 
                    'contact_person': self.contact_person, 
                    'contact_number': self.contact_number, 
                    
                }
  
