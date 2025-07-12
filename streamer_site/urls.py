from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from team_dashboard.admin import create_superuser_view

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),           # ✅ هذا هو المطلوب لتفعيل set_language
    path('create-superuser/', create_superuser_view, name='create_superuser'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('team_dashboard.urls')),        # مسار الفريق
    path('', include('public_site.urls')),                     # صفحات الموقع
]

# دعم ملفات الميديا
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# معالجات الأخطاء
handler403 = 'team_dashboard.views.custom_403'
handler404 = 'team_dashboard.views.custom_404'
handler500 = 'team_dashboard.views.custom_500'

