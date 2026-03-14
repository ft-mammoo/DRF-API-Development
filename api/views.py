from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
    students = {
        'id': 1,
        'name': 'Mandrake',
        'age': 20,
        'course': 'Computer Science',
    }

    return JsonResponse(students)
