from django.db.models import Count

from .models import Robot

from openpyxl import Workbook
from datetime import datetime


def create_exlx():
    date = datetime.today()
    week = date.isocalendar()[1]

    list_models = [i['model'] for i in list(Robot.objects.values('model').filter(created__week=week).distinct())]
    sort_list_models = sorted(list_models)
    models = Robot.objects.values('model', 'version').filter(created__week=week).annotate(Count('version'))

    wb = Workbook()

    for i in sort_list_models:
        ws = wb.create_sheet(i)
        ws.append(('Модель', 'Версия', 'Количество за неделю'))
        ws_model = models.filter(model=i)
        for j in ws_model:
            ws.append((j['model'], j['version'], j['version__count']))

    ws = wb['Sheet']
    wb.remove(ws)
    report_name = f"report_{str(date).split(' ')[0]}.xlsx"
    wb.save(report_name)

    return report_name


