# Generated by Django 4.1.1 on 2022-09-28 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0067_testimonialquotetitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50, verbose_name='TestimonialQuote name1')),
                ('name2', models.CharField(max_length=75, verbose_name='TestimonialQuote name2')),
                ('about', models.TextField(verbose_name='TestimonialQuote about')),
                ('img', models.ImageField(upload_to='media', verbose_name='TestimonialQuote image')),
            ],
            options={
                'verbose_name': 'TestimonialQuote',
                'verbose_name_plural': 'TestimonialQuotes',
            },
        ),
        migrations.AlterModelOptions(
            name='testimonialquotetitle',
            options={'verbose_name': 'TestimonialQuoteTitle', 'verbose_name_plural': 'TestimonialQuoteTitles'},
        ),
    ]
