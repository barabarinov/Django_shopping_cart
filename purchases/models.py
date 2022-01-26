from django.db import models


class Cart(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class Purchase(models.Model):
    name = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)
    is_bought = models.BooleanField(default=False)
    cart_id = models.ForeignKey(
        'purchases.Cart',
        related_name='purchases',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name}'
