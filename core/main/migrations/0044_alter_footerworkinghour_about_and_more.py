# Generated by Django 4.1.1 on 2022-09-24 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_footerworkinghour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerworkinghour',
            name='about',
            field=models.TextField(blank=True, verbose_name='FooterWorkingHour about'),
        ),
        migrations.AlterField(
            model_name='footerworkinghour',
            name='name',
            field=models.CharField(blank=True, max_length=50, verbose_name='FooterWorkingHour name'),
        ),
    ]
