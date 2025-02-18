from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/car_image')
    year = models.PositiveSmallIntegerField()
    price = models.DecimalField(decimal_places= 2,max_digits=100    )
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.make} {self.model}'

