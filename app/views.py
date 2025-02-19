from django.db.models import Q
from django.shortcuts import render, redirect

from .forms import CarCreateForm
from .models import Car, Category

def index_view(request):
    cars = Car.objects.all()
    categories = Category.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        cars = Car.objects.filter(Q(make__icontains=search) | Q(model__icontains=search))

    return render(request, 'app/main.html', {'cars': cars, 'categories': categories})

def one_item(request, pk):
    car = Car.objects.get(id=pk)
    categories = Category.objects.all()

    return render(request, 'app/one_item.html', {'car': car, 'categories': categories})

def one_category(request, category):
    category_obj = Category.objects.get(title=category)
    cars = Car.objects.filter(category=category_obj)
    categories = Category.objects.all()

    return render(request, 'app/one_category.html', {'cars': cars, 'categories': categories})

def add_car(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        image = request.FILES['image']
        year = request.POST['year']
        price = request.POST['price']
        description = request.POST['description']
        category_id = request.POST['category_id']

        category = Category.objects.get(id=category_id)

        car = Car(make=make, model=model, image=image, year=year, price=price, description=description, category=category)
        car.save()

        return redirect('main')

    return render(request, 'app/add_car.html', {'categories': categories})

def add_car_2(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = CarCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return redirect('main')

    form = CarCreateForm()

    return render(request, 'app/add_car_2.html', {'form': form, 'categories': categories})