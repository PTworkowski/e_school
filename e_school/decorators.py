from django.http import HttpResponseForbidden


def student_required(func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_student:
            return HttpResponseForbidden()
        return func(request, *args, *kwargs)

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap


def teacher_required(func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_teacher:
            return HttpResponseForbidden()
        return func(request, *args, *kwargs)

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap


def admin_required(func):
    def wrap(request, *args, **kwargs):
        if not request.user.is_admin:
            return HttpResponseForbidden()
        return func(request, *args, *kwargs)

    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap

def admin_or_teacher_required(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_admin and request.user.is_teacher:
            return func(request, *args, *kwargs)
        return HttpResponseForbidden()


    wrap.__doc__ = func.__doc__
    wrap.__name__ = func.__name__
    return wrap