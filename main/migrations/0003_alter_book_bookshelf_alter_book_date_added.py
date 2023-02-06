# Generated by Django 4.1.5 on 2023-02-01 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_book_options_alter_bookshelf_options_book_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookshelf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.bookshelf'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]