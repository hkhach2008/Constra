# Generated by Django 4.1.1 on 2022-09-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_testimonialtitle_remove_testimonial_name1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonialtitle',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Testimonials name1'),
        ),
    ]