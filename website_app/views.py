from django.shortcuts import render
from Project_utilty.decorators import *
from .models import *
from django.template.loader import render_to_string


def index(request):
    return render(request , 'htmls/index.html')

def AddInventory(request):
    catgory_obj = CategoryMaster.objects.all().order_by('category_name')
    context = {'catgory_obj' : catgory_obj}
    return render(request , 'htmls/add_product.html', context)

def Inventory(request):
    inventory_obj = InventoryMaster.objects.all().order_by('-id')
    rendered = render_to_string('renderToString/r_t_s_inventory.html', {'inventory_obj' : inventory_obj})
    context = {'render_str' : rendered }
    return render(request , 'htmls/Inventory.html', context)

def Sales(request):
    country_list = CountryMaster.objects.all().order_by('-country_name')
    catgory_obj = CategoryMaster.objects.all().order_by('category_name')
    sale_obj = SalesMaster.objects.all().order_by('-id')
    for i in sale_obj:
        i.success = True if SalesProducts.objects.filter(fk_sale_id = i.id).exists() else False
    rendered = render_to_string('renderToString/r_t_s_sales.html', {'sale_obj' : sale_obj})
    context = {'render_str' : rendered , 'catgory_obj' : catgory_obj , 'country_list': country_list}
    return render(request , 'htmls/Blog.html', context)

def Invoice(request , id):
    invoice_obj = SalesMaster.objects.filter(id = id).last()
    product_obj = SalesProducts.objects.filter(fk_sale_id = id)
    total_amount = 0

    for product in product_obj:
        total_amount += float(product.total_amount) 
    return render(request , 'htmls/invoice.html', {'invoice_obj': invoice_obj , 'product_obj': product_obj , 'total_amount': total_amount})


def Votings(request):
    return render(request , 'htmls/Voting.html')



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