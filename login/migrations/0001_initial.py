# Generated by Django 3.2.23 on 2023-12-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('type', models.CharField(blank=True, max_length=45, null=True)),
                ('u_id', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]