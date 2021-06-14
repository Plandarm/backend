# Generated by Django 3.2.4 on 2021-06-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_page_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='html',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(blank=True, default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
