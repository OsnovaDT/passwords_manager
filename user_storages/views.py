'''Views for user_storages app'''

from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# For search query
from django.db.models import Q
from django.urls import reverse_lazy

from user_storages.models import Storage
from user_storages.forms import StorageCreateForm, StorageUpdateForm


class StorageListView(LoginRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Storage list view for index page'''

    template_name = 'user_storages/index.html'
    context_object_name = 'storages'

    def get_queryset(self):
        current_user_id = self.request.user.id

        # Storages for current user
        return Storage.objects.filter(owner=current_user_id)

    # Only 9 storages will show on a single page
    paginate_by = 9


class StorageCreateView(CreateView):  # pylint: disable=too-many-ancestors
    '''Storage create view'''

    def form_valid(self, form):
        # Storage owner will be current user
        form.instance.owner = self.request.user

        return super().form_valid(form)

    form_class = StorageCreateForm
    template_name = "user_storages/create_storage.html"

    # After storage creation we'll go to the index page
    success_url = reverse_lazy('user_storages:index')


class StorageUpdateView(UpdateView):  # pylint: disable=too-many-ancestors
    '''Storage update view'''

    model = Storage
    form_class = StorageUpdateForm
    template_name = "user_storages/update_storage.html"

    # After storage updating we'll go to the index page
    success_url = reverse_lazy('user_storages:index')


class StorageDeleteView(DeleteView):  # pylint: disable=too-many-ancestors
    '''Storage delete view'''

    model = Storage
    template_name = "user_storages/delete_storage.html"

    # After storage deleting we'll go to the index page
    success_url = reverse_lazy('user_storages:index')


class SearchStorageView(ListView):  # pylint: disable=too-many-ancestors
    '''Storage search view'''

    template_name = 'user_storages/search_storage.html'
    context_object_name = 'storages'
    model = Storage

    def get_queryset(self):
        query = self.request.GET.get('q')

        # Filter storages for current user by name from query
        return Storage.objects.filter(
            Q(name__icontains=query) & Q(owner=self.request.user.id)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # User query
        context['query'] = self.request.GET.get('q')

        return context


class StorageDetailView(DetailView):  # pylint: disable=too-many-ancestors
    '''Storage detail view'''

    model = Storage
    template_name = 'user_storages/detail_storage.html'
