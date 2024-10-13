from django.db import models
CATEGORY_CHOICES = [
    ('appetizer', 'Appetizer'),
    ('main_course', 'Main Course'),
    ('dessert', 'Dessert'),
    ('beverage', 'Beverage'),
    ('side', 'Side Dish'),  # Added side dish category
]

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Add this line
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.name
