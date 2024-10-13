from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Welcome view function
def welcome(request):
    return render(request, 'users/welcome.html')  # Ensure 'welcome.html' exists in your templates


from django.http import JsonResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'success': True})  # Return success
        else:
            return JsonResponse({'success': False})  # Return failure
    return render(request, 'users/login.html')



from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account successfully created!')  # Flash message
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()

    # Remove email field from the form
    form.fields.pop('email', None)  # Remove the email field if it exists

    return render(request, 'users/signup.html', {'form': form})



# Forgot password view function
def forgot_password(request):
    return render(request, 'users/forgot_password.html')  # Ensure 'forgot_password.html' exists