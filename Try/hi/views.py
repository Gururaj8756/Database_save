from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import User  
from django.shortcuts import render, redirect


def create_user(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password=request.POST['password']
        email = request.POST['email']
        dob=request.POST['dob']
        age = int(request.POST['age'])
        

        new_user = User(name=name,username=username,password=password ,email=email,dob=dob,age=age)
        new_user.save()

        return render(request, 'success.html')

    return render(request, 'user_form.html')


# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect

# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Check if the redirection path is accurate
#             return redirect('index.html')  # Make sure the path is correct
#         else:
#             error_message = "Invalid username or password"
#             return render(request, 'login.html', {'error_message': error_message})
#     return render(request, 'login.html')

