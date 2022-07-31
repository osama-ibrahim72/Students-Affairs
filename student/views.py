from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from student.models import Student,Courses


def add_dept(request,id):
    stud = Student.objects.get(sid=id)
    
    if request.method == "POST":
        stud.depart = request.POST['department']
        stud.save()
    context = {'student':stud}
    return render(request, 'student/add_dept.html',context)

def add(request):
    if request.method == "POST":
        name = request.POST['name']
        id = request.POST['id']
        email = request.POST['email']
        gpa = request.POST['gpa']
        lvl = request.POST['lvl']
        date = request.POST['date']
        status = request.POST['status']
        dep = request.POST['department']
        mobile = request.POST['mobile']
        student = Student(name=name,sid=id,email=email,gpa=gpa,lvl=lvl,dateOfBirth=date,depart=dep,mobileNum=mobile)
        student.save()

    return render(request, 'student/add.html')

def dep(request):
    obj = None
    if request.method=="POST":
        name = request.POST["s"]
        obj = None
        try:
            obj= Student.objects.filter(depart = name)
        except :
            obj =None
    return render(request, 'student/dep.html',{'stu':obj})

def grades(request,id):
    stud = Student.objects.filter(sid =id)
    coo = Courses.objects.filter(students__id__in=stud.all())
    return render(request, 'student/grades.html',{'coo':coo})

def profile(request,id):
    
    stuu = Student.objects.get(sid = id)
    context ={"student":stuu} 
    return render(request, 'student/profile.html',context)

def search(request):
    obj = None
    if request.method=="POST":
        name = request.POST["s"]
        obj = None
        try:
            obj= Student.objects.get(name = name)
        except :
            obj =None
    # q_dict = request.GET
    # try:
    #     qury = q_dict.get("s")
    # except:
    #     qury = None
    # obj = None
    # if qury is not None :
    #     obj = Student.objects.get(name=qury)
    return render(request, 'student/search.html', {'stu':obj})

def update(request,id):
    stud = Student.objects.get(sid=id)
    context = {'student':stud}
    if request.method == "POST":
        stud.name = request.POST['name']
        # id = request.POST['id']
        stud.email = request.POST['email']
        stud.gpa = request.POST['gpa']
        stud.lvl = request.POST['lvl']
        stud.date = request.POST['date']
        # stud.status = request.POST['status']
        # stud.dep = request.POST['department']
        stud.mobile = request.POST['mobile']
        stud.save()
    return render(request, 'student/update.html',context)

def view(request,id):
    # cooon =[1,2,3,4]
    try:
        stud = Student.objects.filter(lvl =int(id))
    except stud.DoesNotExist:
        stud = None
    return render(request, 'student/view.html',{'student':stud},)

def delete(request,id):
    stud = Student.objects.get(sid=id)
    stud.delete()
    return view(request,1)


# Create your views here.
