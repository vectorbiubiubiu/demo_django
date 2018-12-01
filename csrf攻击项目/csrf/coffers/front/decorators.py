from .models import User
from django.shortcuts import redirect,reverse

def login_required(func):
    def wrapper(request,*args,**kwargs):
        # user_id = request.session.get('user_id')
        # exists = User.objects.filter(pk=user_id).exists()
        # if exists:
        if request.front_user:
            return func(request,*args,**kwargs)
        else:
            return redirect(reverse('login'))

    return wrapper