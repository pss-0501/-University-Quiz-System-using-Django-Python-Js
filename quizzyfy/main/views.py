from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


from .forms import RegistrationForm, UserProfileForm

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            if user.is_superuser or user.is_staff:
                return redirect('/admin')
            
            if user.groups.filter(name='Professor').exists():
                return redirect('prof:index')
            
            return redirect('student:index')
            

        return render(request, 'main/login.html', { 'wrong_cred_message': 'Error' })

    return render(request, 'main/login.html')


def logoutUser(request):
    logout(request)
    return render(request, 'main/logout.html',{ 'logout_message': 'Logged out Successfully' })

# def registration_page(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Log the user in after registration
#             login(request, user)
#             return redirect('home')  # Replace 'home' with the URL name of your home page
#     else:
#         form = UserCreationForm()

#     return render(request, 'main/registration_page.html', {'form': form})

def registration_page(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Log the user in after registration
            login(request, user)
            if profile.is_student:
                student_group = Group.objects.get(name='Student')  # Replace with your actual group name
                user.groups.add(student_group)
                return redirect('student:index')
            else:
                prof_group = Group.objects.get(name='Professor')  # Replace with your actual group name
                user.groups.add(prof_group)
                return redirect('prof:index')
    else:
        user_form = RegistrationForm()
        profile_form = UserProfileForm()

    return render(request, 'main/registration_page.html', {'user_form': user_form, 'profile_form': profile_form})