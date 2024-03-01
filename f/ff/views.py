from django.shortcuts import render,redirect
from ff.models import Course
from ff.forms import EditForm

# Create your views here.
def home(req):
    context = {
        'course': Course.objects.all()
    }
    return render(req, 'home.html',context)

def search_id(req):
    course_id = req.GET.get('course_id')  # Now correctly matching the form input name
    context = {
        'search_id': Course.objects.filter(id=course_id)
    }
    return render(req, 'search_id.html', context)

def search_name(req):
    name = req.GET.get('name')  # รับรหัสวิชาจาก request
    context = {
        'search_name': Course.objects.filter(name=name)
    }
    return render(req, 'search_name.html',context)

def edit(req,id):
    form = EditForm()
    c = Course.objects.get(pk=id)
    if req.method == 'POST':
        form = EditForm(req.POST,instance=c)
        if form.is_valid():
           form.save()
           return redirect('/')
    else:
        form = EditForm(instance=c)
    context = {
        'c':c,
        'form':form    }
    return render(req,'edit.html',context)

def delete(req,id):
    c = Course.objects.get(pk=id)
    c.delete()
    return redirect('/')