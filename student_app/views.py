from django.db.models import query
from django.forms import Form
from django.shortcuts import render, redirect
from django.http import Http404


def get_link(request):
    try:
        Link = Zoom_link.objects.get(pk=zoom_link_id)
    except Zoom_link.DoesNotExist:
        raise Http404('Nie ma obecnie żadnych dostępnych linków.')
    return render(request,'student_app/get_link.html', {'Zoom_link : zoom'})


def view_File(request):
    if request.method == "GET":
        form = ViewFile(request.GET, request.get)
        if form.is_valid():
            id=request.POST.get("file_id")
            ans = query.objects.get(id=file_id)
            response=ans.repo
            if ans is None:
                return redirect("view-file.html")
            else:
                return redirect(response)
    else:
        form = Form()
    return render(request,"view-file.html",{'form':form})

#get success url