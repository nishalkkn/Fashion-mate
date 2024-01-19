# Generated by Django 3.2.23 on 2023-12-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('materials', models.CharField(max_length=45)),
                ('uplod_image', models.CharField(blank=True, db_column='uplod image', max_length=500, null=True)),
            ],
            options={
                'db_table': 'materials',
                'managed': False,
            },
        ),
    ]
