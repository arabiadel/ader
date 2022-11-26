from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def HomePageView(request):
    return render(request, 'pages/home.html')

class Homepage(TemplateView):
    template_name = "pages/about.html"

