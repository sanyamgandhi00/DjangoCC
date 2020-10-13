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
    path('buyAProduct',views.buyAProduct,name="buyAProduct"),
    path('sellAProduct',views.sellAProduct,name="sellAProduct"),
    path('buyBook',views.buyBook,name="buyBook"),
    path('sellBook',views.sellBook,name="sellBook"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)