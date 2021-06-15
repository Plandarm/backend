from django.shortcuts import render
from pages.models import Page 
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def page(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {'page': page}
 
    if page.owner.user.id != request.user.id:
        return HttpResponse('You are not authorized to view this page')

    return render(request, 'pages/editor.html', context)
