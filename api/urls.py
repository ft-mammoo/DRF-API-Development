from django.urls import path
from . import views

urlpatterns = [
    #Function based views
    # path ('studentsFBV/', views.studentsView),
    # path('studentsFBV/<int:pk>/', views.studentDetailView),

    path('students/', views.Students.as_view()),
    path('students/<int:pk>/', views.StudentDetail.as_view()),

    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
]