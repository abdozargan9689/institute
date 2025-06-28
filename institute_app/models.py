from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Student(models.Model):
    id_card_number = models.CharField(_('رقم البطاقة'), max_length=20, unique=True)
    rank = models.CharField(_('الرتبة'), max_length=50)
    full_name = models.CharField(_('الاسم الكامل'), max_length=100)
    unit = models.CharField(_('الوحدة'), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rank} {self.full_name}"

    class Meta:
        verbose_name = _('طالب')
        verbose_name_plural = _('الطلاب')

class Course(models.Model):
    name = models.CharField(_('اسم الدورة'), max_length=100)
    code = models.CharField(_('كود الدورة'), max_length=20, unique=True)
    description = models.TextField(_('وصف الدورة'), blank=True)
    start_date = models.DateField(_('تاريخ البداية'))
    end_date = models.DateField(_('تاريخ النهاية'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('دورة')
        verbose_name_plural = _('الدورات')

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects', verbose_name=_('الدورة'))
    name = models.CharField(_('اسم المادة'), max_length=100)
    code = models.CharField(_('كود المادة'), max_length=20)
    max_grade = models.PositiveIntegerField(_('الدرجة القصوى'), default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.course.name})"

    class Meta:
        verbose_name = _('مادة')
        verbose_name_plural = _('المواد')
        unique_together = ('course', 'code')

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments', verbose_name=_('الطالب'))
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments', verbose_name=_('الدورة'))
    enrollment_date = models.DateField(_('تاريخ التسجيل'), auto_now_add=True)
    is_completed = models.BooleanField(_('مكتملة'), default=False)
    handwritten_report = models.ImageField(_('تقرير بخط اليد'), upload_to='handwritten_reports/', blank=True, null=True)
    course_photo = models.ImageField(_('صورة الدورة'), upload_to='course_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student} - {self.course}"

    class Meta:
        verbose_name = _('تسجيل')
        verbose_name_plural = _('التسجيلات')
        unique_together = ('student', 'course')

class Grade(models.Model):
    GRADE_TYPES = (
        ('subject', _('مادة')),
        ('exam', _('اختبار')),
        ('project', _('مشروع')),
    )
    
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='grades', verbose_name=_('التسجيل'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades', verbose_name=_('المادة'))
    grade_type = models.CharField(_('نوع الدرجة'), max_length=10, choices=GRADE_TYPES)
    grade_name = models.CharField(_('اسم الدرجة'), max_length=100)
    score = models.DecimalField(_('الدرجة'), max_digits=5, decimal_places=2, 
                               validators=[MinValueValidator(0)])
    max_score = models.DecimalField(_('الدرجة القصوى'), max_digits=5, decimal_places=2, 
                                   validators=[MinValueValidator(0)])
    date_achieved = models.DateField(_('تاريخ الحصول'))
    notes = models.TextField(_('ملاحظات'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.enrollment.student} - {self.subject} - {self.grade_name}"

    class Meta:
        verbose_name = _('درجة')
        verbose_name_plural = _('الدرجات')
