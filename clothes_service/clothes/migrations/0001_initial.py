# Generated by Django 4.1.13 on 2024-04-25 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClothesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'c_categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField(default=1)),
                ('images', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='clothes.clothescategory')),
            ],
            options={
                'db_table': 'clothes',
                'ordering': ['-created_at'],
            },
        ),
    ]
