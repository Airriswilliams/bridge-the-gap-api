# Generated by Django 4.0.5 on 2022-06-09 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bridgethegapapi', '0003_remove_review_session'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='session_review',
            new_name='tutor_review',
        ),
    ]
