# Generated by Django 3.1.7 on 2021-05-27 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20210527_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipelog',
            name='rating',
            field=models.IntegerField(choices=[('Rating One', 1), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='Rating One', max_length=20),
        ),
    ]
