# Generated by Django 4.1.1 on 2022-09-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_headerlogo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=50, verbose_name='Contact name')),
                ('name2', models.CharField(max_length=75, verbose_name='Contact name2')),
                ('name3', models.CharField(blank=True, max_length=50, verbose_name='Contact name3')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
