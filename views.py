from django.shortcuts import render
from .forms import RegisterForm

# Create your views here.
def registerview(request):
    form = RegisterForm()
    print(request)
    context = {
            'form':form
        }
    if request.method == "POST":
        
        
        return render(request, 'register.html', context=context)
    return render(request, 'register.html', context=context)
    
