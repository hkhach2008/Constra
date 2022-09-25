# Generated by Django 4.1.1 on 2022-09-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0062_teambg'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='TeamTeam title')),
                ('name1', models.CharField(max_length=50, verbose_name='AboutTeam name1')),
                ('name2', models.CharField(max_length=50, verbose_name='AboutTeam name2')),
                ('about', models.TextField(verbose_name='AboutTeam about')),
                ('img', models.ImageField(upload_to='media', verbose_name='AboutTeam image')),
            ],
            options={
                'verbose_name': 'TeamTeam',
                'verbose_name_plural': 'TeamTeams',
            },
        ),
    ]