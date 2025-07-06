from public_site.models import SiteContent

data = [
    # ===== HEADER SECTION =====
    {"section": "header", "type": "image", "key": "header_logo", "content_en": "img/footer-bg.jpg", "content_ar": "img/footer-bg.jpg"},
    {"section": "header", "type": "image", "key": "ar_lang_icon", "content_en": "img/footer-bg.jpg", "content_ar": "img/footer-bg.jpg"},
    {"section": "header", "type": "image", "key": "en_lang_icon", "content_en": "img/footer-bg.jpg", "content_ar": "img/footer-bg.jpg"},

    # ===== HERO SECTION =====
    {"section": "hero", "type": "title", "key": "hero_main_title", "content_en": "Not just a stream – it’s an experience. Join the journey!", "content_ar": "ليست مجرد بث – إنها تجربة. انضم إلينا!"},
    {"section": "hero", "type": "p", "key": "hero_description", "content_en": "Playing electronic games, whether through consoles, computers, mobile phones or another medium altogether. Gaming is a nuanced term that suggests regular gameplay, possibly as a hobby.", "content_ar": "لعب الألعاب الإلكترونية سواء عبر أجهزة التحكم أو الحواسيب أو الهواتف أو غيرها. الألعاب مفهوم واسع يوحي بلعب منتظم كهواية."},
    {"section": "hero", "type": "button", "key": "hero_cta_button", "content_en": "Get Started Now", "content_ar": "ابدأ الآن"},
    {"section": "hero", "type": "p", "key": "hero_stat_1", "content_en": "300+ Unique Style", "content_ar": "300+ تصميم فريد"},
    {"section": "hero", "type": "p", "key": "hero_stat_2", "content_en": "200+ Project Finished", "content_ar": "200+ مشروع مكتمل"},
    {"section": "hero", "type": "p", "key": "hero_stat_3", "content_en": "500+ Happy Customer", "content_ar": "500+ عميل سعيد"},
    {"section": "hero", "type": "image", "key": "hero_background", "content_en": "img/hero-bg-1.png", "content_ar": "img/hero-bg-1.png"},

    # ===== ABOUT SECTION =====
    {"section": "about", "type": "subtitle", "key": "about_subtitle", "content_en": "About", "content_ar": "من نحن"},
    {"section": "about", "type": "title", "key": "about_main_title", "content_en": "Get to know us well", "content_ar": "تعرّف علينا أكثر"},
    {"section": "about", "type": "title", "key": "about_intro_title", "content_en": "Introduction", "content_ar": "مقدمة"},
    {"section": "about", "type": "p", "key": "about_intro_p", "content_en": "Welcome to the official hub of all things streaming! ...", "content_ar": "مرحبًا بك في المركز الرسمي لكل ما يخص البث المباشر! ..."},
    {"section": "about", "type": "title", "key": "about_contact_title", "content_en": "Contact Information", "content_ar": "معلومات الاتصال"},
    {"section": "about", "type": "p", "key": "about_contact_email", "content_en": "Email: damienbraun@gmail.com", "content_ar": "البريد الإلكتروني: damienbraun@gmail.com"},
    {"section": "about", "type": "p", "key": "about_contact_phone", "content_en": "Phone: +00 000000000", "content_ar": "الهاتف: +00 000000000"},
    {"section": "about", "type": "button", "key": "about_cta_button", "content_en": "Let's Work", "content_ar": "فلنبدأ العمل"},
    {"section": "about", "type": "image", "key": "about_image", "content_en": "img/about-image.png", "content_ar": "img/about-image.png"},
    {"section": "about", "type": "image", "key": "about_hero_background", "content_en": "img/Hero-2.png", "content_ar": "img/Hero-2.png"},
    {"section": "about", "type": "paragraph", "key": "about_scroll_hint", "content_en": "SCROLL DOWN TO SEE\nMY JOURNEY", "content_ar": "مرر لأسفل لتكتشف رحلتنا"},

    # ===== ABOUT STATS =====
    {"section": "about", "type": "p", "key": "about_stats_years", "content_en": "15+", "content_ar": "15+"},
    {"section": "about", "type": "subtitle", "key": "about_stats_years_label", "content_en": "Years in Business", "content_ar": "سنوات من العمل"},
    {"section": "about", "type": "p", "key": "about_stats_clients", "content_en": "500+", "content_ar": "500+"},
    {"section": "about", "type": "subtitle", "key": "about_stats_clients_label", "content_en": "Happy Clients", "content_ar": "عملاء سعداء"},
    {"section": "about", "type": "p", "key": "about_stats_awards", "content_en": "10+", "content_ar": "10+"},
    {"section": "about", "type": "subtitle", "key": "about_stats_awards_label", "content_en": "Photography Awards", "content_ar": "جوائز تصوير"},
    {"section": "about", "type": "p", "key": "about_stats_international", "content_en": "05+", "content_ar": "05+"},
    {"section": "about", "type": "subtitle", "key": "about_stats_international_label", "content_en": "International Shoots", "content_ar": "جلسات دولية"},
    {"section": "about", "type": "p", "key": "about_stats_followers", "content_en": "10,000+", "content_ar": "10,000+"},
    {"section": "about", "type": "subtitle", "key": "about_stats_followers_label", "content_en": "Social Media Followers", "content_ar": "متابعين على المنصات"},
    {"section": "about", "type": "p", "key": "about_stats_retention", "content_en": "90%", "content_ar": "90%"},
    {"section": "about", "type": "subtitle", "key": "about_stats_retention_label", "content_en": "Client Retention Rate", "content_ar": "معدل رضا العملاء"},

    # ===== VIDEO SECTION =====
    {"section": "video", "type": "title", "key": "video_title", "content_en": "Level up your world — where streaming meets technology", "content_ar": "ارتقِ بعالمك — حيث يلتقي البث بالتقنية"},
    {"section": "video", "type": "video", "key": "video_thumbnail", "content_en": "img/video-thumbnail.png", "content_ar": "img/video-thumbnail.png"},

    # ===== FEATURES SECTION =====
    {"section": "features", "type": "title", "key": "features_main_title", "content_en": "CHECK OUT OUR MOST IMPORTANT FEATURES", "content_ar": "اطلع على أهم ميزاتنا"},
    {"section": "features", "type": "p", "key": "features_main_subtitle", "content_en": "Offer sneak peeks and previews of upcoming games, including trailers, screenshots, and information about release.", "content_ar": "تقديم لمحات وعروض لألعاب قادمة، بما في ذلك الإعلانات والمقاطع والمعلومات الخاصة بالإصدار."},

    # ===== PROJECTS SECTION =====
    {"section": "projects", "type": "subtitle", "key": "projects_subtitle", "content_en": "Projects", "content_ar": "المشاريع"},
    {"section": "projects", "type": "title", "key": "projects_main_title", "content_en": "Explore Our work.", "content_ar": "استكشف أعمالنا"},
    {"section": "projects", "type": "button", "key": "projects_cta_button", "content_en": "View All Works", "content_ar": "عرض جميع الأعمال"},

    # ===== CLIENTS SECTION =====
    {"section": "clients", "type": "title", "key": "clients_main_title", "content_en": "We have served more than 150,000 clients. and some of our clients are:", "content_ar": "لقد خدمنا أكثر من 150,000 عميل. ومن بين عملائنا:"},
    {"section": "clients", "type": "p", "key": "clients_description", "content_en": "We have been honored to serve a large number of clients...", "content_ar": "تشرفنا بخدمة عدد كبير من العملاء..."},

    # ===== GAMES SECTION =====
    {"section": "games", "type": "title", "key": "games_title", "content_en": "CHOOSE YOUR FAVORITE GAMES", "content_ar": "اختر ألعابك المفضلة"},
    {"section": "games", "type": "p", "key": "games_subtitle", "content_en": "Offer sneak peeks and previews of upcoming games...", "content_ar": "تقديم لمحات وعروض لألعاب قادمة..."},

    # ===== FAQ SECTION =====
    {"section": "faq", "type": "subtitle", "key": "faq_subtitle", "content_en": "FAQ's", "content_ar": "الأسئلة الشائعة"},
    {"section": "faq", "type": "title", "key": "faq_title", "content_en": "Frequently Asked Questions", "content_ar": "الأسئلة المتكررة"},

    # ===== TESTIMONIALS SECTION =====
    {"section": "testimonials", "type": "subtitle", "key": "testimonials_subtitle", "content_en": "Testimonials", "content_ar": "آراء العملاء"},
    {"section": "testimonials", "type": "title", "key": "testimonials_title", "content_en": "What Our Clients Say", "content_ar": "ماذا يقول عملاؤنا؟"},
    {"section": "testimonials", "type": "subtitle", "key": "testimonials_total_reviews_label", "content_en": "Total Reviews", "content_ar": "إجمالي التقييمات"},
    {"section": "testimonials", "type": "title", "key": "testimonials_total_reviews_value", "content_en": "323", "content_ar": "٣٢٣"},
    {"section": "testimonials", "type": "button", "key": "testimonials_view_all", "content_en": "View All Testimonials", "content_ar": "عرض جميع الآراء"},
    {"section": "testimonials", "type": "link", "key": "testimonials_view_all_link", "content_en": "#", "content_ar": "#"},

    # ===== SOCIAL LINKS =====
    {"section": "about", "type": "link", "key": "social_facebook", "content_en": "https://facebook.com", "content_ar": "https://facebook.com"},
    {"section": "about", "type": "link", "key": "social_youtube", "content_en": "https://youtube.com", "content_ar": "https://youtube.com"},
    {"section": "about", "type": "link", "key": "social_tiktok", "content_en": "https://tiktok.com", "content_ar": "https://tiktok.com"},

    # ===== FOOTER SECTION =====
    {"section": "footer", "type": "image", "key": "footer_background", "content_en": "img/footer-bg.jpg", "content_ar": "img/footer-bg.jpg"},
]

# python manage.py shell < public_site/load_site_content.py
# exec(open('public_site/load_site_content.py', encoding='utf-8').read())
# إدخال أو تحديث العناصر
# for item in data:
#     SiteContent.objects.update_or_create(
#         key=item["key"],
#         defaults=item
#     )

# print("✅ All static content inserted/updated successfully.")
# from public_site.models import SiteContent

data = [
    {
        "section": "about",
        "type": "button",
        "key": "about_main_cta_button",
        "content_en": "Know More",
        "content_ar": "اعرف المزيد"
    },
    {
        "section": "video",
        "type": "title",
        "key": "video_main_heading",
        "content_en": "Level up your world — where streaming meets technology",
        "content_ar": "ارتقِ بعالمك — حيث يلتقي البث بالتقنية"
    },
    {
        "section": "clients",
        "type": "p",
        "key": "clients_secondary_description",
        "content_en": "We have been honored to serve a large number of clients in all areas of our services since 2006 and for more than 14 years and we are still continuing",
        "content_ar": "تشرفنا بخدمة عدد كبير من العملاء في جميع مجالات خدماتنا منذ عام 2006 ولمدة تزيد عن 14 سنة وما زلنا مستمرين."
    },
    {
        "section": "hero",
        "type": "paragraph",
        "key": "hero_marquee_1",
        "content_en": "GAMING SPANING",
        "content_ar": "عالم الألعاب"
    },
    {
        "section": "hero",
        "type": "paragraph",
        "key": "hero_marquee_2",
        "content_en": "ACTION - PACKED",
        "content_ar": "أكشن وتشويق"
    },
    {
        "section": "hero",
        "type": "paragraph",
        "key": "hero_marquee_3",
        "content_en": "MIND - BENDING",
        "content_ar": "مغامرات لا تُنسى"
    },
    {
        "section": "hero",
        "type": "paragraph",
        "key": "hero_marquee_4",
        "content_en": "COLLECTION OF GAMES",
        "content_ar": "مجموعة ألعاب مذهلة"
    },
]

data = [
  {"section": "contact", "key": "contact_hero_title", "type": "title", "content_ar": "ابق على اتصال بنا", "content_en": "Get in Touch with Us"},
  {"section": "contact", "key": "contact_hero_subtitle", "type": "subtitle", "content_ar": "تواصل معنا", "content_en": "Contact Me"},
  {"section": "contact", "key": "contact_hero_paragraph", "type": "paragraph", "content_ar": ".", "content_en": "Step into a world of timeless photography with Damien Braun. Explore our range of photography services, each crafted to tell your unique story through captivating images."},
  {"section": "contact", "key": "contact_scroll_hint", "type": "paragraph", "content_ar": "مرر للأسفل لإرسال رسالة", "content_en": "Scroll down to send me a message"},
  {"section": "contact", "key": "contact_info_title", "type": "title", "content_ar": "معلومات الاتصال", "content_en": "Contact Information"},
  {"section": "contact", "key": "contact_info_paragraph", "type": "paragraph", "content_ar": ".", "content_en": "Feel free to reach out to us through various channels."},
  {"section": "contact", "key": "contact_form_title", "type": "title", "content_ar": "أرسل رسالة", "content_en": "Send Me A Message"},
  {"section": "contact", "key": "contact_form_paragraph", "type": "paragraph", "content_ar": "", "content_en": "Have a specific inquiry? Use the form below and we'll get back to you promptly."},
  {"section": "contact", "key": "contact_form_submit", "type": "button", "content_ar": "إرسال الرسالة", "content_en": "SEND MESSAGE"},
]

for item in data:
    SiteContent.objects.update_or_create(
        key=item["key"],
        defaults=item
    )

print("✅ Missing static content inserted/updated successfully.")
