# Generated by Django 4.1.1 on 2022-09-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0054_alter_aboutbg_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutbg',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='AboutBG image'),
        ),
    ]
