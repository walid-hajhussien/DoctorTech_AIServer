# Generated by Django 2.1.4 on 2019-01-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HeartAttack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heartattack',
            name='pred_attribute',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]