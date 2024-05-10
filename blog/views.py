from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Message
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    data = {
        'title': 'Главная страница!'
    }
    return render(request, 'blog/home.html', data)

def service(request):
    return render(request, 'blog/service.html', {'title': 'Услуги'})

def contacti(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message']
            message = Message(subject=subject, email=email, message=message_text)
            message.save()
            
            # subject = "Тема сообщения"
            # plain_message = "Текст сообщения"
            # from_email = email
            # to_email = "vittello2@gmail.com"
            # send_mail(subject, plain_message, from_email, [to_email])
            messages.success(request, f'Сообщение было успешно отправлено')
            return redirect('contacti')

    else:
        form = ContactForm()
    return render(request, 'blog/contacti.html', {'title': 'Контакты', 'form': form})
