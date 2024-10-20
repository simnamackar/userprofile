
from django.contrib import admin
from django.urls import path,include
# from userapp.views import listview
from . import views
urlpatterns = [
path("register/",views.userregistration,name='register'),
path("personaldetails/",views.personaldetails,name='submit'),
path("",views.loginpage,name='login'),
path("logout/",views.logoutview,name='logout'),
path("details/",views.details,name='details'),
path("qualification/",views.qualifications,name='qualifications'),
path("experience/",views.experiences,name='experience'),
path("skills/",views.skills,name='skills'),
path("project/",views.projects,name='project'),
path("personalview/",views.personview,name='personview'),
path("qualificationview/",views.qualificationview,name='qualificationview'),
path("experienceview/",views.experienceview,name='experienceview'),
path("skillview/",views.skillview,name='skillview'),
path("projectview/",views.projectview,name='projectview')
]