from django.core.management.base import BaseCommand
from django.utils import timezone
from institute_app.models import Student, Course, Subject, Enrollment, Grade
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Creates sample data for testing the application'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Create students
        students = []
        ranks = ['ملازم', 'نقيب', 'رائد', 'مقدم', 'عقيد', 'عميد']
        units = ['الوحدة الأولى', 'الوحدة الثانية', 'الوحدة الثالثة', 'الوحدة الرابعة']
        
        for i in range(1, 21):
            id_card = f'ID{i:05d}'
            rank = random.choice(ranks)
            full_name = f'طالب رقم {i}'
            unit = random.choice(units)
            
            student = Student.objects.create(
                id_card_number=id_card,
                rank=rank,
                full_name=full_name,
                unit=unit
            )
            students.append(student)
            self.stdout.write(f'Created student: {student}')
        
        # Create courses
        courses = []
        today = timezone.now().date()
        
        for i in range(1, 6):
            start_date = today - timedelta(days=random.randint(30, 180))
            end_date = start_date + timedelta(days=random.randint(30, 90))
            
            course = Course.objects.create(
                name=f'دورة رقم {i}',
                code=f'C{i:03d}',
                description=f'وصف الدورة رقم {i}',
                start_date=start_date,
                end_date=end_date
            )
            courses.append(course)
            self.stdout.write(f'Created course: {course}')
            
            # Create subjects for each course
            subjects = []
            for j in range(1, 6):
                subject = Subject.objects.create(
                    course=course,
                    name=f'مادة {j} للدورة {i}',
                    code=f'S{i}{j:02d}',
                    max_grade=100
                )
                subjects.append(subject)
                self.stdout.write(f'Created subject: {subject}')
        
        # Create enrollments and grades
        for student in students:
            # Each student is enrolled in 1-3 random courses
            num_courses = random.randint(1, 3)
            selected_courses = random.sample(courses, num_courses)
            
            for course in selected_courses:
                enrollment_date = course.start_date + timedelta(days=random.randint(0, 5))
                is_completed = course.end_date < today
                
                enrollment = Enrollment.objects.create(
                    student=student,
                    course=course,
                    enrollment_date=enrollment_date,
                    is_completed=is_completed
                )
                self.stdout.write(f'Created enrollment: {student} in {course}')
                
                # Create grades for each subject in the course
                for subject in Subject.objects.filter(course=course):
                    # Subject grade
                    Grade.objects.create(
                        enrollment=enrollment,
                        subject=subject,
                        grade_type='subject',
                        grade_name=f'درجة المادة {subject.name}',
                        score=random.randint(60, 100),
                        max_score=100,
                        date_achieved=course.start_date + timedelta(days=random.randint(10, 20)),
                        notes=''
                    )
                    
                    # Exam grade
                    Grade.objects.create(
                        enrollment=enrollment,
                        subject=subject,
                        grade_type='exam',
                        grade_name=f'اختبار {subject.name}',
                        score=random.randint(60, 100),
                        max_score=100,
                        date_achieved=course.start_date + timedelta(days=random.randint(20, 30)),
                        notes=''
                    )
                    
                    # Project grade (only for some subjects)
                    if random.choice([True, False]):
                        Grade.objects.create(
                            enrollment=enrollment,
                            subject=subject,
                            grade_type='project',
                            grade_name=f'مشروع {subject.name}',
                            score=random.randint(60, 100),
                            max_score=100,
                            date_achieved=course.start_date + timedelta(days=random.randint(30, 40)),
                            notes=''
                        )
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))