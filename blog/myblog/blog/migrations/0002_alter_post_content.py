# Generated by Django 5.1.4 on 2024-12-29 02:30

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="content"),
        ),
    ]
