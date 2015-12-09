from django.conf.urls import url
from .views import WelcomePage, SignIn, Register, verification, Load_Menu, Restaurant_Menu, Review, Portfolio, ContactUs, PlaceOrder, LiveTracking, ScreenShot, rahulanand, aishwarya, vishrut, ashutosh

urlpatterns = [

    url(r'^$', WelcomePage),
    url(r'^signin', SignIn),
    url(r'^register', Register),
    url(r'^verification/', verification),
    url(r'^load_menu/(?P<menu_name>[\w-]+)$', Load_Menu),
    url(r'^rest_menu', Restaurant_Menu),
    url(r'^portfolio', Portfolio),
    url(r'^review', Review),
    url(r'^contact_us', ContactUs),
    url(r'^placeorder/', PlaceOrder),
    url(r'^livetracking/', LiveTracking),
    url(r'^screenshot/', ScreenShot),
    url(r'^rahulanand/', rahulanand),
    url(r'^aishwarya/', aishwarya),
    url(r'^vishrut/', vishrut),
    url(r'^ashutosh/', ashutosh),



]