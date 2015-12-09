from django.contrib import admin
from .models import UserProfle, Restaurant, Menu, Restaurant_Review, review, orderplaced
from django.contrib.auth.models import User

admin.site.register(UserProfle)
admin.site.register(Restaurant)
admin.site.register(Restaurant_Review)
admin.site.register(review)
admin.site.register(Menu)
admin.site.register(orderplaced)



# Register your models here.
