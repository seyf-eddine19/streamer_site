from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.utils.translation import get_language
from .models import (
    SiteContent, SiteImage, TeamMember, Service, Project, ProjectCategory,
    Game, FAQ, Testimonial, ClientLogo, BlogPost
)
from .forms import ContactForm


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


def get_site_images(keys=None):
    queryset = SiteImage.objects.all()
    if keys:
        queryset = queryset.filter(key__in=keys)
    images = {img.key: img.image.url for img in queryset}
    return images


def ensure_minimum_items(queryset, minimum=12):
    items = list(queryset)
    if not items:
        return []
    while len(items) < minimum:
        items += items[:min(minimum - len(items), len(items))]
    return items


def home_view(request):
    lang = get_language()
    images = get_site_images(['hero_bg_1', 'logo', 'about_img', 'ar_img', 'en_img', 'footer_bg'])
    hero_taglines = SiteContent.objects.filter(
        section='hero',
        key__startswith='hero_tagline_'
    ).order_by('key')
    hero_taglines = list(hero_taglines)
    if len(hero_taglines) < 8:
        multiplier = (8 // len(hero_taglines)) + 1
        hero_taglines *= multiplier

    context = {
        'site_content': get_site_content(
            sections=['hero', 'games', 'about', 'video', 'services', 'projects', 'clients', 'testimonials', 'faq'],
            lang=lang
        ),
        'site_images': images,
        'hero_taglines': hero_taglines,
        'team_members': TeamMember.objects.all(),
        'services': Service.objects.all(),
        'projects': ensure_minimum_items(Project.objects.all()),
        'games': ensure_minimum_items(Game.objects.all()),
        'faqs': FAQ.objects.all(),
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'client_logos': ClientLogo.objects.all(),
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), minimum=15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/index.html', context)


def about_view(request):
    lang = get_language()
    images = get_site_images(['hero_bg_2', 'about_img', 'logo', 'ar_img', 'en_img', 'footer_bg'])
    context = {
        'site_content': get_site_content(sections=['about', 'team', 'clients', 'testimonials'], lang=lang),
        'site_images': images,
        'team_members': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'client_logos': ClientLogo.objects.all(),
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), minimum=15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/about.html', context)


def projects_view(request):
    lang = get_language()
    images = get_site_images(['hero_bg_3', 'logo', 'ar_img', 'en_img', 'footer_bg'])
    categories = ProjectCategory.objects.all()
    projects_by_category = {category: Project.objects.filter(categories=category) for category in categories}
    context = {
        'site_content': get_site_content(sections=['projects', 'clients', 'faq', 'testimonials'], lang=lang),
        'site_images': images,
        'categories': categories,
        'projects_by_category': projects_by_category,
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'faqs': FAQ.objects.all(),
        'client_logos': ClientLogo.objects.all(),
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), minimum=15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'lang': lang,
    }
    return render(request, 'public_site/projects.html', context)


def category_view(request, category_id):
    lang = request.LANGUAGE_CODE
    images = get_site_images(['logo', 'ar_img', 'en_img', 'footer_bg'])
    category_obj = get_object_or_404(ProjectCategory, id=category_id)
    projects = Project.objects.filter(categories=category_obj)
    context = {
        'site_content': get_site_content(sections=['projects'], lang=lang),
        'site_images': images,
        'projects': projects,
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), minimum=15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'current_category': category_obj,
        'lang': lang,
    }
    return render(request, 'public_site/projects_by_category.html', context)


def contact_view(request):
    lang = get_language()
    images = get_site_images(['hero_bg_4', 'logo', 'ar_img', 'en_img', 'footer_bg'])
    if request.method == 'POST':
        form = ContactForm(request.POST, lang=lang)
        if form.is_valid():
            form.save()
            messages.success(request, "تم إرسال رسالتك بنجاح." if lang == "ar" else "Your message was sent successfully.")
            return redirect('contact')
    else:
        form = ContactForm(lang=lang)
    context = {
        'form': form,
        'site_content': get_site_content(sections=['contact', 'testimonials'], lang=lang),
        'about_contact': get_site_content(keys=['about_contact_phone', 'about_contact_email'], lang=lang),
        'site_images': images,
        'testimonials': Testimonial.objects.all().order_by('-created_at')[:12],
        'total_reviews': Testimonial.objects.count(),
        'client_logos': ClientLogo.objects.all(),
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), minimum=15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/contact.html', context)


def testimonials_view(request):
    lang = get_language()
    images = get_site_images(['logo', 'ar_img', 'en_img', 'footer_bg'])
    context = {
        'site_content': get_site_content(sections=['testimonials'], lang=lang),
        'site_images': images,
        'testimonials': Testimonial.objects.all().order_by('-created_at'),
        'total_reviews': Testimonial.objects.count(),
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), minimum=15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/testimonials.html', context)


def privacy_policy_view(request):
    lang = get_language()
    images = get_site_images(['logo', 'ar_img', 'en_img', 'footer_bg'])
    policy_content = get_object_or_404(SiteContent, key='privacy_policy_content')

    context = {
        'privacy_policy': policy_content,
        'site_images': images,
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), 15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/privacy_policy.html', context)


def terms_and_conditions_view(request):
    lang = get_language()
    images = get_site_images(['logo', 'ar_img', 'en_img', 'footer_bg'])

    context = {
        'terms_and_conditions': terms_content,
        'site_images': images,
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), 15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/terms_and_conditions.html', context)


def blog_list_view(request):
    lang = get_language()
    images = get_site_images(['hero_bg_5', 'logo', 'ar_img', 'en_img', 'footer_bg'])
    posts = BlogPost.objects.order_by('-created_at')

    # meta_title = "مدونة ستريمر" if lang == "ar" else "streamer Blog"
    # meta_description = "تابع أحدث المقالات والأخبار." if lang == "ar" else "Read our latest articles and updates."

    context = {
        'posts': posts,
        'site_images': images,
        'site_content': get_site_content(sections=['blog'], lang=lang),
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), 15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/blog/blog_list.html', context)


def blog_detail_view(request, post_id):
    lang = get_language()
    images = get_site_images(['logo', 'ar_img', 'en_img', 'footer_bg'])
    post = get_object_or_404(BlogPost, id=post_id)

    # meta_title = post.title_ar if lang == "ar" else post.title_en
    # meta_description = post.summary_ar[:160] if lang == "ar" else post.summary_en[:160]
    meta_image = post.image.url if post.image else ''
    posts = BlogPost.objects.order_by('-created_at')[:15]

    context = {
        'post': post,
        'posts': posts,
        'site_images': images,
        'meta_image': meta_image,
        'footer_categories': ensure_minimum_items(ProjectCategory.objects.all(), 15),
        'about_links': get_list_or_404(SiteContent, section='about', type='link'),
        'categories': ProjectCategory.objects.all(),
        'lang': lang,
    }
    return render(request, 'public_site/blog/blog_detail.html', context)
