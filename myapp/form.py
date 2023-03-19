from django.db import models

class Users(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fname +" "+ self.lname
    @staticmethod
    def get_email(email):
        try:
            return Users.objects.get(email=email)
        except:
            return False
    @staticmethod
    def get_pass(email,password):
        try:
            return Users.objects.get(password=password,email=email)
        except:
            return False
    @staticmethod
    def get_data(email):
        try:
            return Users.objects.get(email=email)
        except:
            return False