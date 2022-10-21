from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
    # Get data from the form
        form = UserCreationForm(request.POST)
        #validate the form
        if form.is_valid():
            form.save()
        # get username
            username = form.cleaned_data.get('username')
            # print a success message
            messages.success(request, f'Account created for {username}!')
            #redirect user to blog-home
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# MESSAGES
#messages.debug
#messages.success
#messages.info
#messages.warning
#messages.error
