from django.db import models


class Order(models.Model):
    order_number = models.IntegerField(default=1)
    received_at = models.DateTimeField(auto_now_add=True, blank=True)
    completed_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Sandwich(Order):

    MAKE = "Make sandwich"
    SERVE = "Serve sandwich"
    TASK_CHOICES = [(MAKE, "Make sandwich"), (SERVE, "Serve sandwich")]
    task = models.CharField(max_length=25, choices=TASK_CHOICES, default=MAKE)
