# Generated by Django 3.1.7 on 2021-05-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_four',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]
