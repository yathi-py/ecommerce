from djongo import models

class Products(models.Model):
    """
    Django model representing products with information such as name, price, description, stock, and user.
    Meta:
        - db_table (str): The name of the database table for storing product data.

    Note:
        This model uses Djongo to interact with a MongoDB database.
    """
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=2000)
    stock = models.IntegerField()
    user = models.IntegerField(null=False)

    class Meta:
        db_table = 'products'
