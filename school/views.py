from django.shortcuts import render
from school.models import Student, Contact
import datetime
from django.contrib import messages
# Create your views here.


def index(request):
    name = Student.objects.all()
    context = {"name": name}

    return render(request, "index.html", context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.date.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')
