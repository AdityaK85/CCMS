from django.urls import path
from .views import *
from .views_aj import *
from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('BestThings/', index),
    path('Inventory/', Inventory),
    path('AddInventory/', AddInventory),
    path('Sales/', Sales),
    path('Invoice/<int:id>', Invoice),
    path('Votings/', Votings),
]


ajax_urls = [
    
    path('SaveInventory/', SaveInventory),
    path('GetInventory/', GetInventory),
    path('get_addr/', get_addr),
    path('SaveSales/', SaveSales),
    path('Add_Prod_On_Sale/', Add_Prod_On_Sale),
]


urlpatterns = [ *admin_urls, *ajax_urls] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)