# Generated by Django 3.1.2 on 2021-05-13 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('blog', '0003_auto_20210428_2033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Publication',
            new_name='Blog',
        ),
    ]
