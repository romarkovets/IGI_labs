from django.shortcuts import render, redirect

# Create your views here.

def employee_view(request):
    if not request.user.staff:
        return redirect('/')
    orders = request.user.employee.order_set.all()
    return render(request, 'orders_of_employee.html', {'orders': orders})




def customer_view(request):
    if request.user.staff:
        return redirect('/')
    orders = request.user.customer.order_set.all()
    return render(request, 'orders_of_customer.html', {'orders': orders})
