from django.shortcuts import render
from django.http import HttpResponse
from .models import Courses, CustomUsers, Lesson, Tests
from .forms import MyUserLogin, MyUserRegister

# Create your views here.
def index(request):

    login_form = MyUserLogin()
    

    context = {'login_form':login_form}

    return render(request, 'login.html', context=context)

def register(request):

    register_form = MyUserRegister()
    context = {'register_form':register_form}

    return render(request, 'register.html', context=context)

def course(request, course_name):

    wanted_course = Courses.objects.get(course_name=course_name)
    lessons = Lesson.objects.filter(course_lesson=wanted_course)
    try:
        lesson_test = Tests.objects.get(for_course=wanted_course)
    except:
        lesson_test = None
    context = {'course':wanted_course, 'lessons':lessons, 'tests':lesson_test}

    return render(request, 'Course.html', context=context)

def home(request, points):

    print(request.user)
    curr_user = CustomUsers.objects.get(id=request.user.id)
    curr_user.world_points = curr_user.world_points + points
    curr_user.save()

    courses = Courses.objects.all()
    context = {'courses':courses}
    print(courses)
    return render(request, 'Low fidelity prototype.html', context=context)

def daily_task(request):
    return render(request, 'Daily task.html')

def profile(request):

    user = CustomUsers.objects.get(id=request.user.id)
    print("Hello")
    print(user.user.username)
    print("Goodbye")
    user_courses = Courses.objects.filter(students=user)
    context = {'user':user, 'user_courses':user_courses}
    return render(request, 'Profile.html', context=context)

def world_rankings(request):

    users  = CustomUsers.objects.order_by('-world_points')

    context = {'users':users}

    return render(request, 'World_rankings.html', context=context)

