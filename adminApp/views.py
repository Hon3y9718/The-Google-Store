from django.shortcuts import render

# Create your views here.
def adminLogin(request):
    vars = {
        'Name': request.user
    }
    return render(request, 'adminAppTemplate/base.html', vars)

def home(request):
    return render(request, "adminAppTemplate/home.html")