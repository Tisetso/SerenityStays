from django.shortcuts import render, get_object_or_404
from .models import Property
import stripe
from django.conf import settings

stripe.api_key = "sk_test_51Q02leEvFmUjZecbAq6t6b2lJfGpWirgYCIdv60GrM7TfA9cdVLP6q9XeJVpGYnSntTogEdvdGcvvxb2navO7PSK00jCbae43W"

def home(request):
    return render(request, 'listings/home.html')

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'listings/property_list.html', {'properties': properties})

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})

def book_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    if request.method == 'POST':
        # Handle payment and booking here
        token = request.POST.get('stripeToken')
        charge = stripe.Charge.create(
            amount=int(property.price_per_night * 100),  # amount in cents
            currency='usd',
            description=f"Booking for {property.title}",
            source=token,
        )
        return render(request, 'listings/success.html', {'property': property})
    return render(request, 'listings/booking.html', {'property': property})
