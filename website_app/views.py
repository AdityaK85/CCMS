from django.shortcuts import render
from Project_utilty.decorators import *
from .models import *
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_control

def Login(request):
    return render(request, 'htmls/login.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def index(request , user):
    sevice_count = CategoryMaster.objects.count()
    inventory_count = InventoryMaster.objects.count()
    sales_count = SalesMaster.objects.count()
    purchase_count = PurchasedMaster.objects.count()
    comp_name = SalesMaster.objects.all().order_by('id')[:5]
    vendors = PurchasedMaster.objects.all().order_by('id')[:5]
    for i in vendors:
        i.purch_count = InventoryMaster.objects.filter(supplier_info_id = i.id).count()

    context = {
        'service_count' : sevice_count,
        'inven_count' : inventory_count,
        'sales_count' : sales_count,
        'purchase_count' : purchase_count, 
        'comp_name' : comp_name , 
        'vendors' : vendors
    }
    return render(request , 'htmls/index.html' , context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def AddInventory(request , user):  
    catgory_obj = CategoryMaster.objects.all().order_by('category_name')
    vendor_obj = PurchasedMaster.objects.all().order_by('-id')
    context = {'catgory_obj' : catgory_obj , 'vendor_obj' : vendor_obj }
    return render(request , 'htmls/add_product.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def Inventory(request  , user):
    inventory_obj = InventoryMaster.objects.all().order_by('-id')
    rendered = render_to_string('renderToString/r_t_s_inventory.html', {'inventory_obj' : inventory_obj})
    context = {'render_str' : rendered }
    return render(request , 'htmls/Inventory.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def Sales(request , user):
    country_list = CountryMaster.objects.all().order_by('-country_name')
    catgory_obj = CategoryMaster.objects.all().order_by('category_name')
    sale_obj = SalesMaster.objects.all().order_by('-id')
    for i in sale_obj:
        i.success = True if SalesProducts.objects.filter(fk_sale_id = i.id).exists() else False
    rendered = render_to_string('renderToString/r_t_s_sales.html', {'sale_obj' : sale_obj})
    context = {'render_str' : rendered , 'catgory_obj' : catgory_obj , 'country_list': country_list}
    return render(request , 'htmls/Blog.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def Invoice(request , user, id):
    invoice_obj = SalesMaster.objects.filter(id = id).last()
    product_obj = SalesProducts.objects.filter(fk_sale_id = id)
    total_amount = 0

    for product in product_obj:
        total_amount += float(product.total_amount) 
    return render(request , 'htmls/invoice.html', {'invoice_obj': invoice_obj , 'product_obj': product_obj , 'total_amount': total_amount})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def Purchased(request  , user):
    return render(request , 'htmls/Voting.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def Categories(request  , user):
    cat_obj = CategoryMaster.objects.all().order_by('-id')
    rendered = render_to_string('renderToString/r_t_s_category.html', {'cat_obj' : cat_obj})
    context = {'render_str' : rendered }
    return render(request , 'htmls/Categories.html' , context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def editVendor(request , user ,id):
    purch_obj = PurchasedMaster.objects.get(id = id)
    return render(request , 'htmls/Voting.html', {'purch_obj':purch_obj})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def editProduct(request  , user, id):
    prod_obj = InventoryMaster.objects.get(id = id)
    catgory_obj = CategoryMaster.objects.all().order_by('category_name')
    vendor_obj = PurchasedMaster.objects.all().order_by('-id')
    context = {'catgory_obj' : catgory_obj , 'vendor_obj' : vendor_obj , 'prod_obj':prod_obj}
    return render(request , 'htmls/add_product.html', context)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@handle_admin_page_exception
def ManageVendors(request , user):
    vendor_obj = PurchasedMaster.objects.all().order_by('-id')
    for i in vendor_obj:
        total_purch_amt = 0
        i.total_amt = 0
        if InventoryMaster.objects.filter(supplier_info_id=i.id).exists():
            supplier_obj = InventoryMaster.objects.filter(supplier_info_id=i.id).values('quantity', 'unit_price')
            total = sum([int(item['quantity']) * float(item['unit_price']) for item in supplier_obj])
            i.total_amt = total
            total_purch_amt += total
            
    rendered = render_to_string('renderToString/r_t_s_manage_vendor.html', {'vendor_obj' : vendor_obj})
    context = {'render_str' : rendered }
    return render(request , 'htmls/Vendors.html', context)



import pandas as pd
from django.http import JsonResponse
import traceback
from django.conf import settings

def UploadCountries():
    try:
        # StateMaster.objects.all().delete()
        # CityMaster.objects.all().delete()
        
        data = pd.read_excel(f'{settings.BASE_DIR}/state_city_files/countries.xlsx', engine='openpyxl')
        
        data = data.to_dict('records')
        # print(":::: data ::::", data)
        for i in data:
            if not CountryMaster.objects.filter(country_name = i['name']).exists():
                CountryMaster.objects.create(country_name = i['name']  )
                print(":::: done :::;", i['name'])
            
        return JsonResponse({"status":"Success"})
    except:
        traceback.print_exc()


def UploadStateCity():
    try:
        # StateMaster.objects.all().delete()
        # CityMaster.objects.all().delete()
        
        data = pd.read_excel(f'{settings.BASE_DIR}/state_city_files/state.xlsx', engine='openpyxl')
        
        data = data.to_dict('records')
        for i in data:
            if not StateMaster.objects.filter(name = i['name']).exists():
                StateMaster.objects.create(name = i['name'] , country_id = i['country_id'] )
                print(":::: done :::;", i['name'])
            
        return JsonResponse({"status":"Success"})
    except:
        traceback.print_exc()



def Upload_Cities():
    try:
        data = pd.read_excel(f'{settings.BASE_DIR}/state_city_files/city.xlsx', engine='openpyxl')
        
        data = data.to_dict('records')
        for i in data:
            if not CityMaster.objects.filter(name = i['name'] , state_id_id = i['state_id']).exists():
                CityMaster.objects.create(name = i['name'], state_id_id = i['state_id'])
                print(':::DONE :::', i['name'])

        return JsonResponse({"status":"Success"})
    except:
        traceback.print_exc()
        return JsonResponse({'status':'error'})


# Upload_Cities()