from django.db.models import query
from django.forms import Form
from django.shortcuts import render, redirect
from administration_app import Course


def get_link(request):
    link = Course.objects.get(id=zoom_link_id)
    return render(request,'student_app/get_link.html', {'Zoom_link : zoom'})


def view_file(request):
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