from datetime import date, datetime
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main.models import *




def page_404(request):
    return render(request, 'admins/page-404.html')

#
def login_view(request):
    print(request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if user.count() > 0:
            usr = authenticate(username=username, password=password)
            if usr.status == 2:
                if usr is not None:
                    login(request, usr)
                    return redirect('admin_dashboard')
                else:
                    return redirect('login')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        return render(request, 'admins/login_admin.html')

#
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def reset_password(request):
    user = request.user
    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        prove = request.POST.get('confirm_password')
        usr = authenticate(username=user.username, password=password)
        if new_password == prove:
            usr.set_password(new_password)
            usr.save()
            return redirect('profile')
        return redirect('profile')
    return redirect('profile')


@login_required(login_url='login')
def admin_dashboard(request):
    context = {
        "student_deleted": Student.objects.filter(status=2).count(),
        "student_finished": Student.objects.filter(status=3).count(),
        "student_news": Student.objects.filter(status=1).count(),
        "student_all": Student.objects.all().count(),
        "course_all": Course.objects.all().count(),
        "student": Student.objects.all(),
    }
    return render(request, 'admins/index1.html', context)

@login_required(login_url='login')
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    if request.method == "POST":
        username = request.POST.get('username')
        img = request.FILES.get('img')
        number = request.POST.get('number')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        bio = request.POST.get('bio')
        email = request.POST.get('email')
        user.username = username
        user.number = number
        user.first_name = first_name
        user.last_name = last_name
        user.bio = bio
        user.email = email
        if img is None:
            user.img = user.img
        else:
            user.img = img


        user.save()
        return redirect('profile')

    return render(request, 'admins/profile.html', context)







@login_required(login_url='login')
def Student_views(request):
    context = {
        'student': Student.objects.all(),

    }
    return render(request,"admins/student.html", context)

@login_required(login_url='login')
def Student_views_new(request):
    context = {
        'student_new': Student.objects.filter(status=1),

    }
    return render(request,"admins/new_student.html", context)


@login_required(login_url='login')
def Student_views_finished(request):
    context = {
        'student': Student.objects.all(),
        'student_finished': Student.objects.filter(status=3),

    }
    return render(request,"admins/finished_student.html", context)


@login_required(login_url='login')
def Student_views_deleted(request):
    context = {
        'student_deleted': Student.objects.filter(status=2),

    }
    return render(request,"admins/deleted_student.html", context)


@login_required(login_url='login')
def add_student(request):
    name = request.POST('name')
    phone_number = request.POST('phone_number')
    cource = request.POST('course')

    Student.objects.create(name=name, phone_number=phone_number, cource=Course.objects.get(id=cource))

    return redirect("student")



@login_required(login_url='login')
def Course_views(request):
    context = {
        'course': Course.objects.all(),

    }
    return render(request,"admins/course.html", context)

@login_required(login_url='login')
def Link_views(request):
    context = {
        'link': Link.objects.all(),

    }
    return render(request,"admins/link.html", context)
@login_required(login_url='login')
def Mock_views(request):
    context = {
        'mock': Mock.objects.all(),

    }
    return render(request,"admins/mock.html", context)




@login_required(login_url='login')
def course_single(request,pk):
    context = {
        'course': Course.objects.get(id=pk),

    }
    return render(request,"admins/course_single.html", context)

@login_required(login_url='login')
def add_course(request):
    image = request.FILES.get("image")
    name = request.POST.get("name")
    text = request.POST.get("text")
    teacher = request.POST.get("teacher")
    price = request.POST.get('price')
    about = request.POST.get('about')
    schedule_start = request.POST.get('schedule_start')
    schedule_finish = request.POST.get('schedule_finish')
    Course.objects.create(image=image,name=name,text=text,price=price, teacher=Teacher.objects.get(id=teacher), about=about, schedule_start=schedule_start, schedule_finish=schedule_finish)
    return redirect("course")

@login_required(login_url='login')
def add_link(request):
    name = request.POST.get("name")
    link = request.POST.get('link')
    Link.objects.create(name=name, link=link)
    return redirect("link")

@login_required(login_url='login')
def add_mock(request):
    name = request.POST.get("name")
    price = request.POST.get('price')
    date = request.POST.get('date')
    Mock.objects.create(name=name, price=price, date=date)
    return redirect("mock")



def update_curse(request, pk):
    context = {
        'course': Course.objects.get(id=pk),
    }
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        image = request.FILES.get('image')
        name = request.POST.get("name")
        text = request.POST.get("text")
        teacher_name = request.POST.get("teacher")
        teacher_ielts = request.POST.get("teacher")
        price = request.POST.get("price")
        about = request.POST.get("about")
        schedule_start = request.POST.get("schedule_start")
        schedule_finish = request.POST.get('schedule_finish')
        course.name = name
        course.text = text
        course.teacher_name = teacher_name
        course.teacher_ielts = teacher_ielts
        course.price = price
        course.about = about
        course.schedule_start = schedule_start
        course.schedule_start = schedule_finish
        if image:
            course.image = image
        else:
            course.image = course.image
        course.save()
        return redirect('course')
    return render(request, 'admins/update-course.html', context)


def delete_course(request, pk):
    clear = Course.objects.get(id=pk)
    clear.delete()
    return redirect("course")


def update_link(request, pk):
    context = {
        'link': Link.objects.get(id=pk),
    }
    link = Link.objects.get(id=pk)
    if request.method == 'POST':
        links = request.POST.get("link")
        name = request.POST.get("name")
        link.link = links
        link.name = name
        link.save()
        return redirect('link')
    return render(request, 'admins/update-link.html', context)

def update_mock(request, pk):
    context = {
        'mock': Mock.objects.get(id=pk),
    }
    mock = Mock.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        date = request.POST.get("date")
        mock.price = price
        mock.name = name
        if date == '':
            mock.date = mock.date
        else:
            mock.date = date
        mock.save()
        return redirect('mock')
    return render(request, 'admins/update-mock.html', context)

def student_mock(request, pk):
    context = {
        'student_mock': Student.objects.filter(mock_id=pk),
    }
    return render(request, 'admins/mock-single.html', context)


def delete_link(request, pk):
    clear = Link.objects.get(id=pk)
    clear.delete()
    return redirect("link")


def delete_mock(request, pk):
    clear = Mock.objects.get(id=pk)
    clear.delete()
    return redirect("mock")



def delete_student(request, pk):
    clear = Student.objects.get(id=pk)
    clear.delete()
    return redirect("student")

def finished_student(request, pk):
    student = Student.objects.get(id=pk)
    student.status = 3
    student.save()
    return redirect("student")

def disactive_mock(request, pk):
    mock = Mock.objects.get(id=pk)
    mock.status = 2
    mock.save()
    return redirect("mock")

def active_mock(request, pk):
    mock = Mock.objects.get(id=pk)
    mock.status = 1
    mock.save()
    return redirect("mock")

def deleted_student(request, pk):
    student = Student.objects.get(id=pk)
    student.status = 2
    student.save()
    return redirect("student")