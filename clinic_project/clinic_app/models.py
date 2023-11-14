from django.db import models

# Create your models here.

class Messages(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    subject= models.CharField(max_length=50)
    message= models.CharField(max_length=1000)
    
class Depatrments(models.Model):
    dep_name= models.CharField(max_length=50)
    description= models.TextField()
    
    def __str__(self):
        return self.dep_name 

class Doctorlist(models.Model):
    img= models.ImageField(upload_to='img')
    doc_name= models.CharField(max_length= 100)
    doc_spec = models.CharField(max_length=100, null=True)
    doc_dep= models.ForeignKey(Depatrments, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.doc_name + " (" + self.doc_spec + ")"    

class Appointment(models.Model):
    name= models.CharField(max_length=100)
    mail= models.EmailField(max_length=155)
    mobile= models.IntegerField()
    doctor= models.ForeignKey(Doctorlist, on_delete=models.CASCADE)
    date= models.DateField()
    booked_on= models.DateField(auto_now=True) 
