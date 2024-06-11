# Video 6 'Render a Django HTML Template to a PDF file Django Utility CFE Render to PDF'

from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .renderers import render_to_pdf

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdf/invoice.html')
        invoice_number = "007cae"
        context = {
            "bill_to": "Ethan Hunt",
            "invoice_number": f"{invoice_number}",
            "amount": locale.currency(100_000, grouping=True),
            "date": "2021-07-04",
            "pdf_title": f"Invoice #{invoice_number}",
        }
        html = template.render(context)
        return HttpResponse(html)