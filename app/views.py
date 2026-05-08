from django.shortcuts import render
from .models import User
from . import USerForm


# Create your views here.
def list_users(request):
    user = User.objects.all()
    return render(request, 'list_users.html', {'users': user})