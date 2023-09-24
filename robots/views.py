from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt

from .models import Robot

import json
from datetime import datetime


@method_decorator(csrf_exempt, name='dispatch')
class RobotsView(View):

    def post(self, request):
        model = request.POST.get("model")
        version = request.POST.get("version")
        created = datetime.strptime(request.POST.get("created"), "%Y-%m-%d %H:%M:%S")

        robot_data = {
            'serial': f'{model}-{version}',
            'model': model,
            'version': version,
            'created': created,
        }

        robot = Robot.objects.create(**robot_data)
        # запрос есть ли такой робот в списке ожидания и если да, передаются данные в заказы

        data = {
            'message': f'New robot {robot.model}-{robot.version} created'
        }
        return JsonResponse(data)

class AccountView(View):
    def get(self, request):
        #year, week, _ = now().isocalendar()
        accountLastWeek = Robot.objects.all()  #filter(time__year=year, time__week=week).values_list('model', 'version', 'created')

        return JsonResponse(accountLastWeek)
