# Generated by Django 5.1.7 on 2025-03-27 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_method_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Главный текст')),
                ('description', models.TextField(max_length=10000, verbose_name='Длинный текст')),
            ],
        ),
    ]
