# Generated by Django 3.2.23 on 2023-12-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designes',
            fields=[
                ('designe_id', models.AutoField(primary_key=True, serialize=False)),
                ('designes', models.CharField(max_length=45)),
                ('images', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'designes',
                'managed': False,
            },
        ),
    ]
