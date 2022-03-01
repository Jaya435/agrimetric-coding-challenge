from django.db import models


class Order(models.Model):
    order_number = models.IntegerField(primary_key=True)
    recipient = models.CharField(max_length=50, default="Anon")
    received_at = models.DateTimeField(auto_now_add=True, blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Sandwich(Order):

    HAM = "Ham sandwich"
    CHEESE = "Cheese sandwich"
    TUNA = "Tuna sandwich"
    TASK_CHOICES = [(HAM, "Ham sandwich"), (CHEESE, "Cheese sandwich"), (TUNA, "Tuna Sandwich")]
    type = models.CharField(max_length=25, choices=TASK_CHOICES, default=HAM)

    def get_incomplete_orders(self):
        return self._meta.model.objects.filter(completed=False).order_by('received_at')

