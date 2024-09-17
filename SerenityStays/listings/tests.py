from django.test import TestCase
from .models import Property

class PropertyModelTest(TestCase):
    def setUp(self):
        self.property = Property.objects.create(
            title="Test Property",
            description="Test description",
            price=100.00,
            location="Test Location",
            available=True
        )

    def test_property_str(self):
        self.assertEqual(str(self.property), "Test Property")

    def test_property_availability(self):
        self.assertTrue(self.property.available)
