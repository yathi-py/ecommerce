from djongo import models

class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=2000)
    stock = models.IntegerField()
    user = models.IntegerField(null=False)

    class Meta:
        db_table = 'products'
