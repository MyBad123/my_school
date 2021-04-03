# Generated by Django 3.1.5 on 2021-04-03 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_codemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('product_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('product_category', models.CharField(max_length=20)),
                ('product_price', models.IntegerField()),
                ('product_sale', models.IntegerField()),
                ('prouct_rating', models.IntegerField()),
                ('prouct_description', models.TextField()),
                ('prouct_sales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.IntegerField()),
                ('review_description', models.TextField()),
                ('review_time', models.DateField(auto_now_add=True)),
                ('review_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productmodel')),
                ('review_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductFavoriteModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productmodel')),
                ('favorite_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket_quantity', models.IntegerField()),
                ('basket_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.productmodel')),
                ('basket_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]