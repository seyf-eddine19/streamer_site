# load_faqs.py

from public_site.models import FAQ

faq_data = [
    {
        "question_en": "WHEN DO YOU USUALLY STREAM",
        "question_ar": "متى تقوم عادةً بالبث المباشر؟",
        "answer_en": "I follow a weekly streaming schedule, and you can always find the latest updates in the “Stream Schedule” section.",
        "answer_ar": "أتبع جدول بث أسبوعي، ويمكنك دائماً متابعة آخر التحديثات في قسم \"جدول البث\"."
    },
    {
        "question_en": "WHAT SETUP DO YOU USE FOR STREAMING?",
        "question_ar": "ما هو الإعداد الذي تستخدمه للبث؟",
        "answer_en": "We use a custom-built PC, Elgato capture card, OBS Studio, and a Shure microphone.",
        "answer_ar": "نستخدم حاسوباً مخصصاً، وبطاقة التقاط Elgato، وبرنامج OBS Studio، وميكروفون Shure."
    },
    {
        "question_en": "WHAT GAMES DO YOU PLAY ON STREAM?",
        "question_ar": "ما الألعاب التي تلعبها أثناء البث؟",
        "answer_en": "Mostly FPS, adventure, and indie games — we love trying out new releases and classics!",
        "answer_ar": "في الغالب ألعاب تصويب ومغامرات وألعاب مستقلة — نحب تجربة الألعاب الجديدة والكلاسيكية!"
    },
    {
        "question_en": "DO YOU UPLOAD STREAM HIGHLIGHTS OR CLIPS?",
        "question_ar": "هل تقوم برفع لقطات أو أبرز لحظات البث؟",
        "answer_en": "Yes! We share highlights and best moments regularly on our YouTube and TikTok.",
        "answer_ar": "نعم! نشارك أبرز اللحظات واللقطات بشكل منتظم على يوتيوب وتيك توك."
    },
    {
        "question_en": "WHERE CAN I WATCH YOUR LIVE STREAMS?",
        "question_ar": "أين يمكنني مشاهدة البث المباشر؟",
        "answer_en": "You can catch us on Twitch and YouTube every week — follow us to stay notified.",
        "answer_ar": "يمكنك متابعتنا على تويتش ويوتيوب كل أسبوع — تابعنا لتصلك التنبيهات."
    },
    {
        "question_en": "HOW CAN I SUPPORT YOUR CONTENT?",
        "question_ar": "كيف يمكنني دعم المحتوى الخاص بك؟",
        "answer_en": "Watching, liking, sharing, subscribing, or joining memberships — every bit of support helps!",
        "answer_ar": "المشاهدة، الإعجاب، المشاركة، الاشتراك، أو الانضمام كعضو — كل دعم له أثر كبير!"
    },
    {
        "question_en": "CAN I JOIN YOUR GAMES OR PLAY WITH YOU?",
        "question_ar": "هل يمكنني الانضمام إلى ألعابك أو اللعب معك؟",
        "answer_en": "Absolutely! We host community sessions where viewers can join in. Stay tuned!",
        "answer_ar": "بالتأكيد! ننظم جلسات مجتمعية يمكن للمشاهدين الانضمام إليها. ترقبها!"
    },
    {
        "question_en": "HOW CAN I CONTACT YOU OR SEND FEEDBACK?",
        "question_ar": "كيف يمكنني التواصل معك أو إرسال ملاحظات؟",
        "answer_en": "You can reach us via email or our Discord channel. We’d love to hear from you.",
        "answer_ar": "يمكنك التواصل معنا عبر البريد الإلكتروني أو قناة Discord. يسعدنا الاستماع إليك."
    },
]

for data in faq_data:
    obj, created = FAQ.objects.get_or_create(
        question_en=data["question_en"],
        defaults={
            "question_ar": data["question_ar"],
            "answer_en": data["answer_en"],
            "answer_ar": data["answer_ar"]
        }
    )
    if created:
        print(f"✅ Added: {data['question_en']}")
    else:
        print(f"⚠️ Already exists: {data['question_en']}")
