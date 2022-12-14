# Generated by Django 4.1.1 on 2022-09-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_homecarusel_img1_remove_homecarusel_img2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeCarusel1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=120, null=True, verbose_name='Carusel1 name 1')),
                ('name2', models.CharField(max_length=120, null=True, verbose_name='Carusel1 name 2')),
                ('img', models.ImageField(null=True, upload_to='media', verbose_name='Carusel1 image')),
            ],
            options={
                'verbose_name': 'HomeCarusel1',
                'verbose_name_plural': 'HomeCarusels1',
            },
        ),
        migrations.CreateModel(
            name='HomeCarusel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=120, null=True, verbose_name='Carusel2 name 1')),
                ('name2', models.CharField(max_length=120, null=True, verbose_name='Carusel2 name 2')),
                ('name3', models.CharField(max_length=120, null=True, verbose_name='Carusel2 name 3')),
                ('img', models.ImageField(null=True, upload_to='media', verbose_name='Carusel2 image')),
            ],
            options={
                'verbose_name': 'HomeCarusel2',
                'verbose_name_plural': 'HomeCarusels2',
            },
        ),
        migrations.CreateModel(
            name='HomeCarusel3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=120, null=True, verbose_name='Carusel3 name 1')),
                ('name2', models.CharField(max_length=120, null=True, verbose_name='Carusel3 name 2')),
                ('name3', models.CharField(max_length=120, null=True, verbose_name='Carusel3 name 3')),
                ('img', models.ImageField(null=True, upload_to='media', verbose_name='Carusel3 image')),
            ],
            options={
                'verbose_name': 'HomeCarusel3',
                'verbose_name_plural': 'HomeCarusels3',
            },
        ),
        migrations.DeleteModel(
            name='HomeCarusel',
        ),
    ]
