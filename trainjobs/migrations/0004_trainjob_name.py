# Generated by Django 2.0.6 on 2018-06-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainjobs', '0003_trainjob_state_pickle'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainjob',
            name='name',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]
