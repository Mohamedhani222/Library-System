
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.category_name



class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
    x = [
        ('available','available'),
        ('rented' , 'rented'),
        ('sold' , 'sold')
    ]
    book_title =models.CharField(max_length=250)
    book_author=models.CharField(max_length=250)
    book_image =models.ImageField(upload_to = 'photos' , null =True , blank= True)
    author_image =models.ImageField(upload_to = 'photos' , null =True , blank= True)
    book_pages = models.IntegerField( null =True , blank= True)
    book_price = models.DecimalField(max_digits=6 , decimal_places=2 ,null =True , blank= True)
    retal_price_day = models.DecimalField(max_digits=6 , decimal_places=2 ,null =True , blank= True)
    retal_peroid = models.IntegerField( null =True , blank= True)
    total_rental = models.DecimalField(max_digits=6 , decimal_places=2 ,null =True , blank= True)
    active = models.BooleanField(default=True)
    status =models.CharField(max_length=50 , choices= x , null =True , blank= True)
    category = models.ForeignKey(Category , on_delete=models.PROTECT, null =True , blank= True)
    
    def __str__(self) -> str:
        return self.book_title


