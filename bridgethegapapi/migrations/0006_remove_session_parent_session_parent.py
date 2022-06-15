# Generated by Django 4.0.5 on 2022-06-15 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridgethegapapi', '0005_alter_tutor_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='parent',
        ),
        migrations.AddField(
            model_name='session',
            name='parent',
            field=models.ManyToManyField(related_name='parents', to='bridgethegapapi.parent'),
        ),
    ]
