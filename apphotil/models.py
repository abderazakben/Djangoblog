from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 

# Create your models here.
ORDER_STATUS= (
     ("Hour" , "1000"),
     ("date" , "100"),
 )
class Hotel(models.Model):
    quantity = models.CharField(max_length=200, null=True,blank=True , choices=ORDER_STATUS )
    hour = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveIntegerField(blank=True)
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    #change required التغيير المطلوب 
    date = models.DateTimeField(default=timezone.now)

    # fonctions total_price functions  calcule tot prix 
    def save(self, *args, **kwargs):
        self.total_price = self.hour * self.quantity
        super().save(*args,**kwargs)

    def __str__(self):
        return "Solled {} - {} items for {}".format(self.hour , self.quantity , self.total_price)
        print(total_price) 


ORDER_STATUS2= (
     ("Vito" , "350"),
     ("E220" , "500"),
     ("Santafi" , "300"),
)
class Matar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_stiy = models.CharField(max_length=200 , null=True, blank=True)
    Cars = models.CharField(max_length=200, null=True,blank=True , choices=ORDER_STATUS2 )
    # date_activiti = date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
         return " trage Matar{}".format(self.user) 




