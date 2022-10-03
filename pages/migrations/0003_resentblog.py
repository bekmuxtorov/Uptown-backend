# Generated by Django 4.0.6 on 2022-09-29 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0002_happyclients'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_text', models.CharField(max_length=55, verbose_name="Qisqa ma'lumot: ")),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('long_text', models.CharField(max_length=200, verbose_name="Ko'proq ma'lumot: ")),
                ('blog_image', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]