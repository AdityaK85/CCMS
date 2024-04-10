from django.urls import path
from .views import *
from .views_aj import *
from django.conf import settings
from django.conf.urls.static import static

admin_urls = [
    path('', Login),
    path('Dashboard/', index),
    path('Inventory/', Inventory),
    path('AddInventory/', AddInventory),
    path('Sales/', Sales),
    path('Invoice/<int:id>', Invoice),
    path('Purchased/', Purchased),
    path('Categories/', Categories),
    path('editVendor/<int:id>', editVendor),
    path('editProduct/<int:id>', editProduct),
    path('Manage-Vendor/', ManageVendors),
    path('Reports/', Reports),
]


ajax_urls = [
    
    path('admin_login_aj/', admin_login_aj),
    path('logout_admin/', logout_admin),
    path('SaveInventory/', SaveInventory),
    path('GetInventory/', GetInventory),
    path('get_addr/', get_addr),
    path('SaveSales/', SaveSales),
    path('Add_Prod_On_Sale/', Add_Prod_On_Sale),
    path('SavePurchased/', SavePurchased),
    path('DeleteVendor/', DeleteVendor),
    path('DeleteSale/', DeleteSale),
    path('DeleteProduct/', DeleteProduct),
    path('DeleteService/', DeleteService),
    path('Remove_Prod_From_List/', Remove_Prod_From_List),
    path('SaveService/', SaveService),
    path('filter_report/', filter_report),
]


urlpatterns = [ *admin_urls, *ajax_urls] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)