# Generated by Django 2.1 on 2018-11-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
