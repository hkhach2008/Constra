# Generated by Django 4.1.1 on 2022-09-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_alter_aboutbg_name1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutbg',
            name='img',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='AboutBG image'),
        ),
    ]
