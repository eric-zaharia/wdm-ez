# Generated by Django 3.0.4 on 2020-03-24 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tema', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cont',
            new_name='Account',
        ),
        migrations.RenameModel(
            old_name='Comentariu',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Postare',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='cont',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='postare',
            new_name='post',
        ),
    ]
