# Generated by Django 3.1.2 on 2021-04-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210428_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='publication',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
