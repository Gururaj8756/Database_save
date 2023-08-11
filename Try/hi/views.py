from django.shortcuts import render

from .models import User  

def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = int(request.POST['age'])

        new_user = User(name=name, email=email, age=age)
        new_user.save()

        return render(request, 'success.html')

    return render(request, 'user_form.html')
