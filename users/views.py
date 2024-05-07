from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm, UserGenderForm, UserChoice
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')   
            messages.success(request, f'Пользователь {username} был успешно создан')
            return redirect('home')
    else:
        form = UserRegisterForm()
        return render(
            request, 
            'users/registration.html', 
            {
                'title': 'Регистрация',
                'form': form
            }
        )
    
    return render(
        request, 
        'users/registration.html', 
        {
            'title': 'Регистрация',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        genderForm = UserGenderForm(request.POST, instance=request.user.profile)
        choiceForm = UserChoice(request.POST, instance=request.user.profile)
        if profileForm.is_valid() and updateUserForm.is_valid() and genderForm.is_valid() and choiceForm.is_valid():
            profileForm.save()
            updateUserForm.save()
            genderForm.save()
            choiceForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')  
        
    profileForm = ProfileImageForm(instance=request.user.profile)
    updateUserForm = UserUpdateForm(instance=request.user)
    genderForm = UserGenderForm(instance=request.user.profile)
    choiceForm = UserChoice(instance=request.user.profile)
    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
        'genderForm': genderForm,
        'choiceForm': choiceForm
    }
    return render(request, 'users/profile.html', data)
