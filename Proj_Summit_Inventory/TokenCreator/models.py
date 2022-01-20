from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    in_stock = models.BooleanField(default=False)
    delete_now  = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name

    class Meta:
        abstract = False




