from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', views.StudentViewSet, basename='student')
router.register('employees', views.EmployeeViewSet)
router.register('blogs', views.BlogViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = [
    #Function based views
    # path ('studentsFBV/', views.studentsView),
    # path('studentsFBV/<int:pk>/', views.studentDetailView),

    # path('students/', views.Students.as_view()),
    # path('students/<int:pk>/', views.StudentDetail.as_view()),

    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),

    path('', include(router.urls))
]