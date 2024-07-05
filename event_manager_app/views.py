from django.shortcuts import redirect, render, get_object_or_404, HttpResponse
from django.shortcuts import redirect, render
from event_manager_app.models import Event
from event_manager_app.forms.event_add_form import EventAdd
from event_manager_app.utils import getdata, setdata 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import *
from event_manager_app.forms.user_login_form import *
from event_manager_app.forms.search_form import * 
import pandas as pd 
from datetime import date


from django.core.paginator import Paginator

data = {}
# Create your views here.
@login_required
def all_events(request):
    events = Event.all()
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'display.html', {'events':page_obj, 'page_obj':page_obj})

@login_required
def UpdateEvents(request):
    id = request.GET.get('event_id')
    
    print(request.method)
    event = Event.get(id=id)
    print(event.title)
    event_dict = event.to_dict()
    form= EventAdd(initial=event_dict)
    if not event:
        return render(request, 'error.html', {'error':"Event not found"})
    
    if request.method == 'POST':
        print('form method', request.method)
        form = EventAdd(request.POST)
        if form.is_valid():
            event.title= form.cleaned_data['title']
            event.description = form.cleaned_data['description']
            event.total_participants = form.cleaned_data['total_participants']
            event.start_date = form.cleaned_data['start_date']
            event.end_date = form.cleaned_data['end_date']
            event.location = form.cleaned_data['location']
            event.contact_person = form.cleaned_data['contact_person']
            event.contact_number= form.cleaned_data['contact_number']
            event.save(event)
            print('inside form valid')
            msg = 'successfully edited'
            name = event.title
            return render(request, 'success_page.html', {'msg':msg, 'name':name})
        else:
             return render(request, 'update_event.html', {'error':"entered else", 'form':form})
        
    return render(request, 'update_event.html', {'form':form})

@login_required
def add_events(request):
    
    
    if request.method == 'POST':
        form = EventAdd(request.POST)
        if form.is_valid():
            global data 
            data = {
            'title':form.cleaned_data['title'],
            'description' :form.cleaned_data['description'],
            'total_participants' :form.cleaned_data['total_participants'],
            'start_date' :form.cleaned_data['start_date'],
            'end_date' :form.cleaned_data['end_date'],
            'location' :form.cleaned_data['location'],
            'contact_person' :form.cleaned_data['contact_person'],
            'contact_number' :form.cleaned_data['contact_number'],
            }
            previous_data = getdata()
            new_id = max([event.get('id', 0) for event in previous_data] + [0]) + 1
            data['id'] = new_id
            title = data['title']
            previous_data.append(data)
            setdata(previous_data)
            
            msg = "Successfully added"
            
            return render(request, 'success_page.html', {'msg':msg, 'title': title})
    else:
        form = EventAdd(request.POST)
       

        
    return render(request, 'add_event.html', {'form':form})


@login_required
def LogoutView(request):
    logout(request)
    return redirect('login')

def UserLogin(request):
    form = UserLoginForm(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)

    
        

    if request.method == 'POST':
        if user is not None: 
            login(request, user)
            msg = "Success"
            return render(request, 'login.html')

        else: 
            msg = "Error, invalid user"
            return render(request, 'login.html', {'msg':msg, 'form':form})
        
    msg = "Login"
    return render(request, 'login.html', {'msg':msg, 'form':form})
    

    
@login_required
def DeleteEvent(request):
    id =int(request.GET.get('event_id'))
    print("id for deletion is", id)
    data_new = []
    del_title = None
    data = getdata()
    for event in data: 
        if event.get('id') !=  id:
            data_new.append(event)
            
        if event.get('id') ==  id:
            del_title = event.get('title')
        

    setdata(data_new)
    return render(request, 'success_page.html', {"msg":"succesfully deleted", 'title':del_title})
@login_required    
def base(request):
    return render(request, 'index.html')


def filter_title(request):

    data = getdata() 
    start_dates = [(item['start_date'], item['start_date']) for item in data]
    msg = ''
    
    form = SearchForm(request.POST)
    if request.method == 'POST':
        

        if form.is_valid():
            title = form.cleaned_data['title']
            start_dates_received = form.cleaned_data['start_dates']
            start_dates_received = start_dates_received.strftime('%d-%m-%Y')
            end_dates_received = form.cleaned_data['end_date']
            print(start_dates_received)

            for item in data:
                print(title)
                if item['title'] == title: 
                    print("exists")
                    msg = item
                elif item['start_date']== start_dates_received:
                    msg = item
                elif item['end_date']== end_dates_received:
                    print(end_dates_received)
                    msg = (item)
    else:
        form = SearchForm( )
    return render(request, 'search.html', {'obj':msg, 'form':form} )


def json_to_csv(request):
   
    df = pd.read_json('event_manager_app/data_json/event.json')
    download = df.to_csv()
    response = HttpResponse(download, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = event_list.csv'
    return response