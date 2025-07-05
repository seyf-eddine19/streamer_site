# public_site/load_testimonials.py

from public_site.models import Testimonial
from django.utils import timezone
import random

names = [
    "Emily Johnson", "John Smith", "Samantha Davis",
    "Liam Brown", "Olivia Garcia", "Noah Lee"
]

addresses = [
    "USA, California", "UK, London", "Canada, Toronto",
    "UAE, Dubai", "Germany, Berlin", "France, Paris"
]

comments_en = [
    "Amazing work! I loved the final result.",
    "Truly professional and creative!",
    "Exceptional service and beautiful photos.",
    "Highly recommended for any event.",
    "Captured every moment perfectly!",
    "Friendly and talented team!"
]

comments_ar = [
    "عمل رائع! أحببت النتيجة النهائية.",
    "محترف ومبدع بالفعل!",
    "خدمة استثنائية وصور جميلة.",
    "أنصح به بشدة لأي مناسبة.",
    "التقط كل اللحظات بدقة!",
    "فريق ودود وموهوب!"
]

social_links = [
    ("https://facebook.com/example", "https://twitter.com/example", "https://linkedin.com/in/example"),
    ("", "", ""),
    ("https://facebook.com/user1", "", "https://linkedin.com/in/user1"),
]

for i in range(12):
    name = random.choice(names)
    address = random.choice(addresses)
    content_en = random.choice(comments_en)
    content_ar = random.choice(comments_ar)
    rating = random.randint(3, 5)
    fb, tw, ln = random.choice(social_links)

    Testimonial.objects.create(
        name=name,
        address=address,
        content_en=content_en,
        content_ar=content_ar,
        rating=rating,
        facebook_url=fb,
        twitter_url=tw,
        linkedin_url=ln,
        created_at=timezone.now()
    )

print("✅ Dummy testimonials created successfully.")
