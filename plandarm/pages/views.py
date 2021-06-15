from django.shortcuts import render, redirect
from pages.models import Page
from django.http import HttpResponse
import json


def page(request, page_id):
    page = Page.objects.get(id=page_id)
    context = {'page': page}
    
    return render(request, 'pages/editor.html', context)


def createPage(request):
    current_user = request.user
    page = Page.objects.create()
    page.owner = current_user.profile
    page.save()
    return redirect(f'/page/{page.id}/')


def savePage(request, page_id):
    if request.method == 'POST':
        dict_request = json.loads(request.body)
        page = Page.objects.get(id=page_id)
        page.title = dict_request['title']
        page.html = dict_request['body']
        page.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


def deletePage(request, page_id):
    page = Page.objects.get(id=page_id)
    page.delete()
    return HttpResponse("Page was deleted", status=200)
