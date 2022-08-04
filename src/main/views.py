from django.shortcuts import render
from .models import Modal
# Create your views here.

def index_view(request):

    modals = Modal.objects.all()

    context = {
        'updates' : modals
    }
    return render(request,'index.html',context)