from django.views import View
from django.http import FileResponse

from .xlsx import create_exlx


class ReportView(View):
    def get(self, request):
        exlx_name = create_exlx()
        response = FileResponse(open(exlx_name, 'rb'))
        return response
