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


USER_STORAGES_FOLDER_NAME = 'user_storages/'
STORAGES_CONTEXT_OBJECT_NAME = 'storages'

# Only 9 storages will show on a single page
STORAGES_AMOUNT_FOR_PAGINATION = 6


class StorageListView(LoginRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    '''Storage list view for index page'''

    template_name = USER_STORAGES_FOLDER_NAME + 'index.html'
    context_object_name = STORAGES_CONTEXT_OBJECT_NAME

    def get_queryset(self):
        current_user_id = self.request.user.id

        # Storages for current user
        return Storage.objects.filter(owner=current_user_id)

    paginate_by = STORAGES_AMOUNT_FOR_PAGINATION


class StorageBaseView:  # pylint: disable=too-few-public-methods
    '''Storage base view'''

    model = Storage

    # After storage creation we'll go to the index page
    success_url = reverse_lazy('user_storages:index')


class StorageCreateView(StorageBaseView, CreateView):  # pylint: disable=too-many-ancestors
    '''Storage create view'''

    def form_valid(self, form):
        # Storage owner will be current user
        form.instance.owner = self.request.user

        return super().form_valid(form)

    form_class = StorageCreateForm
    template_name = USER_STORAGES_FOLDER_NAME + 'create_storage.html'


class StorageUpdateView(StorageBaseView, UpdateView):  # pylint: disable=too-many-ancestors
    '''Storage update view'''

    form_class = StorageUpdateForm
    template_name = USER_STORAGES_FOLDER_NAME + 'update_storage.html'


class StorageDeleteView(StorageBaseView, DeleteView):  # pylint: disable=too-many-ancestors
    '''Storage delete view'''

    template_name = USER_STORAGES_FOLDER_NAME + 'delete_storage.html'


class SearchStorageView(ListView):  # pylint: disable=too-many-ancestors
    '''Storage search view'''

    template_name = USER_STORAGES_FOLDER_NAME + 'search_storage.html'
    context_object_name = STORAGES_CONTEXT_OBJECT_NAME
    model = Storage

    def get_queryset(self):
        user_query = self.request.GET.get('q')

        # Filter storages for current user by name from query
        return Storage.objects.filter(
            Q(name__icontains=user_query) & Q(owner=self.request.user.id)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # User query
        context['user_query'] = self.request.GET.get('q')

        return context


class StorageDetailView(DetailView):  # pylint: disable=too-many-ancestors
    '''Storage detail view'''

    model = Storage
    template_name = USER_STORAGES_FOLDER_NAME + 'detail_storage.html'
