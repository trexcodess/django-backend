# Generated by Django 4.1.5 on 2023-01-24 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='interest',
            field=models.CharField(choices=[('Kids Coding (5-12)', 'KIDS_CODING'), ('Adult Coding ( 13+ )', 'ADULT_CODING'), ('Search Engine Optimization', 'SEO'), ('Server Administration', 'SERVER_ADMIN')], max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='learning_path',
            field=models.CharField(choices=[('Self Help Route', 'SELF_HELP'), ('Classroom Learning', 'CLASSROOM')], max_length=50),
        ),
    ]