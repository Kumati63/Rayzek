# decorators.py
from django.shortcuts import redirect

def login_required_custom(view_func):
    def wrapper(request, *args, **kwargs):
        if 'usuario_id' not in request.session:
            return redirect('Login')
        return view_func(request, *args, **kwargs)
    return wrapper

