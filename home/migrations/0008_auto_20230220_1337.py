# Generated by Django 3.2.18 on 2023-02-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_position_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='date',
            field=models.CharField(default='0000-00-00', max_length=50),
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.CharField(default='0000-00-00', max_length=50),
        ),
    ]
