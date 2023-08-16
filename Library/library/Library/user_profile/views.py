from django.shortcuts import render, redirect
from .forms import  ImageForm


def user_profile(request):
    if not request.user.is_authenticated:
        raise Exception('AUTH PLEASE')

    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            return render(request, 'profile.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'profile.html', {'form': form})