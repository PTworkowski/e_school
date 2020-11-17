from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def get_link(request):
    try:
        zoom = Zoom_link.objects.get(pk=zoom_link_id)
    except Zoom_link.DoesNotExist:
        raise Http404('Nie ma obecnie żadnych dostępnych linków.')
    return render(request,'student_app/get_link.html', {'Zoom_link : zoom'})

