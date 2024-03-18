from django.db import models

# Create your models here.


class contact(models.Model):
    fn=models.CharField(max_length=20)
    ln=models.CharField(max_length=15)
    ed=models.CharField(max_length=50)
    cm=models.TextField()


    def __str__(self):
        return "customer detail :"+self.fn
    

class register(models.Model): 
    sname=models.CharField(max_length=10)
    rpwd=models.CharField(max_length=15)
    remail=models.CharField(max_length=20)
    radd=models.TextField()
    rphone=models.IntegerField(max_length=10)


    def __str__(self):
        return "register Id :"+self.sname
    

class iteams(models.Model):
    iname=models.CharField(max_length=20)
    iprice=models.IntegerField()
    image=models.ImageField(upload_to="images/")


    def __str__(self):
        return "item name :"+self.iname
    
class cartadd(models.Model):
    iname=models.CharField(max_length=20)
    iprice=models.IntegerField()
    image=models.ImageField(upload_to="images/")
    pquantity=models.CharField(max_length=2,default=1)
    ptotalprice=models.CharField(max_length=10,default=50)


    def __str__(self):
        return "item name :"+self.iname

        
    