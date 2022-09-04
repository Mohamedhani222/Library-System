from django.contrib import admin
from .models import *
from .forms import bookform
# Register your models here.
admin.site.register(Category)
admin.site.register(Books)
