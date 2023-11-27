# Generated by Django 4.2.2 on 2023-11-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0016_delete_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bank',
        ),
        migrations.RemoveField(
            model_name='branch',
            name='bname',
        ),
        migrations.AddField(
            model_name='branch',
            name='name',
            field=models.CharField(default='Default Branch Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]