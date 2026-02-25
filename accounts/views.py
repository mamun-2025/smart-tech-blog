from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import ProfileUpdateForm, UserUpdateForm


def signup(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         messages.success(request, f'Account created for {username}! You can now login.')
         return redirect('login')
   else:
      form = UserCreationForm()
         
   return render(request, 'registration/signup.html', {'form': form})
   

# ২. প্রোফাইল ভিউ (প্রোফাইল আপডেট করার জন্য)
@login_required
def profile(request):
      if request.method == 'POST':
         # ইউজারনেম ও ইমেইল আপডেটের জন্য
         u_form = UserUpdateForm(request.POST, instance=request.user)
         # ছবি ও বায়ো আপডেটের জন্য (request.FILES অবশ্যই লাগবে)
         p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

         if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('accounts:profile')
         
      else:
         # বর্তমান ডাটা দিয়ে ফর্ম লোড করা
         u_form = UserUpdateForm(instance=request.user)
         p_form = ProfileUpdateForm(instance=request.user.profile) 


      context = {
         'u_form': u_form,
         'p_form': p_form
      }

      return render(request, 'registration/profile.html', context)  






