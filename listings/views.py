from django.shortcuts import render, get_object_or_404
from .models import Property
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

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
