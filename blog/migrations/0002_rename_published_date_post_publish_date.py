# Generated by Django 3.2.7 on 2021-09-23 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='publish_date',
        ),
    ]
