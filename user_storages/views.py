from django.views.generic.list import ListView

from .models import Storage


class StorageListView(ListView):
    template_name = 'user_storages/index.html'
    context_object_name = 'storages'

    def get_queryset(self):
        current_user_id = self.request.user.id

        return Storage.objects.filter(owner=current_user_id)
    paginate_by = 9
