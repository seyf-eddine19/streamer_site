# Generated by Django 3.2.25 on 2025-07-04 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='اسم المشروع')),
                ('description', models.TextField(blank=True, null=True, verbose_name='وصف المشروع')),
                ('status', models.CharField(choices=[('لم يبدأ بعد', 'لم يبدأ بعد'), ('قيد التنفيذ', 'قيد التنفيذ'), ('مكتمل', 'مكتمل'), ('معلق', 'معلق')], default='لم يبدأ بعد', max_length=20, verbose_name='حالة المشروع')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='منشئ المشروع')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='تاريخ الإنشاء')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsapp_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='WhatsApp Number')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(choices=[('اختيار الموضوع', 'اختيار الموضوع'), ('كتابة المحتوى', 'كتابة المحتوى'), ('التسجيل', 'التسجيل'), ('المونتاج', 'المونتاج'), ('الثامنايل', 'الثامنايل'), ('الرفع', 'الرفع')], max_length=50)),
                ('status', models.CharField(choices=[('لم يبدأ بعد', 'لم يبدأ بعد'), ('قيد التنفيذ', 'قيد التنفيذ'), ('مكتمل', 'مكتمل'), ('معلق', 'معلق')], default='قيد التنفيذ', max_length=20)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('assigned_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='team_dashboard.project')),
            ],
        ),
    ]
