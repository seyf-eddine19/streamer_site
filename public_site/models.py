from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# محتوى نصوص عامة ديناميكية
class SiteTextContent(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value_ar = models.TextField(verbose_name="النص (عربي)")
    value_en = models.TextField(verbose_name="Text (English)")
    note = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.key

# أعضاء الفريق
class TeamMember(models.Model):
    name_ar = models.CharField(max_length=100)
    name_en = models.CharField(max_length=100)
    role_ar = models.CharField(max_length=100, verbose_name="الدور (عربي)")
    role_en = models.CharField(max_length=100, verbose_name="Role (English)")
    image = models.ImageField(upload_to='public_site/team/')
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)

    def __str__(self):
        return self.name_ar

# الخدمات
class Service(models.Model):
    title_ar = models.CharField(max_length=100, verbose_name="العنوان (عربي)")
    title_en = models.CharField(max_length=100, verbose_name="Title (English)")
    description_ar = models.TextField(verbose_name="الوصف (عربي)")
    description_en = models.TextField(verbose_name="Description (English)")
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.title_ar


class Project(models.Model):
    title_ar = models.CharField(max_length=100, verbose_name="العنوان (عربي)")
    title_en = models.CharField(max_length=100, verbose_name="Title (English)")
    
    # بدل category بـ ManyToMany
    categories = models.ManyToManyField('ProjectCategory', verbose_name="التصنيفات")

    description_ar = models.TextField(blank=True, verbose_name="الوصف (عربي)")
    description_en = models.TextField(blank=True, verbose_name="Description (English)")
    image = models.ImageField(upload_to='public_site/projects/')
    date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title_ar


class ProjectCategory(models.Model):
    name_en = models.CharField(max_length=100, unique=True, verbose_name="Name (English)")
    name_ar = models.CharField(max_length=100, unique=True, verbose_name="الاسم (عربي)")

    def __str__(self):
        return self.name_ar

# الالعاب
class Game(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name="الدور (عربي)")
    name_en = models.CharField(max_length=100, verbose_name="Role (English)")
    image = models.ImageField(upload_to='public_site/games/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name_ar

# الأسئلة الشائعة
class FAQ(models.Model):
    question_ar = models.CharField(max_length=255, verbose_name="السؤال (عربي)")
    question_en = models.CharField(max_length=255, verbose_name="Question (English)")
    answer_ar = models.TextField(verbose_name="الجواب (عربي)")
    answer_en = models.TextField(verbose_name="Answer (English)")

    def __str__(self):
        return self.question_ar

# التقييمات (من العملاء أو المتابعين)
class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    address = models.CharField(max_length=255, blank=True, verbose_name="المدينة أو الدولة")
    content_ar = models.TextField(verbose_name="التعليق (عربي)")
    content_en = models.TextField(verbose_name="Comment (English)")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="التقييم من 1 إلى 5"
    )
    facebook_url = models.URLField(blank=True, verbose_name="رابط فيسبوك")
    twitter_url = models.URLField(blank=True, verbose_name="رابط تويتر")
    linkedin_url = models.URLField(blank=True, verbose_name="رابط لينكدإن")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}★)"

# شعارات العملاء
class ClientLogo(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name="الاسم (عربي)")
    name_en = models.CharField(max_length=100, verbose_name="Name (English)")
    logo = models.ImageField(upload_to='public_site/clients/')

    def __str__(self):
        return self.name_ar

# رسائل التواصل
class ContactMessage(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.firstname} {self.lastname}"
