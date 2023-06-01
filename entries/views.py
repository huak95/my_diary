from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# Restrict access to your views
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Entry

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')

class EntryDetailView(DetailView):
    model = Entry

class EntryCreateView(SuccessMessageMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    success_url = reverse_lazy('entry-list')
    success_message = "Your new entry was created!"

class EntryUpdateView(SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ['title', 'content']
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy(
            'entry-detail',
            kwargs={'pk': self.object.pk}
        )
    
class EntryDeleteView(DeleteView):
    model = Entry
    success_url = reverse_lazy('entry-list')
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    
# LockedView
class LockedView(LoginRequiredMixin):
    login_url = "admin:login"

class EntryLockedListView(LockedView, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by('-date_created')
