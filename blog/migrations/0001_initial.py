# Generated by Django 5.0.3 on 2024-03-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=60)),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
    ]