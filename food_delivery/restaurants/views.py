from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant, MenuItem

# List of restaurants
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Restaurant

# View to display the menu for a specific restaurant
def menu_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)

    # Initialize selected_items in session if not present
    if 'selected_items' not in request.session:
        request.session['selected_items'] = []

    # Handle POST request for item selection
    if request.method == 'POST':
        selected_item_id = request.POST.get('item_id')
        if selected_item_id:
            # Add the selected item ID to the session
            request.session['selected_items'].append(selected_item_id)
            request.session.modified = True  # Mark session as modified

    # Retrieve the selected menu items using the IDs in session
    selected_items = MenuItem.objects.filter(id__in=request.session['selected_items'])

    return render(request, 'restaurants/menu.html', {
        'menu_items': menu_items,
        'selected_items': selected_items,
        'restaurant': restaurant
    })

# Cart view
def cart_view(request):
    # Get the selected items from the session
    selected_items = MenuItem.objects.filter(id__in=request.session.get('selected_items', []))

    # Calculate total amount
    total_amount = sum(item.price for item in selected_items)

    return render(request, 'restaurants/cart.html', {
        'items': selected_items,
        'total_amount': total_amount,
    })

# Place order view (you can expand this further for actual order processing)
def place_order(request):
    if request.method == 'POST':
        # Logic to handle order placement can go here
        # Clear the selected items from the session
        request.session['selected_items'] = []
        request.session.modified = True  # Mark session as modified

        # Redirect or render a success page
        return redirect('order_success')  # Ensure this URL is defined in your urls.py

    return redirect('cart')  # Redirect to cart for a GET request

# View for order success
def order_success(request):
    return render(request, 'restaurants/order_success.html')
