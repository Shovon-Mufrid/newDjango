# Generated by Django 4.1.3 on 2022-12-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_starts',
            field=models.IntegerField(choices=[(1, 'worst'), (2, 'bad'), (3, 'moderate'), (4, 'good'), (5, 'excellent')]),
        ),
    ]