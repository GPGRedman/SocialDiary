from django.urls import path
from .views import EventList, EventDetail, EventCreate, EventUpdate, EventDelete, CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns =[
    path('login/',CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('', EventList.as_view(), name='events'),
    path('event/<int:pk>/', EventDetail.as_view(), name= 'event'),
    path('create-event/', EventCreate.as_view(), name='event-create'),
    path('event-update/<int:pk>/', EventUpdate.as_view(), name='event-update'),
    path('event-delete/<int:pk>/', EventDelete.as_view(), name='event-delete'),
]