from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Storage
from .forms import StorageCreateForm, StorageUpdateForm


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


class StorageUpdateView(UpdateView):
    model = Storage
    form_class = StorageUpdateForm
    success_url = reverse_lazy('user_storages:index')
    template_name = "user_storages/update_storage.html"
