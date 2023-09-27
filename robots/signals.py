from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Robot
from orders.models import Order
from orders.message import email_message


@receiver(post_save, sender=Robot)
def post_save_robot(sender, instance, created, **kwargs):
    robot = instance
    if created:
        order_completed = Order.objects.filter(robot_serial=robot.serial).filter(completed=False).first()
        if order_completed:
            email = order_completed.customer.email
            email_message(robot.model, robot.version, email)
            order_completed.completed = True
            order_completed.save()


