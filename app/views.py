from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm  


# Create your views here.
def list_users(request):
    user = User.objects.all()
    return render(request, 'users/list.html', {'user': user})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_users')
        else:
            form = UserForm()
        return render(request, 'users/form.html', {'form': form})
    
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
        else:
            form = UserForm(instance=user)
        return render(request, 'users/form.html', {'form': form})
    
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('list_users')
    return render(request, 'users/confirm_delete.html', {'user': user})