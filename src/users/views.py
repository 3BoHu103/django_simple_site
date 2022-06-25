from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserProfileForm


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'account/profile.html', context)


@login_required
def profile_change(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile was updated')
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'account/profile_change.html', context)
