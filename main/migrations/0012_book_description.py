# Generated by Django 4.1.5 on 2023-02-23 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_review_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default=1, verbose_name='Опис'),
            preserve_default=False,
        ),
    ]
