from django.urls import path
from . import views,urls
from django.conf import settings


urlpatterns = [
    path('', views.index,name="index"),
    #path('sellerSignUp',views.sellerSignUp , name="sellerSignUp" ),
    #path('customerSignUp',views.customerSignUp , name="customerSignUp" ) ,
    path('login' , views.login , name="login"),
    path('logout' , views.logout , name="logout"),
    path('signup',views.signup,name="signup"),
    path('profile',views.profile,name="profile"),
    path('buyAProduct',views.buyAProduct,name="buyAProduct"),
    path('sellAProduct',views.sellAProduct,name="sellAProduct"),
    path('buyBook/<int:bookId>',views.buyBook,name="buyBook"),
    path('buySuit',views.buySuit,name="buySuit"),
    path('buyCoat',views.buyCoat,name="buyCoat"),
    path('buyCalculator',views.buyCalculator,name="buyCalculator"),
    path('buyTool',views.buyTool,name="buyTool"),
    path('sellBook',views.sellBook,name="sellBook"),
    path('sellSuit',views.sellSuit,name="sellSuit"),
    path('sellCoat',views.sellCoat,name="sellCoat"),
    path('sellCalculator',views.sellCalculator,name="sellCalculator"),
    path('advertisements',views.advertisements,name="advertisements"),
    path('orders',views.orders,name="orders"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)