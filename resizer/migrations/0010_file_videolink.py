# Generated by Django 4.0.4 on 2022-05-24 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resizer', '0009_alter_image_options_image_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='videolink',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
