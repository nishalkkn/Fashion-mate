# Generated by Django 3.2.23 on 2023-12-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models',
            fields=[
                ('models_id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=45)),
                ('uplode_image', models.CharField(blank=True, max_length=45, null=True)),
                ('amount', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'models',
                'managed': False,
            },
        ),
    ]
