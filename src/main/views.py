from django.views.generic import DetailView,ListView
from .models import Modal


class IndexView(ListView):
    template_name = 'index.html'
    model = Modal
