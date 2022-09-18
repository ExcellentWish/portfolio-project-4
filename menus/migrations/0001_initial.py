# Generated by Django 3.2.15 on 2022-09-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkItems',
            fields=[
                ('drink_id', models.AutoField(primary_key=True, serialize=False)),
                ('drink_name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('price', models.IntegerField()),
                ('allergens', models.CharField(max_length=200)),
                ('on_menu', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-on_menu'],
            },
        ),
        migrations.CreateModel(
            name='FoodItems',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('price', models.IntegerField()),
                ('dietary', models.CharField(max_length=200)),
                ('allergens', models.CharField(max_length=200)),
                ('on_menu', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-on_menu'],
            },
        ),
    ]