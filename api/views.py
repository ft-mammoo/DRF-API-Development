from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

def studentsView(request):
    students =Student.objects.all()
    return JsonResponse(list(students.values()), safe=False)
