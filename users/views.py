from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom

def register(request):
    if request.method == 'POST':
    # Get data from the form
        form = UserRegisterFrom(request.POST)
        #validate the form
        if form.is_valid():
            form.save()
        # get username
            username = form.cleaned_data.get('username')
            # print a success message
            messages.success(request, 'Account has been created! You can now log in')
            #redirect user to blog-home
            return redirect('login')
    else:
        form = UserRegisterFrom()
    return render(request, 'users/register.html', {'form': form})



# MESSAGES
#messages.debug
#messages.success
#messages.info
#messages.warning
#messages.error
