from django.shortcuts import render, redirect
from .models import Page
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url='login')
def page(request, page_id):
    page = Page.objects.get(id=page_id)

    if page.owner.user.id != request.user.id and request.user.profile not in page.viewers.all():
        return redirect('error', page_id, "ownership")
    
    user_pages = request.user.profile.page_set.all()
    other_pages = request.user.profile.viewable_pages.all()

    if page.owner.user.id != request.user.id:
        view_only = True
    else:
        view_only = False
    
    context = {'page': page, 'user_pages': user_pages, 'other_pages': other_pages, 'view_only': view_only}
    
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
        return redirect('error', page_id, "deletion")
    
    if len(page.owner.page_set.all()) > 1:
        page.delete()
        first_page = request.user.profile.page_set.first().id
        return redirect('page', first_page)
    else:
        page.delete()
        return redirect('create_page')


@login_required(login_url='login')
def pagePermissions(request, page_id):
    
    page = Page.objects.get(id=page_id)

    if page.owner.user.id != request.user.id:
        return redirect('error', page_id, "access")

    if request.method == 'POST':
        username = request.POST.get('username')

        if username == request.user.username:
            messages.error(request, 'This role cannot be assigned to Owner')
            return redirect('page_permissions', page_id)

        try:
            new_viewer = User.objects.get(username=username)  
        except ObjectDoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('page_permissions', page_id)

        page.viewers.add(new_viewer.profile)
        return redirect('page_permissions', page_id)
             
    viewers = page.viewers.all()

    context = {'viewers': viewers, 'page_id': page_id}
    return render (request, 'pages/permissions.html', context)


@login_required(login_url='login')
def permissionRemove(request, page_id, username):
    page = Page.objects.get(id=page_id)

    if page.owner.user.id != request.user.id:
        return HttpResponse('You are not allowed to edit permissions of this page', status=403)

    page.viewers.remove(User.objects.get(username=username).profile)
    return redirect('page_permissions', page_id)

@login_required(login_url='login')
def denyAccess(request, page_id, err):
    page = Page.objects.get(id=page_id)
    context = {'page_title': page.title, 'current_user': request.user.username, 'err': err}

    return render(request, 'pages/error.html', context)


@login_required(login_url='login')
def honestWork(request):
    return render(request, 'pages/honest-work.html')
