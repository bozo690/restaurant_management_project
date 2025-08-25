from django.db import models
from ddjango.conf import settings #used to link to the built-in user model

class MenuItem(models.model):
    """
    Represents a single dish or item available on the restaurant's menu.
    """
    name=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self)
        return f"{self.name} -${self.price}"

class Order(models.Model):
    """
    Represents a customer's order, containing one or more menu items.
    """

    STATUS_CHOICES=(
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )


    items=models.ManyToManyField(MenuItem, through='OrderItem')

    total_amount=models.DecimalField(max_digits=10, decimal_places=2)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at=models.DateTimeField(auto_new_add=True)

    def __str__(self):
        return f"Order #{self.id} - status: {self.status}"

class OrderItem(models.Model):

    """
    This "through" model allows us to store the quantity of each menu item within a  specific order.
    """

    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item=models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} in order #{self.order.id}"   
