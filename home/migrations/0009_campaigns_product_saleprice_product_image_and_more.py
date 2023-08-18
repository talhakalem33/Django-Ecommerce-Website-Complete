# Generated by Django 4.2.4 on 2023-08-15 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='SalePrice',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='isPopularInMainPage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='isSale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='isSaleInMainPage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='campaign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.campaigns'),
        ),
    ]
