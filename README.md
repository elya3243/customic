# Mockup Builder Django Project

یک پروژه Django برای ساخت **mockup تصاویر لباس‌ها** با استفاده از متن ورودی کاربر و پردازش تصویر با **Pillow** و **Celery**. پروژه به کاربران امکان می‌دهد متن دلخواه خود را روی تصاویر موجود در سرور قرار دهند و تصاویر نهایی را دریافت کنند.

---

## ویژگی‌ها

- مدیریت کاربران با مدل پیش‌فرض Django
- مدل‌های `Mockup` و `Dress` برای ذخیره متن‌ها و تصاویر
- APIهای RESTful با استفاده از **Django REST Framework**
- پردازش تصویر با **Pillow**
- اجرای پردازش‌ها به صورت **Asynchronous** با **Celery**
- پیگیری وضعیت تسک‌ها و دریافت نتایج

---

## ساختار پروژه

- **models.py**  
  - `BaseModel`: مدل انتزاعی برای افزودن فیلد `created_at`  
  - `Mockup`: شامل متن و کاربر  
  - `Dress`: شامل تصویر و رابطه با `Mockup`  

- **serializers.py**  
  - `MockupSerializer`: سریالایزر برای Mockup و تصاویر مرتبط  
  - `DressSerializer`: سریالایزر برای تصاویر  

- **views.py**  
  - `MockupCreateView`: ایجاد mockup جدید و شروع تسک Celery  
  - `MockupListView`: مشاهده لیست mockupها  
  - `MockupStatusAPIView`: بررسی وضعیت تسک و دریافت تصاویر نهایی  

- **tasks.py**  
  - `mockup_builder`: پردازش تصاویر موجود و قرار دادن متن روی آن‌ها  

---

## نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.10+
- Django 4.x
- Django REST Framework
- Celery
- Redis یا هر broker دیگری برای Celery
- Pillow

### مراحل نصب

1. کلون کردن پروژه:
```bash
git clone <repo_url>
cd <project_folder>


نصب وابستگی‌ها:
pip install -r requirements.txt

اجرای migrations:
python manage.py makemigrations
python manage.py migrate

ساخت سوپر یوزر:
python manage.py createsuperuser

اجرای سرور توسعه:
python manage.py runserver

اجرای Celery:
celery -A <project_name> worker --loglevel=info

استفاده از API
ایجاد Mockup
URL: /api/v1/mockups/

Method: POST

Headers: Authorization: Bearer <user_token>

Body:
{
  "text": "متن شما برای قرار گرفتن روی لباس"
}
Response:
{
  "task_id": "abc123",
  "status": "PENDING",
  "message": "ساخت تصویر آغاز شد."
}
دریافت وضعیت تسک
URL: /api/v1/tasks/<task_id>/

Method: GET

Response:
{
  "task_id": "abc123",
  "status": "SUCCESS",
  "result": [
    {
      "image_url": "/media/edited/1/image1.png",
      "created_at": "2025-11-04T15:00:00Z"
    }
  ]
}
لیست Mockupها
URL: /api/v1/mockups/list/

Method: GET

Query Params: text=<filter_text> (اختیاری)

پوشه‌ها
static/shirts/: تصاویر اولیه برای mockup

media/edited/: تصاویر نهایی ساخته شده

توسعه و تست
اضافه کردن تصاویر جدید در پوشه static/shirts/

تنظیمات Celery و Redis در settings.py

تغییر فونت یا موقعیت متن در tasks.py

