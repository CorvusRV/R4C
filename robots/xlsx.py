from django.db.models import Count

from .models import Robot

from openpyxl import Workbook
from datetime import datetime


def create_exlx():
    week = datetime.today().isocalendar()[1]
    #models = list(Robot.objects.values('model').filter(created__week=week).distinct())  # получение 'списка' всех моделей
    models = list(Robot.objects.values('model').distinct())
    list_models = [i['model'] for i in models]  # получение списка моделей
    models2 = Robot.objects.values('model', 'version').annotate(Count('version'))  # получение кол-ва модель-версия
    wb = Workbook()
    for i in list_models:
        ws = wb.create_sheet(i)
        ws.append(('Модель', 'Версия', 'Количество за неделю'))
        ws_model = models2.filter(model=i)
        for j in ws_model:
            ws.append((j['model'], j['version'], j['version__count']))

    ws = wb['Sheet']  # удаление базового листа
    wb.remove(ws)

    wb.save('test.xlsx')

    return 'test.xlsx'


