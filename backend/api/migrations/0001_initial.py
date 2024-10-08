# Generated by Django 3.2.3 on 2024-09-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.FloatField(verbose_name='Цена')),
            ],
        ),
    ]
