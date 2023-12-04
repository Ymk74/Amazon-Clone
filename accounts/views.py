from django.shortcuts import render , redirect
from .forms import SignupForm , ActivationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail




def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.changed_data['password']
            form.save()
            
            profile = Profile.objects.get(user__username=username)
            
            send_mail(
                "Activate Your Account",
                f"Welcome {username} \nuse this code {profile.code} to activate your account",
                "adhamgeka1@gmail.com",
                [email],
                fail_silently=False,
                )
                
            return redirect('/accounts/{username}/activate')
            
    else :
        form = SignupForm()

    return render(request, 'registration/register.html',{'form':form})



def activate(request,username):
    pass



def profile(request):
    pass
