# Generated by Django 4.2.2 on 2023-11-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0007_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='desc',
            field=models.TextField(),
        ),
    ]