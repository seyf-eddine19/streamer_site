from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class SiteContent(models.Model):
    SECTION_CHOICES = [
        ('header', _('Header')),
        ('hero', _('Hero')),
        ('about', _('About')),
        ('games', _('Games')),
        ('services', _('Services')),
        ('projects', _('Projects')),
        ('faq', _('FAQ')),
        ('testimonials', _('Testimonials')),
        ('clients', _('Clients')),
        ('contact', _('Contact')),
        ('footer', _('Footer')),
    ]

    TYPE_CHOICES = [
        ('title', _('Title')),
        ('subtitle', _('Subtitle')),
        ('paragraph', _('Paragraph')),
        ('button', _('Button')),
        ('image', _('Image')),
        ('video', _('Video')),
        ('link', _('Link')),
    ]

    # PAGE_CHOICES = [
    #     ('home', _('home')),
    #     ('about', _('about')),
    #     ('projects', _('projects')),
    #     ('contact', _('contact')),
    # ]
    
    section = models.CharField(max_length=50, choices=SECTION_CHOICES, verbose_name=_("Section"))
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name=_("Content Type"))
    # pages = models.CharField(max_length=200, verbose_name=_("Pages"), help_text=_("Select pages separated by commas like: home,about"),)
    key = models.CharField(max_length=100, unique=True, verbose_name=_("Unique Key"))
    content_ar = models.TextField(blank=True, verbose_name=_("Content (Arabic)"))
    content_en = models.TextField(blank=True, verbose_name=_("Content (English)"))

    def get_pages_list(self):
        return self.pages.split(',') if self.pages else []

    def get_pages_display(self):
        return [dict(self.PAGE_CHOICES).get(p, p) for p in self.get_pages_list()]

    class Meta:
        verbose_name = _("Site Content Item")
        verbose_name_plural = _("Site Content")
        ordering = ['key']
        unique_together = ('section', 'key')

    def __str__(self):
        return f"{self.section} - {self.type} - {self.key}"


class TeamMember(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name=_("Name (Arabic)"))
    name_en = models.CharField(max_length=100, verbose_name=_("Name (English)"))
    role_ar = models.CharField(max_length=100, verbose_name=_("Role (Arabic)"))
    role_en = models.CharField(max_length=100, verbose_name=_("Role (English)"))
    image = models.ImageField(upload_to='public_site/team/', verbose_name=_("Image"))
    facebook_url = models.URLField(blank=True, verbose_name=_("Facebook URL"))
    instagram_url = models.URLField(blank=True, verbose_name=_("Instagram URL"))
    twitter_url = models.URLField(blank=True, verbose_name=_("Twitter URL"))

    class Meta:
        verbose_name = _("Team Member")
        verbose_name_plural = _("Team Members")

    def __str__(self):
        return self.name_ar


class Service(models.Model):
    title_ar = models.CharField(max_length=100, verbose_name=_("Title (Arabic)"))
    title_en = models.CharField(max_length=100, verbose_name=_("Title (English)"))
    description_ar = models.TextField(verbose_name=_("Description (Arabic)"))
    description_en = models.TextField(verbose_name=_("Description (English)"))
    icon = models.CharField(max_length=100, verbose_name=_("Icon"))

    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

    def __str__(self):
        return self.title_ar


class Project(models.Model):
    title_ar = models.CharField(max_length=100, verbose_name=_("Title (Arabic)"))
    title_en = models.CharField(max_length=100, verbose_name=_("Title (English)"))
    categories = models.ManyToManyField('ProjectCategory', verbose_name=_("Categories"))
    description_ar = models.TextField(blank=True, verbose_name=_("Description (Arabic)"))
    description_en = models.TextField(blank=True, verbose_name=_("Description (English)"))
    image = models.ImageField(upload_to='public_site/projects/', verbose_name=_("Image"))
    date = models.DateField(default=timezone.now, blank=True, null=True, verbose_name=_("Date"))

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title_ar


class ProjectCategory(models.Model):
    name_en = models.CharField(max_length=100, unique=True, verbose_name=_("Name (English)"))
    name_ar = models.CharField(max_length=100, unique=True, verbose_name=_("Name (Arabic)"))

    class Meta:
        verbose_name = _("Project Category")
        verbose_name_plural = _("Project Categories")

    def __str__(self):
        return self.name_ar


class Game(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name=_("Name (Arabic)"))
    name_en = models.CharField(max_length=100, verbose_name=_("Name (English)"))
    image = models.ImageField(upload_to='public_site/games/', verbose_name=_("Image"))
    url = models.URLField(blank=True, verbose_name=_("Game URL"))

    class Meta:
        verbose_name = _("Game")
        verbose_name_plural = _("Games")

    def __str__(self):
        return self.name_ar


class FAQ(models.Model):
    question_ar = models.CharField(max_length=255, verbose_name=_("Question (Arabic)"))
    question_en = models.CharField(max_length=255, verbose_name=_("Question (English)"))
    answer_ar = models.TextField(verbose_name=_("Answer (Arabic)"))
    answer_en = models.TextField(verbose_name=_("Answer (English)"))

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.question_ar


class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    address = models.CharField(max_length=255, blank=True, verbose_name=_("City or Country"))
    content_ar = models.TextField(verbose_name=_("Comment (Arabic)"))
    content_en = models.TextField(verbose_name=_("Comment (English)"))
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name=_("Rating (1 to 5)")
    )
    facebook_url = models.URLField(blank=True, verbose_name=_("Facebook URL"))
    twitter_url = models.URLField(blank=True, verbose_name=_("Twitter URL"))
    linkedin_url = models.URLField(blank=True, verbose_name=_("LinkedIn URL"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")

    def __str__(self):
        return f"{self.name} ({self.rating}★)"


class ClientLogo(models.Model):
    name_ar = models.CharField(max_length=100, verbose_name=_("Name (Arabic)"))
    name_en = models.CharField(max_length=100, verbose_name=_("Name (English)"))
    logo = models.ImageField(upload_to='public_site/clients/', verbose_name=_("Logo"))

    class Meta:
        verbose_name = _("Client Logo")
        verbose_name_plural = _("Client Logos")

    def __str__(self):
        return self.name_ar


class ContactMessage(models.Model):
    firstname = models.CharField(max_length=100, verbose_name=_("First Name"))
    lastname = models.CharField(max_length=100, verbose_name=_("Last Name"))
    email = models.EmailField(verbose_name=_("Email"))
    phone_number = models.CharField(max_length=20, blank=True, verbose_name=_("Phone Number"))
    message = models.TextField(verbose_name=_("Message"))
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Sent At"))

    class Meta:
        verbose_name = _("Contact Message")
        verbose_name_plural = _("Contact Messages")

    def __str__(self):
        return f"Message from {self.firstname} {self.lastname}"
