from django.db.models import query
from django.forms import Form
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect


def get_link(request):
    try:
        Link = Zoom_link.objects.get(pk=zoom_link_id)
    except Zoom_link.DoesNotExist:
        raise Http404('Nie ma obecnie żadnych dostępnych linków.')
    return render(request,'student_app/get_link.html', {'Zoom_link : zoom'})

def get_File(request):
    if request.method == "GET":
        form = DownloadFile(request.GET, request.get)
        if form.is_valid():
            id=request.POST.get("id")
            ans = query.objects.get(id=id)
            response=ans.repo
            if ans is None:
                return redirect("file.html")
            else:
                return redirect(response)
    else:
        form = Form()
    return render(request,"file.html",{'form':form})