# Generated by Django 4.2.2 on 2023-11-26 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0023_userprofile_delete_branch_delete_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='district',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
