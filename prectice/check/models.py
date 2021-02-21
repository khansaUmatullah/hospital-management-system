from django.db import models

# Create your models here.
class employee(models.Model):
    
    
    
    name=models.CharField(max_length=10)
    address=models.CharField(max_length=20)
    department=models.CharField(max_length=10)
    sex=models.CharField(max_length=10)
    salary=models.IntegerField()
class doctors(models.Model):
    Employee=models.ForeignKey(employee,null=True, blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=10)
    image=models.ImageField()
    phoneno=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
class nurses(models.Model):
    Employee=models.ForeignKey(employee,null=True, blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=10)
    image=models.ImageField()
    phoneno=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
class receiptionist(models.Model):
    Employee=models.ForeignKey(employee,null=True, blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=10)
    image=models.ImageField()
    phoneno=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)


class room(models.Model):
    capacity=models.IntegerField()
   
    Nurses=models.ForeignKey(nurses,null=True, blank=True,on_delete=models.CASCADE)






class patient(models.Model):
    
    
    
    Bill=models.IntegerField()
    bill_date=models.DateField()
    name=models.CharField(max_length=10)
    age=models.IntegerField()
    b_group=models.CharField(max_length=10)
    
    
    phoneno=models.CharField(max_length=100)
class admitted(models.Model):
    Patient=models.ForeignKey(patient,null=True, blank=True,on_delete=models.CASCADE)
    admitteddate=models.DateField()
    Room=models.ForeignKey(room,null=True, blank=True,on_delete=models.CASCADE)
class visited(models.Model):
    Patient=models.ForeignKey(patient,null=True, blank=True,on_delete=models.CASCADE)
    visiteddate=models.DateField()
class attend(models.Model):
    Doctors=models.ForeignKey(doctors,null=True, blank=True,on_delete=models.CASCADE)
    Patient=models.ForeignKey(patient,null=True, blank=True,on_delete=models.CASCADE)
    date=models.DateField()
class records(models.Model):
    Receiptionist=models.ForeignKey(receiptionist,null=True, blank=True,on_delete=models.CASCADE)
    patients_info=models.TextField()
    app_date=models.DateField()
class prescription(models.Model):
    pres_date=models.DateField()
class prescribed(models.Model):
    Prescription=models.ForeignKey(prescription,null=True, blank=True,on_delete=models.CASCADE)
    Doctors=models.ForeignKey(doctors,null=True, blank=True,on_delete=models.CASCADE)
    testorPres=models.CharField(max_length=20)
class furniture(models.Model):
    Noofbeds=models.IntegerField()
    Room=models.ForeignKey(room,null=True, blank=True,on_delete=models.CASCADE)
class surgical_instruments(models.Model):
    name=models.CharField(max_length=20)
    Doctors=models.ForeignKey(doctors,null=True, blank=True,on_delete=models.CASCADE)
class staff_supplies(models.Model):
    name=models.CharField(max_length=20)
    Employee=models.ForeignKey(employee,null=True, blank=True,on_delete=models.CASCADE)
class pharmacy(models.Model):
    medicine_record=models.CharField(max_length=20)

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10)
    message=models.TextField()



