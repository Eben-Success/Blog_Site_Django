from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
       else:
       form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


#message.debug
#message.success
#message.info
#message.warning
#message.error