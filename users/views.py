from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success

       else:
       form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# MESSAGES
#messages.debug
#messages.success
#messages.info
#messages.warning
#messages.error