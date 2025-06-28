from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from .models import Student, Course, Subject, Enrollment, Grade

def home(request):
    """Home page view."""
    students_count = Student.objects.count()
    courses_count = Course.objects.count()
    enrollments_count = Enrollment.objects.count()
    
    context = {
        'students_count': students_count,
        'courses_count': courses_count,
        'enrollments_count': enrollments_count,
    }
    return render(request, 'institute_app/home.html', context)

class StudentListView(ListView):
    """View for listing all students."""
    model = Student
    template_name = 'institute_app/student_list.html'
    context_object_name = 'students'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(id_card_number__icontains=search_query) |
                Q(full_name__icontains=search_query) |
                Q(rank__icontains=search_query) |
                Q(unit__icontains=search_query)
            )
        return queryset

class StudentDetailView(DetailView):
    """View for displaying student details."""
    model = Student
    template_name = 'institute_app/student_detail.html'
    context_object_name = 'student'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student = self.get_object()
        enrollments = student.enrollments.all()
        context['enrollments'] = enrollments
        return context

class CourseListView(ListView):
    """View for listing all courses."""
    model = Course
    template_name = 'institute_app/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(code__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset

class CourseDetailView(DetailView):
    """View for displaying course details."""
    model = Course
    template_name = 'institute_app/course_detail.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        subjects = course.subjects.all()
        enrollments = course.enrollments.all()
        context['subjects'] = subjects
        context['enrollments'] = enrollments
        return context

class EnrollmentDetailView(DetailView):
    """View for displaying enrollment details with grades."""
    model = Enrollment
    template_name = 'institute_app/enrollment_detail.html'
    context_object_name = 'enrollment'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enrollment = self.get_object()
        
        # Get grades grouped by type
        subject_grades = enrollment.grades.filter(grade_type='subject')
        exam_grades = enrollment.grades.filter(grade_type='exam')
        project_grades = enrollment.grades.filter(grade_type='project')
        
        context['subject_grades'] = subject_grades
        context['exam_grades'] = exam_grades
        context['project_grades'] = project_grades
        
        return context

def search_view(request):
    """View for searching students, courses, and enrollments."""
    query = request.GET.get('q', '')
    students = []
    courses = []
    
    if query:
        students = Student.objects.filter(
            Q(id_card_number__icontains=query) |
            Q(full_name__icontains=query) |
            Q(rank__icontains=query) |
            Q(unit__icontains=query)
        )
        
        courses = Course.objects.filter(
            Q(name__icontains=query) |
            Q(code__icontains=query) |
            Q(description__icontains=query)
        )
    
    context = {
        'query': query,
        'students': students,
        'courses': courses,
    }
    
    return render(request, 'institute_app/search_results.html', context)
