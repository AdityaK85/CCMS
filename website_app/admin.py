from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(InventoryMaster)
class InventoryMasterAdmin(admin.ModelAdmin):
    list_display = ('id' , 'product_name', 'product_no', 'fk_category')

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('id' , 'username', 'password')

@admin.register(CountryMaster)
class CountryMasterAdmin(admin.ModelAdmin):
    list_display = ('id' , 'country_name')

@admin.register(StateMaster)
class StateMasterAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name', 'country')

@admin.register(CityMaster)
class CityMasterAdmin(admin.ModelAdmin):
    list_display = ('id' , 'name', 'state_id')

@admin.register(CategoryMaster)
class CategoryMasterAdmin(admin.ModelAdmin):
    list_display = ('id' , 'category_name')


@admin.register(SalesMaster)
class SalesMasterAdmin(admin.ModelAdmin):
    list_display = ('id' , 'fk_product', 'company_name', 'mobile_no', 'email')

@admin.register(SalesProducts)
class SalesProductsAdmin(admin.ModelAdmin):
    list_display = ('id' , 'fk_sale', 'fk_product', 'qty', 'total_amount')

@admin.register(PurchasedMaster)
class PurchasedMasterAdmin(admin.ModelAdmin):
    list_display = ('id' , 'vendor_code', 'vendor_name', 'purchased_dt', 'phone')