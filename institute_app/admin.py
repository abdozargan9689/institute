from django.contrib import admin
from .models import Student, Course, Subject, Enrollment, Grade

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id_card_number', 'rank', 'full_name', 'unit')
    search_fields = ('id_card_number', 'full_name', 'rank', 'unit')
    list_filter = ('rank', 'unit')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'start_date', 'end_date')
    search_fields = ('name', 'code', 'description')
    list_filter = ('start_date', 'end_date')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'course', 'max_grade')
    search_fields = ('name', 'code')
    list_filter = ('course',)

class GradeInline(admin.TabularInline):
    model = Grade
    extra = 1

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date', 'is_completed')
    search_fields = ('student__full_name', 'student__id_card_number', 'course__name')
    list_filter = ('course', 'is_completed', 'enrollment_date')
    inlines = [GradeInline]

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'subject', 'grade_type', 'grade_name', 'score', 'max_score', 'date_achieved')
    search_fields = ('enrollment__student__full_name', 'subject__name', 'grade_name')
    list_filter = ('grade_type', 'subject', 'date_achieved')
