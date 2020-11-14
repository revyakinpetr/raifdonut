from django.db import models

import secrets


class Streamer(models.Model):
    name = models.TextField()
    surname = models.TextField()
    nickname = models.TextField()
    account = models.TextField(null=True)
    token = models.TextField(null=True)
    min_donation = models.DecimalField(max_digits=20, decimal_places=2, default=10.0)

    def save(self, *args, **kwargs):
        self.token = secrets.token_urlsafe(20)
        super(Streamer, self).save(*args, **kwargs)


class Donat(models.Model):
    streamer_id = models.IntegerField()
    name = models.TextField(max_length=50)
    text = models.TextField(max_length=200, null=True)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    currency = models.TextField(max_length=3, default="RUB")
    create_date = models.DateTimeField(auto_now_add=True)
    qr_id = models.TextField(max_length=40, null=True)
    qr_url = models.TextField(null=True)
    payment_state = models.TextField(max_length=15, null=True)