from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view to return the index page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag"""

    # Get the quantity from the form
    quantity = int(request.POST.get('quantity'))
    # Get the redirect from the form
    redirect_url = request.POST.get('redirect_url')
    # If product size is in request
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # Check to see if there is a bag variable in the sesssion
    # If not create one
    bag = request.session.get('bag', {})

    # Check if a product with sizes is being added
    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
