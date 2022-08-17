# Generated by Django 4.1 on 2022-08-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_post_keyword_post_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='keywords',
        ),
        migrations.AddField(
            model_name='post',
            name='keyword',
            field=models.ManyToManyField(db_column='ds_keyword', to='base.keyword'),
        ),
    ]