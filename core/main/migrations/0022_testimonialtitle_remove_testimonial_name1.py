# Generated by Django 4.1.1 on 2022-09-24 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='Testimonials name1')),
            ],
            options={
                'verbose_name': 'TestimonialTitle',
                'verbose_name_plural': 'TestimonialTitles',
            },
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='name1',
        ),
    ]
