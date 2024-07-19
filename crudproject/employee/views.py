from django.shortcuts import render
from . models import Employee

# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        # create an object
        new_person = Employee(first_name=first_name, last_name=last_name, email=email)
        new_person.save()

    return render(request, 'index.html')