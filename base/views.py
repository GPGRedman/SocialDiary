from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import   LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Event
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('events')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('events')

class EventList(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = context['events'].filter(user=self.request.user)
        context['place'] = 'North East'
        context['count'] = context['events'].filter(finished = False).count()
        return context

class EventDetail(LoginRequiredMixin,DetailView):
    model=Event
    context_object_name="event"
    template_name= 'base/event.html'

class EventCreate(LoginRequiredMixin,CreateView):
    model= Event
    fields = '__all__'
    #fields = ['title','description','finished']
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate,self).form_valid(form)

class EventUpdate(LoginRequiredMixin,UpdateView):
    model = Event
    fields = ['title','description','finished']
    success_url = reverse_lazy('events')

class EventDelete(LoginRequiredMixin,DeleteView):
    model = Event
    context_object_name = 'event'
    success_url = reverse_lazy('events')