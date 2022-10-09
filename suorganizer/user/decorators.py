from django.conf import settings
from django.contrib.auth import get_user
from django.shortcuts import redirect
from functools import wraps
from django.utils.decorators import available_attrs
from django.contrib.auth.decorators import login_required

def custom_login_required(view):
    # view argument must be a function
    decorated_view = login_required(view)
    return decorated_view