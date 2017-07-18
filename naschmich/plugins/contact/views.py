import re
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from ...settings import get_email_user


def contact_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        own_mail = get_email_user()
        if check_input_email(email):
            message = request.POST.get('message')
            send_mail(
                subject='Kontakt via Hompage',
                message=message,
                from_email=email,
                recipient_list=[own_mail]
            )
            return redirect('/')
        else:
            context = {
                'error_msg': _('Bitte überprüfen Sie ihre Email-Adresse')
            }
            return render(request, 'contact_plugin.html', context)
    else:
        return render(request, 'contact_plugin.html', context={'': ''})


def check_input_email(email):
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return True
    else:
        return False
