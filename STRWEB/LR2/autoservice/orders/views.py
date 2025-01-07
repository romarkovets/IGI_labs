from django.shortcuts import render, redirect
from .models import Service, Order


def customer_view(request):
    if request.user.is_employee:
        return redirect('/')
    orders = request.user.customer.order_set.all()
    return render(request, 'orders_of_customer.html', {'orders': orders})


def create_order(request):
    if request.method == 'POST':
        # Находим услугу по названию
        service_id = request.POST.get('service_id')
        service = Service.objects.get(id=service_id)

        # Создаём заказ
        order = Order.objects.create(service=service, customer=request.user.customer)
        order.save()

    return redirect('/services/')

def update_quantity(request, order_id):
    # Получаем заказ по его ID
    order = Order.objects.get(id=order_id)

    if request.method == 'POST':
        # Получаем новое количество из формы
        new_quantity = int(request.POST.get('quantity'))

        # Проверяем, что количество в пределах допустимого диапазона
        if 1 <= new_quantity <= 100:
            order.quantity = new_quantity  # Обновляем количество
            order.save()  # Сохраняем изменения
        else:
            # Можно добавить ошибку в случае неправильного ввода
            # Например, вернуть сообщение об ошибке, если количество вне диапазона
            pass

    # Перенаправляем на страницу с заказами
    return redirect('/customerorders/')  # Замените 'order_list' на название вашего маршрута с заказами


def delete_order(request, order_id):
    if request.method == 'POST':
        # Получаем заказ по ID и удаляем
        order = Order.objects.get(id=order_id)
        order.delete()
        # Перенаправляем на список заказов
        return redirect('/customerorders/')  # Или другой ваш маршрут

def pay_order(request, order_id):
    # Отображение страницы подтверждения оплаты
    order = Order.objects.get(id=order_id)
    return render(request, 'payment_confirmation.html', {'order': order})

def confirm_payment(request, order_id):
    # Обработка подтверждения оплаты
    if request.method == 'POST':
        order = Order.objects.get(id=order_id)
        order.is_received = True  # Устанавливаем флаг оплаты
        order.save()
        return redirect('/customerorders/')