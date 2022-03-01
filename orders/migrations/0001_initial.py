# Generated by Django 3.2.12 on 2022-03-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sandwich',
            fields=[
                ('order_number', models.AutoField(primary_key=True, serialize=False)),
                ('recipient', models.CharField(default='Anon', max_length=50)),
                ('received_at', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('Ham sandwich', 'Ham sandwich'), ('Cheese sandwich', 'Cheese sandwich'), ('Tuna sandwich', 'Tuna Sandwich')], default='Ham sandwich', max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
