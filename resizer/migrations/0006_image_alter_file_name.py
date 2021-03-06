# Generated by Django 4.0.4 on 2022-05-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resizer', '0005_rename_image_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(upload_to='generated')),
            ],
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
