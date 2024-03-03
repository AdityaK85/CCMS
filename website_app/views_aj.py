from django.http import JsonResponse
from Project_utilty.decorators import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string


@csrf_exempt
def admin_login_aj(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    if Admin.objects.filter(username = username ,  password = password).exists():
        user = Admin.objects.get(username = username ,  password = password )
        request.session['admin_user_id'] = user.id
        request.session['admin_user_type'] = "admin"
        return JsonResponse({"status": 1, "msg": "Success"})
    else:
        return JsonResponse({"status": 0, "msg": "Invalid Credentials"})



@csrf_exempt
def logout_admin(request):
    try :
        if request.session.get("admin_user_id") :
            del request.session['admin_user_id']
            del request.session['admin_user_type']
    except :
        traceback.print_exc()
    return redirect('/')


@csrf_exempt
@handle_ajax_exception
def SaveInventory(request):
    data = request.POST.dict()
    val_id = request.POST.get('val_id')
    data.pop('val_id')
    data.pop('category_name')
    data.pop('supplier_info')
    if val_id != "" and InventoryMaster.objects.filter(id = val_id).exists() :
        InventoryMaster.objects.filter(id = val_id).update(**data)
        obj = InventoryMaster.objects.get(id = val_id)
        obj.fk_category_id = request.POST.get('category_name')
        obj.supplier_info_id = request.POST.get('supplier_info')
        obj.save()
        msg = "Inventory Modified"
    else:
        obj = InventoryMaster.objects.create(**data)
        obj.fk_category_id = request.POST.get('category_name')
        obj.supplier_info_id = request.POST.get('supplier_info')
        obj.save()
        msg = "Inventory Saved"
    send_data = {'status': 1 , 'msg' : msg }
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
def SavePurchased(request):
    data = request.POST.dict()
    val_id = request.POST.get('val_id')
    data.pop('val_id')
    if val_id != "" and PurchasedMaster.objects.filter(id = val_id).exists() :
        PurchasedMaster.objects.filter(id = val_id).update(**data)
        obj = PurchasedMaster.objects.get(id = val_id)
        obj.save()
    else:
        obj = PurchasedMaster.objects.create(**data)
    send_data = {'status': 1 , 'obj_id' : obj.id ,  'msg' : f'Vendor Details { 'Modified' if val_id != '' else 'Saved' }  ' }
    return JsonResponse(send_data)

@csrf_exempt
@handle_ajax_exception
def SaveService(request):
    id = request.POST.get('id')
    service_name = request.POST.get('service_name')

    if id != "" and CategoryMaster.objects.filter(id = id).exists() :
        CategoryMaster.objects.filter(id = id).update(category_name = service_name)
    else:
        obj = CategoryMaster.objects.create(category_name = service_name)
    
    cat_obj = CategoryMaster.objects.all().order_by('-id')
    rendered = render_to_string('renderToString/r_t_s_category.html', {'cat_obj' : cat_obj})
    send_data = {'status': 1 , 'rendered_str' : rendered ,  'msg' : f'Service { 'Modified' if id != '' else 'Saved' }  ' }
    return JsonResponse(send_data)

@csrf_exempt
@handle_ajax_exception
def GetInventory(request):
    sale_id = request.POST.get('sale_id')
    cat_id = request.POST.get('cat_id')
    product_no = request.POST.get('product_no')
    product_name = request.POST.get('product_name')
    get_obj = InventoryMaster.objects.order_by('-id')
    if cat_id != "":
        get_obj = get_obj.filter(fk_category_id = cat_id).order_by('-id')
    if product_no != "":
        get_obj = get_obj.filter(product_no = product_no).order_by('-id')
    if product_name != "":
        get_obj = get_obj.filter(product_name__icontains = product_name).order_by('-id')
    if get_obj:
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


@csrf_exempt
@handle_ajax_exception
def DeleteVendor(request):
    id = request.POST.get('id')
    PurchasedMaster.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg':'Vendor Deleted'})

@csrf_exempt
@handle_ajax_exception
def DeleteSale(request):
    id = request.POST.get('id')
    SalesMaster.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg':'Record Deleted'})


@csrf_exempt
@handle_ajax_exception
def DeleteService(request):
    id = request.POST.get('id')
    CategoryMaster.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg':'Service Deleted'})


@csrf_exempt
@handle_ajax_exception
def DeleteProduct(request):
    id = request.POST.get('id')
    InventoryMaster.objects.filter(id = id).delete()
    return JsonResponse({'status':1, 'msg':'Record Deleted'})

@csrf_exempt
@handle_ajax_exception
def Remove_Prod_From_List(request):
    sale_id = request.POST.get('sale_id')
    id = request.POST.get('id')
    cat_id = request.POST.get('cat_id')
    product_no = request.POST.get('product_no')
    product_name = request.POST.get('product_name')
    SalesProducts.objects.filter(fk_product_id = id , fk_sale_id = sale_id ).delete()
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
    return JsonResponse({'status':1, 'msg':'Product List Updated' , 'render_str': rendered })