# Generated by Django 4.1.13 on 2024-01-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(max_length=2000)),
                ('stock', models.IntegerField()),
                ('user', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
