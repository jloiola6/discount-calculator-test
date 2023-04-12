from django.template.response import TemplateResponse
from back.apps.core.calculator import calculator

# Create your views here.


def index(request):
    template_name = 'index.html'
    
    if request.method == 'POST':
        consumption = [float(request.POST.get('inputvalor1')), float(request.POST.get('inputvalor2')), float(request.POST.get('inputvalor3'))]
        distributor_tax = float(request.POST.get('taxa'))
        tax_type = request.POST.get('tipo')
        
        result = calculator(consumption, distributor_tax, tax_type)
        
        return TemplateResponse(request, template_name, locals())
    
    return TemplateResponse(request, template_name, locals())