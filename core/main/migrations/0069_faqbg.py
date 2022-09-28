# Generated by Django 4.1.1 on 2022-09-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0068_testimonialquote_alter_testimonialquotetitle_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqBG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, max_length=50, verbose_name='FaqBG name1')),
                ('name2', models.CharField(max_length=50, verbose_name='FaqBG name2')),
                ('img', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='FaqBG image')),
            ],
            options={
                'verbose_name': 'FaqBG',
                'verbose_name_plural': 'FaqBGs',
            },
        ),
    ]
