from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterFrom, UserUpdateForm, ProfileUpdateForm

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

@login_required
def profile(request):
    if request.method == 'POST':

        # current login user
        u_form = UserUpdateForm(request.POST, instance=request.user)
        #current profile
        p_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)



# MESSAGES
#messages.debug
#messages.success
#messages.info
#messages.warning
#messages.error
