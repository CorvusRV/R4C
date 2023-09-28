from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import Order
from customers.models import Customer
from robots.models import Robot


@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    def post(self, request):
        email = request.POST.get("email")
        robot_serial = request.POST.get("robot_serial")
        customer, created = Customer.objects.get_or_create(email=email)  # добавление/поиск заказчика в БД
        robot = Robot.objects.filter(serial=robot_serial).filter(available=True).first()
        if robot is None:
            completed = False
            date = {'message': f'Приносим извинения за неудобства, '
                               f'но робота {robot_serial} нет в наличие, '
                               f'мы свяжемся с вами как только он появится.'}
        else:
            robot.available = False
            robot.save()
            completed = True
            date = {'message': f'Заказ на робота {robot_serial} принят.'}
        order_data = {
            'customer': customer,
            'robot_serial': robot_serial,
            'completed': completed,
        }
        Order.objects.create(**order_data)
        return JsonResponse(date)
