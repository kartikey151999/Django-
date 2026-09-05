from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UploadForm
from .models import Profile
# Create your views here.


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File uploaded successfully!')
            return redirect('view')
        else:
            messages.error(request, 'Error uploading file. Please try again.')  
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})   


def view(request):
    profiles = Profile.objects.all()
    return render(request, 'view.html', {'profiles': profiles})