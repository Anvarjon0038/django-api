from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Course
from .models import Category


# Create your views here.



def index(request):
    course=Course.objects.all()
    category=Category.objects.all()
    #return HttpResponse("Hi from the shop app")
    #return HttpResponse(''.join([str(i)+'<br>' for i in courses]))
    return render(request,template_name='shop/courses.html',context={'course':course})

def single_course(request,course_id):
    # try:
    #     course=Course.objects.get(pk=course_id)
    #     return render(request,'single_course.html',{'course':course,'num':range(5)})
    # except Course.DoesNotExist:
    #     raise Http404()

    #2
    course=get_object_or_404(Course,pk=course_id)
    return render(request,'shop/single_course.html',{'course':course})
