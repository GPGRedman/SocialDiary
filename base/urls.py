from django.urls import path
from .views import EventList, EventDetail, EventCreate, EventUpdate, EventDelete, CustomLoginView,RegisterPage, TotalEventList
from django.contrib.auth.views import LogoutView


# these are the url patterns obeyed by the application
# the entry point is the eventlist classview which shows the diary of each resident
# total event is not wired up yet and was intended to be the view seen by the HA

urlpatterns =[
    path('login/',CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('', EventList.as_view(), name='events'),
    path('totalevent/', TotalEventList.as_view(), name='total-events' ),
    path('event/<int:pk>/', EventDetail.as_view(), name= 'event'),
    path('create-event/', EventCreate.as_view(), name='event-create'),
    path('event-update/<int:pk>/', EventUpdate.as_view(), name='event-update'),
    path('event-delete/<int:pk>/', EventDelete.as_view(), name='event-delete'),
]