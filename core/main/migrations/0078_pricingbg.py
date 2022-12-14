# Generated by Django 4.1.1 on 2022-09-29 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0077_faqpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricingBG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(blank=True, max_length=50, verbose_name='PricingBG name1')),
                ('name2', models.CharField(max_length=50, verbose_name='PricingBG name2')),
                ('img', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='PricingBG image')),
            ],
            options={
                'verbose_name': 'PricingBG',
                'verbose_name_plural': 'PricingBGs',
            },
        ),
    ]
