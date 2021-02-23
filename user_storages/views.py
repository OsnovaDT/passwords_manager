from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django import forms

from .models import Storage
from .forms import StorageCreateForm


class StorageListView(LoginRequiredMixin, ListView):
    template_name = 'user_storages/index.html'
    context_object_name = 'storages'

    def get_queryset(self):
        current_user_id = self.request.user.id

        return Storage.objects.filter(owner=current_user_id)
    paginate_by = 9


class StorageCreateView(CreateView):
    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super().form_valid(form)

    form_class = StorageCreateForm
    template_name = "user_storages/create_storage.html"
    success_url = reverse_lazy('user_storages:index')
