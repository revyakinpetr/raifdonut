# Generated by Django 2.2.9 on 2020-11-14 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streamer', '0003_auto_20201114_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donat',
            name='payment_state',
            field=models.TextField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='donat',
            name='qr_id',
            field=models.TextField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='donat',
            name='qr_url',
            field=models.TextField(null=True),
        ),
    ]