# Generated by Django 4.1.6 on 2023-02-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art_collections', '0011_alter_collection_image_alter_work_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=models.FilePathField(path='/website/art_collections/static/img'),
        ),
        migrations.AlterField(
            model_name='work',
            name='image',
            field=models.FilePathField(path='/website/art_collections/static/img'),
        ),
    ]
