from django.http import HttpResponse
from django.shortcuts import redirect
from accounts.models import Profile


def logged_out(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            page_id = str(profile.page_set.first().id)
            
            return redirect('/page/'+page_id)
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func
    