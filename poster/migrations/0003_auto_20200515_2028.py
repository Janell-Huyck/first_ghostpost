# Generated by Django 3.0.6 on 2020-05-15 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poster', '0002_auto_20200515_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghostpost',
            name='down_votes',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='ghostpost',
            name='magic_string',
            field=models.CharField(editable=False, max_length=6),
        ),
        migrations.AlterField(
            model_name='ghostpost',
            name='up_votes',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]