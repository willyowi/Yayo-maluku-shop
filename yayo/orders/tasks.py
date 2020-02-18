from celery import task, shared_task
from django.core.mail import send_mail
from .models import Order
from time import sleep
from django.utils import timezone
from celery.utils.log import get_task_logger

# logger = get_task_logger(name)



@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    sleep(5)
    send_mail('Testing Celery Email',
    'Pay your Bills',
    'brians931@gmail.com',
    ['sundaypriest@outlook.com'])

    return None

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\Your order id is {}.'.format(order.first_name,order.id)
    mail_sent = send_mail(subject,message,'admin@yayo-malooku.com',[order.email])
    return mail_sent