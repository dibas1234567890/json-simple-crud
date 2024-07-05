from django.urls import path
from event_manager_app.views import *
urlpatterns = [
    path('display_all/', all_events, name='display_all'),
    path('', base, name='base'),
    path('update_event/', UpdateEvents, name='update_event'),
    path('delete_event/', DeleteEvent, name='delete_event'),
    path('add_event/', add_events, name='add_event'),
    path('login/', UserLogin, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('search-title/', filter_title, name='filter_title'),
    path('download/', json_to_csv, name='json_to_csv'),



]
