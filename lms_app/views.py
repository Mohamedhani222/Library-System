
from django.shortcuts import get_object_or_404 , redirect, render
from .models import *
from .forms import bookform , catform
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        add_book =bookform(request.POST , request.FILES)
        if add_book.is_valid():
            add_book.save()
    if request.method == 'POST':
        cat_name = catform(request.POST)
        if cat_name.is_valid():
            cat_name.save()
    x ={
        'Books' : Books.objects.all(),
        'book_count' : Books.objects.filter(active = True).count(),
        'category' : Category.objects.all(),
        'bf' : bookform(),
        'add_book' : bookform(request.POST , request.FILES),
        'cf' : catform() ,
        'done' : 'book was added',
        'booksold' : Books.objects.filter(status ='sold').count(),
        'bookavailable' : Books.objects.filter(status ='available').count(),
        'bookrented' : Books.objects.filter(status ='rented').count(),
    }
    return render(request , 'pages/index.html' , context = x)

@login_required(login_url='login')
def books(request):

    search = Books.objects.all()
    title = None

    if 'search_name' in request.GET:
        title = request.GET['search_name']
    if title :
        search = search.filter(book_title__icontains = title )
            
    x ={
        'Books' : search,
        'category' : Category.objects.all()
        
}
    return render(request , 'pages/books.html' , context= x)

def update(request , id):
    book_id = Books.objects.get(id=id)
    if request.method == 'POST':
        book_save = bookform(request.POST , request.FILES ,instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect("/")
    else:
        book_save =bookform(instance=book_id)
        
    context ={
        'form' : book_save,
    }
    return render(request , 'pages/update.html' , context)
    
def delete (request , id):
    book_delete =Books.objects.get(id = id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect("/")
    context ={
        'form_delete' : book_delete
    }
    return render(request , 'pages/delete.html' , context)


