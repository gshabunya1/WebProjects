from django.db import models
from datetime import datetime, timezone

# Create your models here.

class People(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dr = models.DateField('ДР', default=timezone.now)
    adress_sity = models.CharField(max_length=50)
    adress_streat = models.CharField(max_length=50)
    adress_haus = models.CharField(max_length=50)
    adress_flat = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
        
    class Meta:
        ordering = ["last_name"]
        
class Customers(People):
    firm_email = models.CharField(max_length=255)
    firm = models.CharField(max_length=255)
 
class Staff(People):
    mail2 = models.CharField(max_length=255)
    foto = models.CharField(max_length=255)
    fotos = models.CharField(max_length=255)
    current_projects = models.ForeignKey(Event, on_delete=models.CASCADE)
    SET_JOB = (
        (1, "директор"),
        (2, "старший менеджер"),
        (3, "креативный директор"),
        (4, "менеджер проекта"),
        (5, "аниматор"),
        (6, "фотограф"),
        (7, "художник"),
        (8, "рабочий"),
        (9, "программист")
    )
    job = models.IntegerField(choices=SET_JOB, default=1)
       
class Places(models.Model):
    short_name = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    eu_name = models.CharField(max_length=255)
    adress_sity = models.CharField(max_length=50)
    adress_streat = models.CharField(max_length=50)
    adress_haus = models.CharField(max_length=50)
    point_on_map1 = models.FloatField()
    point_on_map2 = models.FloatField()
    plus_code = models.CharField(max_length=50)
    
    class Meta:
        ordering = ["name"]

class Events(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    start_date = models.DateField('Дата', default=timezone.now)
    end_date = models.DateField('Дата', default=timezone.now)
    team_leader = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ["name"]

class Hotels(Places):
    comfort = models.IntegerField()
    manager = models.ForeignKey(People, on_delete=models.CASCADE)
    phone_1 = models.CharField(max_length=20)
    name_1 = models.CharField(max_length=50)
    phone_2 = models.CharField(max_length=20)
    name_2 = models.CharField(max_length=50)
    phone_3 = models.CharField(max_length=20)
    name_3 = models.CharField(max_length=50)

class Restaurants(Places):
    food = models.CharField(max_length=50)
    manager = models.ForeignKey(People, on_delete=models.CASCADE)
    chef = models.ForeignKey(People, on_delete=models.CASCADE)
    phone_1 = models.CharField(max_length=20)
    name_1 = models.CharField(max_length=50)
    phone_2 = models.CharField(max_length=20)
    name_2 = models.CharField(max_length=50)
    phone_3 = models.CharField(max_length=20)
    name_3 = models.CharField(max_length=50)
    room = models.IntegerField()
    seats = models.IntegerField()
    
class Portfolio(models.Model):
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    place_id = models.ForeignKey(Places, on_delete=models.CASCADE)
    picture = models.CharField(max_length=255)
