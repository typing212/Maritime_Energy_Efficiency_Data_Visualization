# Generated by Django 3.2.8 on 2021-10-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_visual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_type', models.CharField(max_length=64)),
                ('num_ships', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='visual',
        ),
    ]
