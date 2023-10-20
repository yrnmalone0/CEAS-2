from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings

def send_mail(request):
    if request.method == 'POST':
        candidate_name = request.POST['name']
        candidate_email = request.POST['email']
        message = request.POST['message']

        # Send Mail
        email = EmailMessage(
            'Exciting News! Your Interview is Confirmed', #The Subject of Mail
            f"Dear {candidate_name}, \n{message}",
            settings.EMAIL_HOST_USER, #The Mail Sender
            [candidate_email] #The Receiver
        )

        email.fail_silently = True
        email.send()
        
    return render(request, 'mail/send_mail.html', {})