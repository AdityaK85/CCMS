from django.db import models
import datetime
# Create your models here.

class Admin(models.Model):
    username =  models.CharField(max_length = 200, blank = True, null = True)
    password =  models.CharField(max_length = 200, blank = True, null = True)

class CategoryMaster(models.Model):
    category_name = models.CharField(max_length = 200, blank = True, null = True)

class CountryMaster(models.Model):
    country_name = models.CharField(max_length = 200, blank = True, null = True)

class StateMaster(models.Model):
    name = models.CharField(max_length = 100 , blank = True , null = True)
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE, blank=True, null=True)

class CityMaster(models.Model):
    name = models.CharField(max_length = 100 , blank = True , null = True)
    state_id = models.ForeignKey(StateMaster, on_delete=models.CASCADE, blank=True, null=True)

class PurchasedMaster(models.Model):
    vendor_code = models.CharField(max_length = 200, blank = True, null = True)
    vendor_name = models.CharField(max_length = 200, blank = True, null = True)
    purchased_dt = models.DateField(blank = True, null = True)
    phone = models.CharField(max_length = 200, blank = True, null = True)
    mail = models.CharField(max_length = 200, blank = True, null = True)
    other_link = models.CharField(max_length = 200, blank = True, null = True)
    note = models.TextField(blank = True, null = True)
    created_dt = models.DateTimeField(blank=True , null= True , default= datetime.datetime.now())

class InventoryMaster(models.Model):
    product_name = models.CharField(max_length = 200, blank = True, null = True)
    product_no = models.CharField(max_length = 200, blank = True, null = True)
    fk_category = models.ForeignKey(CategoryMaster, on_delete=models.CASCADE , blank = True, null = True)
    model = models.CharField(max_length = 200, blank = True, null = True )
    quantity = models.CharField(max_length = 200, blank = True, null = True)
    unit_price = models.CharField(max_length = 200, blank = True, null = True)
    supplier_info = models.ForeignKey(PurchasedMaster, on_delete=models.CASCADE , blank = True, null = True)
    note = models.TextField(blank = True, null = True)
    created_dt = models.DateTimeField(blank=True , null= True , default= datetime.datetime.now())



class SalesMaster(models.Model):
    fk_product = models.ForeignKey(InventoryMaster, on_delete=models.CASCADE , blank = True, null = True)
    company_name = models.CharField(max_length = 200, blank = True, null = True)
    mobile_no = models.CharField(max_length = 200, blank = True, null = True)
    phone_no = models.CharField(max_length = 200, blank = True, null = True)
    email = models.CharField(max_length = 200, blank = True, null = True)
    country = models.ForeignKey(CountryMaster, on_delete=models.CASCADE , blank = True, null = True )
    state = models.ForeignKey(StateMaster, on_delete=models.CASCADE , blank = True, null = True )
    cities = models.ForeignKey(CityMaster, on_delete=models.CASCADE , blank = True, null = True )
    postal_code = models.CharField(max_length = 200, blank = True, null = True)
    fax_no = models.CharField(max_length = 200, blank = True, null = True)
    created_dt = models.DateTimeField(blank=True , null= True , default= datetime.datetime.now())



class SalesProducts(models.Model):
    fk_sale = models.ForeignKey(SalesMaster, on_delete=models.CASCADE)
    fk_product = models.ForeignKey(InventoryMaster, on_delete=models.CASCADE)
    qty = models.CharField(max_length = 200, blank = True, null = True)
    total_amount = models.CharField(max_length = 200, blank = True, null = True)
    

