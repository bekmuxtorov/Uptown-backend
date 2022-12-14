# Generated by Django 4.0.6 on 2022-10-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agents',
            options={'verbose_name': 'Ishchi', 'verbose_name_plural': 'Ishchilar'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Xabar', 'verbose_name_plural': 'Xabarlar'},
        ),
        migrations.AlterModelOptions(
            name='happyclients',
            options={'verbose_name': 'Buyurtmachi', 'verbose_name_plural': 'Buyurtmachilar'},
        ),
        migrations.AlterModelOptions(
            name='offerworks',
            options={'verbose_name': 'Topshirilgan ish', 'verbose_name_plural': 'Topshirilgan ishlar'},
        ),
        migrations.AlterModelOptions(
            name='resentblog',
            options={'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, help_text='Email:', max_length=254, verbose_name='Email:'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(blank=True, help_text='Xabar:', verbose_name='Xabar:'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(blank=True, help_text='Ism:', max_length=100, verbose_name='Ism:'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, help_text='Mavzu:', max_length=200, verbose_name='Mavzu:'),
        ),
    ]
