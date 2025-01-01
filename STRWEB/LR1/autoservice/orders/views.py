from django.shortcuts import render, redirect


def customer_view(request):
    if request.user.is_employee:
        return redirect('/')
    orders = request.user.customer.order_set.all()
    return render(request, 'orders_of_customer.html', {'orders': orders})
