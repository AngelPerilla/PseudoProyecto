# Generated by Django 5.1 on 2024-08-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='nombres',
        ),
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]
