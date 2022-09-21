from django.db import models

# Create your models here.


# destination 

class destinaton(models.Model):
    d_name = models.CharField(max_length=200,default='null')
    c_id = models.IntegerField(default='null')
    d_type = models.CharField(max_length=50,default='null')
    d_image = models.CharField(max_length=500,default='null')


    def __str__(self):
        return self.d_name
    

# Guide 

class guide(models.Model):
    g_name = models.CharField(max_length=200,default='null')
    g_image = models.CharField(max_length=500,default='null')
    g_type = models.CharField(max_length=100,default='null')
    g_place = models.IntegerField(default='null')
    g_place_type = models.CharField(max_length=10,default='null')
    g_salary = models.IntegerField(default='null')
    g_experience = models.CharField(max_length=100,default='null')
    g_achivment = models.CharField(max_length=500,default='null')
    g_about = models.CharField(max_length=5000,default='null')


    def __str__(self):
        return self.g_name
    

# hotel

class hotel(models.Model):
    h_name = models.CharField(max_length=500,default='null')
    h_image = models.CharField(max_length=1000,default='null')
    h_rate = models.IntegerField(default='null')
    h_location = models.CharField(max_length=500,default='null')
    h_room = models.CharField(max_length=1000,default='null')
    h_room_about = models.CharField(max_length=500,default='null')
    h_price = models.IntegerField(default='null')
    h_place = models.IntegerField(default='null')
    h_place_type = models.CharField(default='null',max_length=50)


    def __str__(self):
        return self.h_name


# login info table 

class info(models.Model):
    user_name = models.CharField(max_length=100,default='null')
    user_phone_no = models.IntegerField(default='null')
    user_password = models.CharField(max_length=50,default='null')

    def __str__(self):
        return self.user_name


#  info update table 

class pack(models.Model):
    u_name = models.CharField(max_length=100,default='null')
    u_phone = models.IntegerField(default='null')
    u_c_id = models.IntegerField(default='null')
    u_h_name = models.CharField(max_length=500,default='null')
    u_h_image = models.CharField(max_length=1000,default='null')
    u_g_name = models.CharField(max_length=200,default='null')
    u_main_destination = models.CharField(max_length=50,default='null')
    u_sub_destination = models.CharField(max_length=50,default='null')

    def __str__(self):
        return self.u_name
    