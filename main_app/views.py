from django.shortcuts import render
from .models import Restaurant

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def restaurants_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {
        'restaurants': restaurants
    })

def restaurants_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant
    })