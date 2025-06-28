from django.urls import path
from . import views

app_name = 'institute_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('enrollments/<int:pk>/', views.EnrollmentDetailView.as_view(), name='enrollment_detail'),
    path('search/', views.search_view, name='search'),
]