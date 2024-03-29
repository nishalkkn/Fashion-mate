# Generated by Django 3.2.23 on 2023-12-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orders_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.CharField(blank=True, max_length=45, null=True)),
                ('status', models.CharField(blank=True, db_column='STATUS', max_length=45, null=True)),
                ('working_status', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': False,
            },
        ),
    ]
