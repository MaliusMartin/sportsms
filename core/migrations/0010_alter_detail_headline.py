# Generated by Django 4.2.1 on 2023-05-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_name_author_fname_author_sname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='headline',
            field=models.CharField(max_length=250),
        ),
    ]
