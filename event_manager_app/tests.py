from django.test import TestCase, Client
from django.urls import reverse
from event_manager_app.models import Event
from django.contrib.auth.models import User
class BasicTests(TestCase):

    def setUP(self):
       
        self.user = User.objects.create(username = "TESTER", password = "TESTER")

    #testing if event is instantiated or not because we are not using models and using JSON
    def test_1(self):
        
        event_instance = Event(id = 45, 
        title = 'title',
        description = 'Test Description',
        total_participants = 2,
        start_date = "11-06-2024" ,
        end_date = "15-06-2024",
        location = "Test Locaiton" ,
        contact_person = "Test Person",
        contact_number = 123456789)


        self.assertTrue(isinstance(event_instance, Event))

#login_required testing 
class LoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("tester")
        self.client = Client(self.user)
        self.url = reverse('base')
    def test_login(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200) #originally, here the AssertionError: 302 != 200 would occur

#testing index (base) page by setting up client 
class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("tester")
        self.client = Client(self.user)
        self.index_url = reverse('base')

    def test_index_GET(self):
        logged_client = self.client.force_login(user=self.user)
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html' )
        print(response)

#form testing by disabling CSRF Token, have to disable the token check for a simple test.     
class FormTester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="tester")
        self.client_login_test = Client(enforce_csrf_checks=False)
        self.url = reverse('add_event')
        
    def test_index_GET(self):
        response = self.client.get(self.url)
        logged_client = self.client.force_login(user=self.user)
        response = self.client.post(self.url, {'id': 45, 'title' : 'title 2',
        'description' : 'Test Description 2',
        'total_participants' : 2,
        'start_date' : "11-06-2024" ,
        'end_date' : "15-06-2024",
        'location' : "Test Locaiton" ,
        'contact_person' : "Test Person",
        'contact_number': 123456789, 

        })
        
        self.assertEqual(response.status_code, 200)
        print(response)


         



