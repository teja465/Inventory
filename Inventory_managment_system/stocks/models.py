from django.db import models

# Create your models here.
class device(models.Model):
    STATUS_CHOICES = (
        ('available','available'),('No_stock','No_Stock'),('restoring','restoring')
    )
    brand=models.CharField(max_length=20)
    model=models.CharField(max_length=20)
    price=models.IntegerField()
    #status=models.ChoiceField(('available','available'),('No_stock','No_Stock'),('restoring','restoring'))
    status=models.CharField(max_length=15,choices=STATUS_CHOICES)
    issues=models.CharField(max_length=20)

    class Meta:
        abstract=True

class mobile(device):
    pass
class desktop(device):
    pass
class laptop(device):
    pass
