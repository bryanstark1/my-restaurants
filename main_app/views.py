from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Restaurant

# VIEW FUNCTIONS
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def restaurants_index(request):
  restaurants = Restaurant.objects.filter(user=request.user)
  return render(request, 'restaurants/index.html', {
    'restaurants': restaurants
  })

@login_required
def restaurants_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  return render(request, 'restaurants/detail.html', {
    'restaurant': restaurant
  })


# CLASS BASED VIEWS
class RestaurantCreate(LoginRequiredMixin, CreateView):
  model = Restaurant
  fields = ['name', 'location', 'cuisine', 'description']

  # Assigns new object to logged in user
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RestaurantUpdate(LoginRequiredMixin, UpdateView):
  model = Restaurant
  fields = ['name', 'location', 'cuisine', 'description']

class RestaurantDelete(LoginRequiredMixin, DeleteView):
  model = Restaurant
  success_url='/restaurants'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)