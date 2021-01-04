from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # Get the bag from the session
    bag = request.session.get('bag, {}')
    # If there's nothing in the bag
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('products'))

    # Create an instance of order form
    order_form = OrderForm()
    # Create the template
    template = 'checkout/checkout.html'
    # Create the context containing the form
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
