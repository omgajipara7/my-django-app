from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from djangohelp.models import Member
def hello(request):
    return HttpResponse("hello this is my first project")

def hellohtml(request):
    return render(request,"html/hello.html")


from django.shortcuts import render,redirect
from djangohelp.models import Member  # Import the correct model

def members(request):
    # Retrieve all Member objects and get their values
    queryset = Member.objects.all()

    # Create the context dictionary
    context = {
        'members': queryset,
    }

    # Render the template with the context and return the response
    return render(request, 'html/2.html', context)



def details(request,id):
    queryset=Member.objects.get(id=id)

    # Create the context dictionary
    context = {
        'members': queryset,
    }

    # Render the template with the context and return the response
    return render(request, 'html/details.html', context)

def main(request):
    return render(request,"html/main.html")



#self practice

from djangohelp.models import Student

def student(request):
    if request.method=="POST":
        data=request.POST
        name=data.get('name')
        enroll=data.get('enroll')
        branch=data.get('branch')

        Student.objects.create(
            name=name,
            enroll=enroll,
            branch=branch,)
        return redirect('student')
    queryset = Student.objects.all()

    context={'student':queryset}
    return render(request,'html/student.html',context)

def stlist(request):
    queryset = Student.objects.all()
    context = {'student': queryset}


    return render(request,'html/stlist.html',context)



def stdetails(request,id):
    queryset=Auth.objects.get(id=id)
    context={
        'student':queryset
    }
    return render(request,'html/stdetails.html',context)



#authentication
from django.shortcuts import render, redirect
from .models import Auth

def auth(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username", "").strip().lower()
        password = data.get("password")
        enroll = data.get('enroll')
        branch = data.get('branch')
        if Auth.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
        else:
            Auth.objects.create(
                username=username,
                password=password,
                enroll=enroll,
                branch=branch,
            )
            return redirect('login')




    queryset = Auth.objects.all()
    context = {'auth': queryset}
    return render(request, 'html/auth.html', context)





from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Auth

def login(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username", "").strip().lower()
        password = data.get("password")

        try:
            user = Auth.objects.get(username=username, password=password)
            messages.success(request, "You have successfully logged in.")
            return redirect('stportal', id=user.username)  # Pass the username to stportal view
        except Auth.DoesNotExist:
            messages.error(request, "Invalid username or password.")

    return render(request, 'html/login.html')




from django.shortcuts import render, get_object_or_404
from .models import Auth  # Adjust the import path as per your project structure

def stportal(request, id):
    user = get_object_or_404(Auth, username=id)
    context = {
        'student': user  # Pass the user object directly
    }
    return render(request, 'html/stportal.html', context)



#testing

def testing(request):
    queryset=Student.objects.all().values()
    context={
        'student': queryset,
        'firstname': 'Linus',
        'fruits':['apple,banana,mango']
    }
    return render(request,'html/test.html',context)