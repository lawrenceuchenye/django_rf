from django.db import models

# Create your models here.
class Product(models.Model):
  title=models.CharField(max_length=255)
  body=models.TextField()
  price=models.DecimalField(max_digits=10,decimal_places=2,default=99.99)

  @property
  def sale_pricee(self):
     return "%.2f"%(float(self.price)*0.6)

  def get_discount(self):
     return "345"
