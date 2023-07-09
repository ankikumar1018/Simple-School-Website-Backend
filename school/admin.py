from django.contrib import admin
from school.models import School, Student, Teacher, Contact


admin.site.register([School, Student, Teacher, Contact])
