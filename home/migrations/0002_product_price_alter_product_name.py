# Generated by Django 4.2.4 on 2023-08-15 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
