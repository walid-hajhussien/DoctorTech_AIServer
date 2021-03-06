# Generated by Django 2.1.4 on 2019-01-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diabetes', '0002_diabetes_outcome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diabetes',
            name='Age',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='BMI',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='BloodPressure',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='DiabetesPedigreeFunction',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='Glucose',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='Insulin',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='Outcome',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='Pregnancies',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='diabetes',
            name='SkinThickness',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
