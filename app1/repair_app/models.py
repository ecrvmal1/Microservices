from django.db import models

# Create your models here.

class Repair(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE,
                              verbose_name="Smartphone")

    STATUSES = (
        ("N", 'NO'),
        ('P', 'PROCESS'),
        ('D', 'DONE'),
    )
    status = models.CharField(max_length=1,
                              choices=STATUSES,
                              verbose_name='Status')

    create = models.DateTimeField(auto_now_add=True,
                                  verbose_name="Creation Date and time")


