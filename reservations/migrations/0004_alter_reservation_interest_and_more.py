# Generated by Django 4.1.5 on 2023-01-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_alter_reservation_interest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='interest',
            field=models.CharField(choices=[('seo_training', 'SEO'), ('kids_coding', 'Kids Coding (5-12yrs)'), ('adult_coding', 'Adult Coding (13+yrs)'), ('server_admin', 'Learn Server Administration')], max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='learning_path',
            field=models.CharField(choices=[('self_help', 'Self Help Route'), ('classroom_env', 'Online Classroom')], max_length=50),
        ),
    ]
