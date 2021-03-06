# Generated by Django 2.0.6 on 2018-06-12 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datasets', '0001_initial'),
        ('predictors', '0002_auto_20180609_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datasets.Dataset')),
                ('predictor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predictors.Predictor')),
            ],
        ),
    ]
