from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from dj_celery import settings

@shared_task(bind=True)
def send_the_mails(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = 'Hello! I am from Celery'
        message = 'Please! do not shock. It is just due to testing of Celery app.'
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=False
        )
    return "All Mails SENT!"
