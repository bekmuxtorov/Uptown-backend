# Generated by Django 4.0.6 on 2022-11-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_user_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=' ', max_length=30, null=True, verbose_name='Foydalanuvchi familiyasi:'),
        ),
    ]
