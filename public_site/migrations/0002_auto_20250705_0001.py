# Generated by Django 3.2.25 on 2025-07-04 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=100, unique=True, verbose_name='Name (English)')),
                ('name_ar', models.CharField(max_length=100, unique=True, verbose_name='الاسم (عربي)')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='category',
        ),
        migrations.AlterField(
            model_name='clientlogo',
            name='logo',
            field=models.ImageField(upload_to='public_site/clients/'),
        ),
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(to='public_site.ProjectCategory', verbose_name='التصنيفات'),
        ),
    ]
