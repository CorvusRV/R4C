from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.core.serializers import serialize  # возможно временный

from .models import Order
from customers.models import Customer


@method_decorator(csrf_exempt, name='dispatch')
class OrderView(View):
    def post(self, request):
        email = request.POST.get("email")
        robot_serial = request.POST.get("robot_serial")

        customer, created = Customer.objects.get_or_create(email=email)

        order_data = {
                 'customer': customer,
                 'robot_serial': robot_serial,
        }

        Order.objects.create(**order_data)

        date = {'message': f'Заказ оформлен'}

        return JsonResponse(date)
