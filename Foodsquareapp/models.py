from django.contrib.auth.models import User
from django.db import models




class UserProfle(models.Model):
    user = models.OneToOneField(User)
    otp = models.CharField(max_length=30)

    def __unicode__(self):
        return self.otp


class Restaurant(models.Model):
    rest_name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.rest_name



class Restaurant_Review(models.Model):
    rest_name = models.ForeignKey(Restaurant)
    image_name = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s %s"  % (
            self.rest_name,
            self.image_name
        )



class review(models.Model):
    comment = models.CharField(max_length=200)

    def __unicode__(self):
        return self.comment



class Menu(models.Model):
    rest_name = models.ForeignKey(Restaurant)
    dish_name = models.CharField(max_length=60)
    dish_price = models.IntegerField()
    avail = models.BooleanField(default= True)

    def __unicode__(self):
        return "%s %s %s %s"  % (
            self.rest_name,
            self.dish_name,
            self.dish_price,
            self.avail
        )


class orderplaced(models.Model):
    username = models.CharField(max_length=50)
    order = models.CharField(max_length=256)
    order_id = models.CharField(max_length=40)
    placed_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=30, default="Order Placed")

    def __unicode__(self):

        return "%s %s %s %s %s"  % (
            self.username,
            self.order,
            self.order_id,
            self.placed_on,
            self.status
        )



