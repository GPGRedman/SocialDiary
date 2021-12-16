from django.shortcuts import render, redirect
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


# A design choice was made to use class based views.
# Not only are they way cooler but allow us to take advantage of superior security
# offered by  Django. Notably by the "mixins" . These use polymorphism to ensure
# that folk are correctly logged in.

# login CBV
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('events')
# user registration CBV
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('events')
# over rides
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('events')
        return super(RegisterPage, self).get(*args, **kwargs)

# this is the main entry point
class EventList(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'
# this over rides and ensures that each resident is only seeing  their own entries
#
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.user)
        print(context['events'])
        context['events'] = context['events'].filter(user=self.request.user)
        print(context['events'])
        context['count'] = context['events'].filter(finished = False).count()
        return context

# this is the class based view for the HA rep which is not wired up
class TotalEventList(LoginRequiredMixin, ListView):
    model = Event
    context_object_name = 'events'


# event detail!
class EventDetail(LoginRequiredMixin,DetailView):
    model=Event
    context_object_name="event"
    template_name= 'base/event.html'
# event creation!
class EventCreate(LoginRequiredMixin,CreateView):
    model= Event
    fields = ['title','description','finished']
    success_url = reverse_lazy('events')
# over ride to ensure a user is attached to each event
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate,self).form_valid(form)
# event update
class EventUpdate(LoginRequiredMixin,UpdateView):
    model = Event
    fields = ['title','description','finished']
    success_url = reverse_lazy('events')
# event delete
class EventDelete(LoginRequiredMixin,DeleteView):
    model = Event
    context_object_name = 'event'
    success_url = reverse_lazy('events')