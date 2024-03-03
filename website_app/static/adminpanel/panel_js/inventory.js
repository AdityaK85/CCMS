import { log, callAjax, fieldsValidator, removeError, sweetAlertMsg, showToastMsg } from '../../CommonJS/common.js';
$('#recommendations_submenu_sidebar').addClass("mm-show");
window.removeError = removeError;

$("#cat_tbl").DataTable()

window.ClearAllFields = function() {
    var field = document.querySelectorAll('input', 'select')
    field.forEach(function(val){
        val.value = ''
    }) 
}


window.ServiceModel = function(sale_id , name){
    var obj_id = $("#service_id").val(sale_id)
    $("#service_field").val(name)
    var service_model = new bootstrap.Modal(document.getElementById("service_model"))
    service_model.show()
    service_model._element.addEventListener('hidden.bs.modal', function () {
        $('#obj_id').val('');
        $('#service_field').val('');
    });
}

window.SaveService = async function(){
    
    var obj_id = $("#service_id").val()
    var servi_field =  $("#service_field").val()

    if (servi_field.trim() == "") {
        showToastMsg("Error", "Field Required", 'error')
        servi_field.focus()
    }
    else{
        var data = {
            'id' : obj_id,
            'service_name' : servi_field
        }
        var response = await callAjax('/SaveService/', data)
        if (response.status == 1) {
            showToastMsg("Success", response.msg, 'success')
            $("#service_close").trigger('click')
            $("#service_div").html(response.rendered_str)
            $("#cat_tbl").DataTable()
        }
        else
        {
            showToastMsg("Error", 'Something went wrong', 'error')
        }
    }
}



window.generateRandomCode = function(prefix, length) {
    const randomNumber = Math.floor(Math.random() * Math.pow(10, length));
    $("#product_no").val(prefix + randomNumber.toString().padStart(length, '0'))
}

if ($('#prod_id').val() == ''){
    generateRandomCode('PRODUCTNO', 4)
}


window.SaveInventory = async function(this_ , val_id){
    var fields = await fieldsValidator(['product_name','product_no','category_name', 'model','quantity','unit_price','supplier_info' ])
    if (fields){
        var data = new FormData;
        for ( var key in fields) {
            data.append(key, fields[key])
        }
        data.append('note', $("#note").val())
        data.append('val_id',val_id)
        var response = await callAjax('/SaveInventory/' , data , this_ , 'Saving...' , 'Saved' , true )
        if (response.status == 1){
            showToastMsg('Success' , response.msg , 'success')
            await new Promise(resolve => setTimeout(resolve, 1500));
            location.reload()
            // ClearAllFields()
        }
    }
}




window.DeleteVendor = async function(id)
{
 
    var preference = await sweetAlertMsg('Delete Vendor', "Do you want to delete this Vendor?", 'question', 'cancel', 'Yes', )
   
    var data = {
        'id': id,
    }

    if (preference)
    {
        
        var response = await callAjax('/DeleteVendor/', data );
        if (response.status == 1)
        {
            showToastMsg('Sucess',response.msg, 'success'); 
			await new Promise(resolve => setTimeout(resolve, 1500)); 
			location.reload();
        }
        else 
        {
            showToastMsg("Error", response.msg, 'error');
        }
    } 
}

window.DeleteProduct = async function(id)
{
 
    var preference = await sweetAlertMsg('Delete Product', "Do you want to delete this Product?", 'question', 'cancel', 'Yes', )
   
    var data = {
        'id': id,
    }

    if (preference)
    {
        
        var response = await callAjax('/DeleteProduct/', data );
        if (response.status == 1)
        {
            showToastMsg('Sucess',response.msg, 'success'); 
			await new Promise(resolve => setTimeout(resolve, 1500)); 
			location.reload();
        }
        else 
        {
            showToastMsg("Error", response.msg, 'error');
        }
    } 
}

window.DeleteCategory = async function(id)
{
 
    var preference = await sweetAlertMsg('Delete Service', "Do you want to delete this Service?", 'question', 'cancel', 'Yes', )
   
    var data = {
        'id': id,
    }

    if (preference)
    {
        
        var response = await callAjax('/DeleteService/', data );
        if (response.status == 1)
        {
            showToastMsg('Sucess',response.msg, 'success'); 
			await new Promise(resolve => setTimeout(resolve, 1500)); 
			location.reload();
        }
        else 
        {
            showToastMsg("Error", response.msg, 'error');
        }
    } 
}
