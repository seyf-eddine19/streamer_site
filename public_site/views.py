from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import get_language
from .models import (
    SiteTextContent, TeamMember, Service, Project, ProjectCategory,
    Game, FAQ, Testimonial, ClientLogo
)
from .forms import ContactForm

def home_view(request):
    lang = get_language()  # 'en' أو 'ar'

    # تحضير النصوص حسب اللغة
    def get_translated(queryset, field_ar, field_en):
        field = field_en if lang == 'en' else field_ar
        return [getattr(obj, field) for obj in queryset]

    # تحميل البيانات
    site_texts = SiteTextContent.objects.all()
    team_members = TeamMember.objects.all()
    services = Service.objects.all()
    projects = Project.objects.all()
    games = Game.objects.all()
    faqs = FAQ.objects.all()
    testimonials = Testimonial.objects.all().order_by('-created_at')[:12]
    total_reviews = testimonials.count()
    client_logos = ClientLogo.objects.all()

    context = {
        'site_texts': {t.key: t.value_en if lang == 'en' else t.value_ar for t in site_texts},
        'team_members': team_members,
        'services': services,
        'projects': projects,
        'games': games,
        'faqs': faqs,
        'testimonials': testimonials,
        'total_reviews': total_reviews,
        'client_logos': client_logos,
        'lang': lang,
    }

    return render(request, 'public_site/index.html', context)

def about_view(request):
    lang = request.LANGUAGE_CODE  # أو حسب اختيارك
    testimonials = Testimonial.objects.all().order_by('-created_at')[:12]
    total_reviews = testimonials.count()
    client_logos = ClientLogo.objects.all()

    return render(request, 'public_site/about.html', {
        'testimonials': testimonials,
        'total_reviews': total_reviews,
        'client_logos': client_logos,
        'lang': lang
    })

def projects_view(request):
    lang = request.LANGUAGE_CODE  # أو حسب اختيارك
    categories = ProjectCategory.objects.all()
    projects_by_category = {category: Project.objects.filter(categories=category) for category in categories}
    testimonials = Testimonial.objects.all().order_by('-created_at')[:12]
    total_reviews = testimonials.count()
    faqs = FAQ.objects.all()
    client_logos = ClientLogo.objects.all()

    return render(request, 'public_site/projects.html', {
        'categories': categories,
        'projects_by_category': projects_by_category,
        'testimonials': testimonials,
        'total_reviews': total_reviews,
        'client_logos': client_logos,
        'faqs': faqs,
        'lang': lang
    })


def contact_view(request):
    lang = get_language()  # تأكد من استخدام get_language لضمان التوافق مع اللغات

    testimonials = Testimonial.objects.all().order_by('-created_at')[:12]
    total_reviews = testimonials.count()
    client_logos = ClientLogo.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST, lang=lang)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "تم إرسال رسالتك بنجاح." if lang == "ar" else "Your message was sent successfully."
            )
            return redirect('contact')  # تأكد أن اسم المسار مطابق لما هو في urls.py
    else:
        form = ContactForm(lang=lang)

    return render(request, 'public_site/contact.html', {
        'form': form,
        'testimonials': testimonials,
        'total_reviews': total_reviews,
        'client_logos': client_logos,
        'lang': lang
    })
