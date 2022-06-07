from django.db import models

# Create
class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=40,default="")
    sub_category = models.CharField(max_length=40,default="")
    price=models.IntegerField(default=0)
    des=models.CharField(max_length=200)
    publish_date=models.DateField()
    image=models.ImageField(upload_to='shop/images',default="")


    def __str__(self):
        return self.product_name