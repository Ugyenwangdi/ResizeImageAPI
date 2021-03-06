# Generated by Django 4.0.4 on 2022-05-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resizer', '0006_image_alter_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
