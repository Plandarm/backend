from django.shortcuts import render
from pages.models import Page 

# Create your views here.

def page(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {'page': page}
    
    return render(request, 'pages/editor.html', context)
