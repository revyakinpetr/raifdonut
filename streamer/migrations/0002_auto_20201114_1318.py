# Generated by Django 2.2.9 on 2020-11-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donat',
            name='qr_id',
            field=models.TextField(max_length=40),
        ),
        migrations.AlterField(
            model_name='streamer',
            name='account',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='streamer',
            name='min_donation',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='streamer',
            name='token',
            field=models.TextField(null=True),
        ),
    ]
