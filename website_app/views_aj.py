from django.http import JsonResponse
from Project_utilty.decorators import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string


@csrf_exempt
@handle_ajax_exception
def SaveInventory(request):
    data = request.POST.dict()
    val_id = request.POST.get('val_id')
    data.pop('val_id')
    data.pop('category_name')
    if val_id != "" and InventoryMaster.objects.filter(id = val_id).exists() :
        InventoryMaster.objects.filter(id = val_id).update(**data)
        obj = InventoryMaster.objects.get(id = val_id)
        obj.fk_category_id = request.POST.get('category_name')
        obj.save()
    else:
        obj = InventoryMaster.objects.create(**data)
        obj.fk_category_id = request.POST.get('category_name')
        obj.save()
    send_data = {'status': 1 , 'msg' : f'Inventory { 'Modified' if val_id != '' else 'Saved' }   Successfully' }
    return JsonResponse(send_data)

@csrf_exempt
@handle_ajax_exception
def SaveSales(request):
    data = request.POST.dict()
    val_id = request.POST.get('val_id')
    data.pop('val_id')
    data.pop('country')
    data.pop('state')
    data.pop('cities')
    if val_id != "" and SalesMaster.objects.filter(id = val_id).exists() :
        SalesMaster.objects.filter(id = val_id).update(**data)
        obj = SalesMaster.objects.get(id = val_id)
        obj.save()
    else:
        obj = SalesMaster.objects.create(**data)
        obj.country_id = request.POST.get('country')
        obj.state_id = request.POST.get('state')
        obj.cities_id = request.POST.get('cities')
        obj.save()
    send_data = {'status': 1 , 'obj_id' : obj.id ,  'msg' : f'Details { 'Modified' if val_id != '' else 'Saved' }  ' }
    return JsonResponse(send_data)

@csrf_exempt
@handle_ajax_exception
def GetInventory(request):
    cat_id = request.POST.get('cat_id')
    product_no = request.POST.get('product_no')
    product_name = request.POST.get('product_name')
    get_obj = InventoryMaster.objects.all().order_by('-id')
    if cat_id != "":
        get_obj = get_obj.filter(fk_category_id = cat_id).order_by('-id')
    if product_no != "":
        get_obj = get_obj.filter(product_no = product_no).order_by('-id')
    if product_name != "":
        get_obj = get_obj.filter(product_name__icontains = product_name).order_by('-id')
    rendered = render_to_string('renderToString/r_t_s_get_inventory.html', {'get_obj' : get_obj})
    return JsonResponse({'status': 1 , 'render_str': rendered })


@csrf_exempt
@handle_ajax_exception
def Add_Prod_On_Sale(request):
    cat_id = request.POST.get('cat_id')
    product_no = request.POST.get('product_no')
    product_name = request.POST.get('product_name')
    qty = request.POST.get('qty')
    price = request.POST.get('price')
    prod_id = request.POST.get('prod_id')
    sale_id = request.POST.get('sale_id')
    msg = 'Something went wrong !Please try again later'

    if (sale_id != None ):
        if SalesProducts.objects.filter(fk_sale_id = sale_id , fk_product_id = prod_id).exists():
            SalesProducts.objects.filter(fk_sale_id = sale_id , fk_product_id = prod_id).update(qty = qty , total_amount = price)
            msg = "Product List Updated"
        else:
            SalesProducts.objects.create(fk_sale_id = sale_id , fk_product_id = prod_id, qty = qty , total_amount = price)
            msg = "Product Added To Sale List"


    get_obj = InventoryMaster.objects.all().order_by('-id')
    if cat_id != "":
        get_obj = get_obj.filter(fk_category_id = cat_id).order_by('-id')
    if product_no != "":
        get_obj = get_obj.filter(product_no = product_no).order_by('-id')
    if product_name != "":
        get_obj = get_obj.filter(product_name__icontains = product_name).order_by('-id')

    for i in get_obj:
        i.update_id = False 
        i.prev_qty = None
        i.prev_price = None
        if SalesProducts.objects.filter(fk_sale_id = sale_id , fk_product_id = i.id  ).exists():
            sale_obj = SalesProducts.objects.get(fk_sale_id = sale_id , fk_product_id = i.id  )
            i.update_id = True 
            i.prev_qty = sale_obj.qty
            i.prev_price = sale_obj.total_amount
        
    rendered = render_to_string('renderToString/r_t_s_get_inventory.html', {'get_obj' : get_obj})
    return JsonResponse({'status': 1 , 'msg': msg , 'render_str': rendered })




@csrf_exempt
@handle_ajax_exception
def get_addr(request):
    id = request.POST.get('id')
    type = request.POST.get('type')
    if id != '' and type == 'state' :
        states = StateMaster.objects.filter(country_id=id).values('id', 'name') 
        send_data = {"status": 1, "list": list(states)}
    elif id != '' and type == 'cities' :
        states = CityMaster.objects.filter(state_id=id).values('id', 'name') 
        send_data = {"status": 1, "list": list(states)}
    else:
        send_data = {"status": 0 , "msg": 'error'}
    return JsonResponse(send_data)