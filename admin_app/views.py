from django.shortcuts import render,redirect
from .forms import ProfileForm
from .models import Profile
# Create your views here.
def create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=ProfileForm()

    return render(request,'admin/create.html',{'form':form})

def list_detail(request):
    profiles = Profile.objects.all()
    
    return render(request,'admin/view.html',{'profiles':profiles})