# Video 6 'Render a Django HTML Template to a PDF file Django Utility CFE Render to PDF'

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .renderers import render_to_pdf
import locale
locale.setlocale(locale.LC_ALL, "")

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        invoice_number = "007cae"
        context = {
            "customer_name": "Ethan Hunt",
            "invoice_number": f"{invoice_number}",
            "amount": locale.currency(100_000, grouping=True),
            "date": "2021-07-04",
            "pdf_title": f"Invoice #{invoice_number}",
        }
        html = template.render(context)
        pdf = render_to_pdf('pdf/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse('Not Found')