from django.shortcuts import redirect, render

from courseapp.models import Course

def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'course/home.html',context)

def delete(req,id):
    c = Course.objects.get(pk=id)
    c.delete()
    # return redirect('/')
    return render(req, 'course/delete.html')