from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required

from .models import Personaldetails,Qualifications,Experience,Skills,Projects


def userregistration(request):



    if request.method == "POST":

        username = request.POST['username']
        # firstname = request.POST['firstname']
        # lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        # password2 = request.POST['password2']
        # username = request.POST['username']
        # password = request.POST['password']
        # login_table.password2 = request.POST['password2']
        # login_table.type = 'user'
        # personal_details.username=request.POST['username']




        if request.POST['password'] == request.POST['password2']:
            # user_profile.save()
            # login_table.save()
            # personal_details.save()
            user = User.objects.create_user(username=username,email=email, password=password)
            user.save()
            messages.info(request, 'registration successfull')
            return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
    return render(request, 'register.html')


def loginpage(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     # password2 = request.POST['password2']
    #     user = logintable.objects.filter(username=username, password=password, type='user').exists()
    #     try:
    #         if user is not None:
    #             user_details = logintable.objects.get(username=username, password=password)
    #             user_name = user_details.username
    #             type = user_details.type
    #
    #             if type == 'user':
    #                 request.session['username'] = user_name
    #                 return redirect('details')
    #             elif type == 'admin':
    #                 request.session['username'] = user_name
    #                 return redirect('admin_view')
    #         else:
    #             messages.error(request, 'invalid username or password')
    #     except:
    #         messages.error(request, 'invalid role')
    # return render(request, 'login.html')



        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('details')  # Redirect to personal details form after login.
            else:
                messages.error(request, "Invalid username or password")

        return render(request, 'login.html')
@login_required
def personaldetails(request):

    user = request.user
    try:
        personal_details = Personaldetails.objects.get(user=user)
    except Personaldetails.DoesNotExist:
        personal_details = Personaldetails(user=user)

    if request.method == "POST":
        personal_details.firstname = request.POST['firstname']
        personal_details.lastname = request.POST['lastname']
        personal_details.email = request.POST['email']
        personal_details.place = request.POST['place']
        personal_details.sex = request.POST['sex']
        personal_details.dob = request.POST['dob']
        personal_details.address = request.POST['address']
        personal_details.relation = request.POST['relation']
        personal_details.phone = request.POST['phone']

        personal_details.save()

        return redirect('details')
    return render(request,'personaldetails.html',{'personal_details':personal_details})

def details(request):
    return render( request,'details.html')

@login_required
def qualifications(request):

    try:
       qualification = Qualifications.objects.get(user=request.user)
    except Qualifications.DoesNotExist:
        qualification = Qualifications(user=request.user)


    if request.method == "POST":
        qualification.sslc = request.POST['sslc']
        qualification.sslcmark = request.POST['sslcmark']
        qualification.plustwo = request.POST['plustwo']
        qualification.plustwomark = request.POST['plustwomark']
        qualification.degree = request.POST['degree']
        qualification.degreemark = request.POST['degreemark']
        qualification.pg = request.POST['pg']
        qualification.pgmark = request.POST['pgmark']


        qualification.save()

        return redirect('details')
    return render(request,'qualification.html',{'qualification':qualification})
@login_required()
def experiences(request):
    try:
        experience = Experience.objects.get(user=request.user)
    except Experience.DoesNotExist:
        experience=Experience(user=request.user)

    if request.method =="POST":
        experience.experience1 = request.POST['experience1']
        experience.experience2 = request.POST['experience2']
        experience.experience3 = request.POST['experience3']
        experience.experience4 = request.POST['experience4']

        experience.save()

        return redirect('details')
    return render(request,'experience.html',{'experience':experience})

def skills(request):
    try:
        skill=Skills.objects.get(user=request.user)
    except Skills.DoesNotExist:
        skill=Skills(user=request.user)

    if request.method =='POST':
        skill.skill1=request.POST['skill1']
        skill.skill2 = request.POST['skill2']
        skill.skill1 = request.POST['skill1']
        skill.skill1 = request.POST['skill1']
        skill.save()
        return redirect('details')
    return render(request,'skillS.html',{'skill':skill})

def projects(request):
    try:
        project1=Projects.objects.get(user=request.user)
    except Projects.DoesNotExist:
        project1=Projects(user=request.user)

    if request.method=="POST":
        project1.projectname=request.POST['projectname']
        project1.image=request.POST['image']
        project1.link=request.POST['link']
        project1.save()
        return redirect('details')
    return render(request,'projects.html',{'project1':project1})
def logoutview(request):
    logout(request)
    return redirect('login')
@login_required
def personview(request):
    # pview=Personaldetails.objects.all(user=request.user)
    try:
        pview=Personaldetails.objects.get(user=request.user)
    except Personaldetails.DoesNotExist:
        pview = Qualifications(user=request.user)
    return render(request,'viewpersonaldetails.html',{'pview':pview})


def qualificationview(request):
    try:
        qview=Qualifications.objects.get(user=request.user)
    except Qualifications.DoesNottExist:
        qview=Qualifications(user=request.user)
    return render(request,'viewqualification.html',{'qview':qview})

def experienceview(request):
    try:
        eview=Experience.objects.get(user=request.user)
    except Experience.DoesNotExist:
        eview=Experience(user=request.user)
    return render(request,'viewexperience.html',{'eview':eview})

def skillview(request):
    try:
        sview=Skills.objects.get(user=request.user)
    except Skills.DoesNotExist:
        sview=Skills(user=request.user)
    return render(request,'viewskill.html',{'sview':sview})

def projectview(request):
    try:
        proview=Projects.objects.get(user=request.user)
    except Projects.DoesNotExist:
        proview=Projects(user=request.user)
    return render(request,'viewproject.html',{'proview':proview})