# Generated by Django 2.1.5 on 2019-01-20 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]