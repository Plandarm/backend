from django.shortcuts import render, redirect
from pages.models import Page
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json


@login_required(login_url='login')
def page(request, page_id):
    page = Page.objects.get(id=page_id)
 
    if page.owner.user.id != request.user.id:
        return HttpResponse('You are not allowed to view this page', status=403)

    user_pages = page.owner.page_set.all()
    context = {'page': page, 'user_pages': user_pages}

    return render(request, 'pages/editor.html', context)


@login_required(login_url='login')
def createPage(request):
    current_user = request.user
    page = Page.objects.create()
    page.owner = current_user.profile
    page.save()
    return redirect(f'/page/{page.id}/')


@login_required(login_url='login')
def savePage(request, page_id):
    if request.method == 'POST':
        dict_request = json.loads(request.body)
        page = Page.objects.get(id=page_id)

        if page.owner.user.id != request.user.id:
            return HttpResponse(status=403)

        page.title = dict_request['title']
        page.html = dict_request['body']
        page.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)


@login_required(login_url='login')
def deletePage(request, page_id):
    page = Page.objects.get(id=page_id)

    if page.owner.user.id != request.user.id:
        return HttpResponse('You are not allowed to delete this page', status=403)
    
    if len(page.owner.page_set.all()) > 1:
        page.delete()
        first_page = page.owner.page_set.first().id
        return redirect('/page/' + str(first_page))
    else:
        page.delete()
        return redirect('create_page')