# نظام إدارة المعهد

نظام متكامل لإدارة المعهد، يتيح تتبع الطلاب والدورات والدرجات.

## الميزات الرئيسية

- إدارة بيانات الطلاب (رقم البطاقة، الرتبة، الاسم الكامل، الوحدة)
- إدارة الدورات التدريبية
- تسجيل الطلاب في الدورات
- تسجيل درجات المواد والاختبارات والمشاريع
- تقارير بخط اليد وصور للدورات
- نظام بحث متكامل

## المتطلبات التقنية

- Python 3.8+
- Django 5.2+
- MySQL/MariaDB
- Bootstrap 5

## التثبيت

1. استنساخ المشروع:
```
git clone https://github.com/abdozargan9689/institute.git
cd institute
```

2. إنشاء بيئة افتراضية وتفعيلها:
```
python -m venv venv
source venv/bin/activate  # على Linux/Mac
venv\Scripts\activate  # على Windows
```

3. تثبيت المتطلبات:
```
pip install -r requirements.txt
```

4. إنشاء قاعدة البيانات:
```
mysql -u root -p
CREATE DATABASE institute_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
exit
```

5. تعديل إعدادات قاعدة البيانات في ملف `institute_project/settings.py`

6. تنفيذ الترحيلات:
```
python manage.py migrate
```

7. إنشاء مستخدم مدير:
```
python manage.py createsuperuser
```

8. إنشاء بيانات تجريبية (اختياري):
```
python manage.py create_sample_data
```

9. تشغيل الخادم:
```
python manage.py runserver
```

10. الوصول إلى النظام عبر المتصفح:
- واجهة المستخدم: http://localhost:8000/
- لوحة الإدارة: http://localhost:8000/admin/

## هيكل المشروع

- `institute_project/`: إعدادات المشروع الرئيسية
- `institute_app/`: تطبيق إدارة المعهد
  - `models.py`: نماذج البيانات
  - `views.py`: المعالجات
  - `urls.py`: مسارات URL
  - `admin.py`: إعدادات لوحة الإدارة
  - `templates/`: قوالب HTML
- `static/`: الملفات الثابتة (CSS، JavaScript)
- `media/`: ملفات الوسائط المرفوعة

## النماذج الرئيسية

1. **الطالب (Student)**:
   - رقم البطاقة
   - الرتبة
   - الاسم الكامل
   - الوحدة

2. **الدورة (Course)**:
   - اسم الدورة
   - كود الدورة
   - وصف الدورة
   - تاريخ البداية والنهاية

3. **المادة (Subject)**:
   - اسم المادة
   - كود المادة
   - الدورة المرتبطة
   - الدرجة القصوى

4. **التسجيل (Enrollment)**:
   - الطالب
   - الدورة
   - تاريخ التسجيل
   - حالة الإكمال
   - تقرير بخط اليد
   - صورة الدورة

5. **الدرجة (Grade)**:
   - التسجيل
   - المادة
   - نوع الدرجة (مادة، اختبار، مشروع)
   - اسم الدرجة
   - الدرجة المحصلة
   - الدرجة القصوى
   - تاريخ الحصول
   - ملاحظات