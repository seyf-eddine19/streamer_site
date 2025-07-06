from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import get_language
from .models import (
    SiteContent, TeamMember, Service, Project, ProjectCategory,
    Game, FAQ, Testimonial, ClientLogo
)
from .forms import ContactForm


# ===== Utility to Fetch Content by Section / Type / Key =====
def get_site_content(sections=None, keys=None, type=None, lang='en'):
    queryset = SiteContent.objects.all()

    if sections:
        queryset = queryset.filter(section__in=sections)
    if keys:
        queryset = queryset.filter(key__in=keys)
    if type:
        queryset = queryset.filter(type=type)

    result = {}
    for item in queryset:
        content = item.content_ar if lang == 'ar' else item.content_en
        result.setdefault(item.section, []).append({
            'key': item.key,
            'type': item.type,
            'content': content
        })

    return result

def ensure_minimum_items(queryset, minimum=12):
    items = list(queryset)
    if not items:
        return []

    while len(items) < minimum:
        items += items[:min(minimum - len(items), len(items))]

    return items

# ======= HOME PAGE =======
def home_view(request):
    lang = get_language()
    
    context = {
        'site_content': get_site_content(
            sections=['hero', 'games', 'about', 'video', 'services', 'projects', 'clients', 'testimonials', 'faq'],
            lang=lang
        ),
        'team_members': TeamMember.objects.all(),
        'services': Service.objects.all(),
        'projects': ensure_minimum_items(Project.objects.all(), minimum=12),
        'games': ensure_minimum_items(Game.objects.all(), minimum=12),
        'faqs': FAQ.objects.all(),
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'client_logos': ClientLogo.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/index.html', context)


# ======= ABOUT PAGE =======
def about_view(request):
    lang = get_language()

    context = {
        'site_content': get_site_content(sections=['about', 'clients', 'testimonials'], lang=lang),
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'client_logos': ClientLogo.objects.all(),
        'lang': lang
    }
    return render(request, 'public_site/about.html', context)


# ======= PROJECTS PAGE =======
def projects_view(request):
    lang = get_language()

    categories = ProjectCategory.objects.all()
    projects_by_category = {
        category: Project.objects.filter(categories=category)
        for category in categories
    }

    context = {
        'site_content': get_site_content(sections=['projects', 'clients', 'faq', 'testimonials'], lang=lang),
        'categories': categories,
        'projects_by_category': projects_by_category,
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'faqs': FAQ.objects.all(),
        'client_logos': ClientLogo.objects.all(),
        'lang': lang
    }
    return render(request, 'public_site/projects.html', context)


# ======= CONTACT PAGE =======
def contact_view(request):
    lang = get_language()

    if request.method == 'POST':
        form = ContactForm(request.POST, lang=lang)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "تم إرسال رسالتك بنجاح." if lang == "ar" else "Your message was sent successfully."
            )
            return redirect('contact')
    else:
        form = ContactForm(lang=lang)

    context = {
        'form': form,
        'site_content': get_site_content(sections=['contact', 'testimonials'], lang=lang),
        'about_contact': get_site_content(keys=['about_contact_phone', 'about_contact_email'], lang=lang),
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'client_logos': ClientLogo.objects.all(),
        'lang': lang
    }
    return render(request, 'public_site/contact.html', context)
