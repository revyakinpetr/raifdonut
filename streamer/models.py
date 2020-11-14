from django.db import models


class Streamer(models.Model):
    name = models.TextField();
    surname = models.TextField();
    nickname = models.TextField();
    account = models.TextField();
    token = models.TextField();
    min_donation = models.DecimalField(max_digits=20, decimal_places=2);


class Donat(models.Model):
    streamer_id = models.IntegerField();
    name = models.TextField(max_length=50);
    text = models.TextField(max_length=200);
    amount = models.DecimalField(max_digits=20, decimal_places=2);
    currency = models.TextField(max_length=3, default="RUB");
    create_date = models.DateTimeField();
    qr_id = models.TextField(max_length=32);
    qr_url = models.TextField();
    payment_state = models.TextField(max_length=15);