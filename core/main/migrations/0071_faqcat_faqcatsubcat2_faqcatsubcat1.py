# Generated by Django 4.1.1 on 2022-09-28 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0070_faqcattitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=175, verbose_name='FaqCat name')),
            ],
            options={
                'verbose_name': 'FaqCat',
                'verbose_name_plural': 'FaqCats',
            },
        ),
        migrations.CreateModel(
            name='FaqCatSubcat2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='FaqCatSubcat1')),
                ('faqcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcat2', to='main.faqcat')),
            ],
            options={
                'verbose_name': 'FaqCatSubcat2',
                'verbose_name_plural': 'FaqCatSubcats2',
            },
        ),
        migrations.CreateModel(
            name='FaqCatSubcat1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='FaqCatSubcat1')),
                ('faqcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcat1', to='main.faqcat')),
            ],
            options={
                'verbose_name': 'FaqCatSubcat1',
                'verbose_name_plural': 'FaqCatSubcats1',
            },
        ),
    ]