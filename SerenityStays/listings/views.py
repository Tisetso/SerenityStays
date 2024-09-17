from django.shortcuts import render, get_object_or_404
from .models import Property

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'listings/property_list.html', {'properties': properties})

def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, 'listings/property_detail.html', {'property': property})

def booking(request, id):
    property = get_object_or_404(Property, id=id)
    # Add your booking logic here
    return render(request, 'listings/booking.html', {'property': property})
