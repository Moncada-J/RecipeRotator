# Generated by Django 3.2.3 on 2021-05-23 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cuisine', models.CharField(choices=[('NA', 'North American'), ('SA', 'South American'), ('LA', 'Latin American'), ('AS', 'Asian'), ('EU', 'European'), ('MD', 'Mediterranean'), ('AF', 'African')], default='NA', max_length=3)),
                ('instructions', models.TextField(max_length=500)),
                ('servingsize', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
