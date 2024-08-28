from django.shortcuts import render
from .models import *

# Create your views here.
def home_page(request):
    myinfo = PersonalInformation.objects.all()
    myabout = About.objects.all()
    myprojects = Projects.objects.all()
    myskills = Skills.objects.all()
    myachievements = Achievements.objects.all()
    mycontact = Contact.objects.all()
    
    context = {
        "info": myinfo,
        "about": myabout,
        "projects": myprojects,
        "skills": myskills,
        "achievements": myachievements,
        "contacts": mycontact,
    }

    return render(request, "home_page.html", context)
