from django.urls import path 
from shop.views import baby_products,beauty,books,branded,clothing,dvd,electronics,furniture,games,gardening,giftcards,healthcare,industrial,jewellery,kitchen,luxury,musical,office,outdoor,petcare,sports

app_name = 'shop'

urlpatterns = [
  path('clothing/',clothing,name="clothing"),
  path('baby_products/',baby_products,name="baby_products"),
  path('beauty/',beauty,name="beauty"),
  path('books/',books,name="books"),
  path('branded/',branded,name="branded"),
  path('dvd/',dvd,name="dvd"),
  path('electronics/',electronics,name="electronics"),
  path('furniture/',furniture,name="furniture"),
  path('games/',games,name="games"),
  path('gardening/',gardening,name="gardening"),
  path('giftcards/',giftcards,name="giftcards"),
  path('healthcare/',healthcare,name="healthcare"),
  path('industrial/',industrial,name="industrial"),
  path('jewellery/',jewellery,name="jewellery"),
  path('kitchen/',kitchen,name="kitchen"),
  path('luxury/',luxury,name="luxury"),
  path('musical/',musical,name="musical"),
  path('office/',office,name="office"),
  path('outdoor/',outdoor,name="outdoor"),
  path('petcare/',petcare,name="petcare"),
  path('sports/',sports,name="sports"),
]