from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import FileResponse

from .models import Robot
from .xlsx import create_exlx

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
            'message': f'Робот {robot.model}-{robot.version} создан'
        }
        return JsonResponse(data)

class ReportView(View):
    def get(self, request):
        exlx_name = create_exlx()
        response = FileResponse(open(exlx_name, 'rb'))
        response['Content-Disposition'] = 'attachment; filename=' + exlx_name
        response['X-Sendfile'] = exlx_name
        return response
