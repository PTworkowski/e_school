# Generated by Django 3.1.2 on 2020-11-19 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration_app', '0004_auto_20201119_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='day',
            field=models.CharField(choices=[(0, 'Poniedziałek'), (1, 'Wtorek'), (2, 'Środa'), (3, 'Czwartek'), (4, 'Piątek'), (5, 'Sobota'), (6, 'Niedziela')], max_length=255),
        ),
    ]
