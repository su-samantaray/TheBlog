# Generated by Django 4.0.2 on 2022-04-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metazoa', '0002_alter_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(upload_to='Blog_img'),
        ),
    ]
