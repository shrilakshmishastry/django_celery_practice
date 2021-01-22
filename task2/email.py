from django.template import Context
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import EmailMessage


def send_review_email(name, email, review):
    context = {
        'name': name,
        'email': email,
        'review': review,
    }
    email_subject = 'Thank you for your review'
    email_body = render_to_string('email_message.txt', context)
    email = EmailMessage(
        email_subject,
        email_body,
        to=['shrilakshmishastry@gmail.com']
    )
    return email.send(fail_silently=False)
