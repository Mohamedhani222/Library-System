from pyexpat import model
from attr import fields
from django import forms
from .models import Books , Category 


class bookform(forms.ModelForm):
        class Meta:
                model = Books 
                fields = ['book_title' ,'book_author','book_image','author_image','book_pages','book_price', 'retal_price_day' ,'retal_peroid','total_rental','status'  ,'category' ,]
                widgets = {
                'book_title' : forms.TextInput(attrs={'class' : 'form-control'}) ,
                'book_author': forms.TextInput(attrs={'class' : 'form-control'}) ,

                'book_pages' : forms.NumberInput(attrs={'class' : 'form-control'}) ,
                'book_price' : forms.NumberInput(attrs={'class' : 'form-control'}) ,
                'retal_price_day': forms.NumberInput(attrs={'class' : 'form-control', 'id' : 'priceretal'}) , 
                'retal_peroid': forms.NumberInput(attrs={'class' : 'form-control' , 'id' :'retalperiod'}) , 
                'total_rental': forms.NumberInput(attrs={'class' : 'form-control' , 'id' : 'total'}) ,
                'status'  : forms.Select(attrs={'class' : 'form-control'}) , 
                'category': forms.Select(attrs={'class' : 'form-control'}) 
                }

        
class catform(forms.ModelForm):
        class Meta :
                model = Category
                fields = ['category_name']
                widgets = {
                        'category_name' : forms.TextInput(attrs={'class' : 'form-control'})
                }

