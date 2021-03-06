# Generated by Django 3.1.1 on 2020-12-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField(blank=True)),
                ('info', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='tour/')),
            ],
        ),
    ]
