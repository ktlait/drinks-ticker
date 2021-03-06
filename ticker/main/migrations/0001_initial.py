# Generated by Django 2.1.3 on 2018-11-12 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foster', models.DecimalField(decimal_places=2, max_digits=5)),
                ('g_t', models.DecimalField(decimal_places=2, max_digits=5)),
                ('captain_morgan', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pampero', models.DecimalField(decimal_places=2, max_digits=5)),
                ('roe_and_co', models.DecimalField(decimal_places=2, max_digits=5)),
                ('zaconey', models.DecimalField(decimal_places=2, max_digits=5)),
                ('vodka_redbull', models.DecimalField(decimal_places=2, max_digits=5)),
                ('interval_index', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
