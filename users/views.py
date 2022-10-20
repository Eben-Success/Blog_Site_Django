from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
    # Get data from the form
        form = UserCreationForm(request.POST)
        #validate the form
        if form.is_valid():
        # get username
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username!}')
        else:
            form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# MESSAGES
#messages.debug
#messages.success
#messages.info
#messages.warning
#messages.error