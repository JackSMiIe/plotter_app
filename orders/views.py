from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order

def home(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # после сохранения перезагружаем страницу
    else:
        form = OrderForm()

    orders = Order.objects.all().order_by('-created_at')  # все заказы, последние сверху
    return render(request, 'orders/home.html', {'form': form, 'orders': orders})

