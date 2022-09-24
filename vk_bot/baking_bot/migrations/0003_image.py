# Generated by Django 3.2.13 on 2022-09-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baking_bot', '0002_auto_20220917_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='baking_bot/img')),
                ('image_b64', models.BinaryField(blank=True, null=True)),
            ],
        ),
    ]