import { log, callAjax, fieldsValidator, removeError, sweetAlertMsg, showToastMsg, validateFile } from '../../CommonJS/common.js';

$('#recommendations_submenu_sidebar').addClass("mm-show");
window.removeError = removeError;

window.ClearAllFields = function() {
    var field = document.querySelectorAll('input', 'select')
    field.forEach(function(val){
        val.value = ''
    }) 
}



window.show_qty_price_field = function(val_id , button){
    var field = $(`#${val_id}`);
    field.toggle();
    var icon = $(button).find('i');
    if (field.is(':visible')) {
        icon.removeClass('fa-plus').addClass('fa-minus');
    } else {
        icon.removeClass('fa-minus').addClass('fa-plus');
    }
}



window.getStates = async function(id , type){
  
    var data = {"id":id , 'type' : type }
    var response = await callAjax('/get_addr/', data);
    if (response.status == 1) {

        var renderList = response.list;
        var selectField = document.getElementById(type);
        selectField.innerHTML = '';

        if (renderList.length > 0){

            renderList.forEach(function(state) {
                var option = document.createElement('option');
                option.value = state.id;  
                option.text = state.name; 
                selectField.appendChild(option);
            });
        } else {
            var selectField = document.getElementById(type);
            selectField.innerHTML = `<option value="">Not Found This ${type}</option>`;
        }
            

    }
    else{

        var selectField = document.getElementById(type);
        selectField.innerHTML = `<option value="">Select ${type}</option>`;
    }
}


window.getInventory = async function(){
    var category_id = $("#category_id").val()
    var product_no = $("#product_no").val()
    var product_name = $("#product_name").val()
    var data = {
        'cat_id' : category_id , 
        'product_no' : product_no , 
        'product_name' : product_name , 
    }
    var response = await callAjax('/GetInventory/' , data )
    if (response.status == 1){
        $("#inventory_div").html(response.render_str)
    }
     
}

window.SaveSales = async function(this_){
    var fields = await fieldsValidator(['company_name','mobile_no','email', 'country','state','cities','postal_code' ])
    var obj_id = $("#obj_id").val()
    if (fields){
        var data = new FormData;
        for ( var key in fields) {
            data.append(key, fields[key])
        }
        data.append('phone_no', $("#phone_no").val())
        data.append('fax_no', $("#fax_no").val())
        data.append('val_id',obj_id)
        var response = await callAjax('/SaveSales/' , data , this_ , 'Saving...' , 'Saved' , true )
        if (response.status == 1){
            showToastMsg('Success' , response.msg , 'success')
            await new Promise(resolve => setTimeout(resolve, 1500));
            $("#obj_id").val(response.obj_id)
            document.getElementById('add_products').style.display = 'block'
        }
    }
}


window.getQty = function(input_qty , unit_price , show_total_price){
    var total_amt = parseInt(input_qty) * parseFloat(unit_price)
    $(`#${show_total_price}`).val(total_amt)
}



window.sale_product = async function(prod_id , qty_field, total_amt_field , on_update){
    var qty = $(`#${qty_field}`).val()
    var price = $(`#${total_amt_field}`).val()
    var obj_id = $("#obj_id").val()
    var category_id = $("#category_id").val()
    var product_no = $("#product_no").val()
    var product_name = $("#product_name").val()

    if (qty.trim() == "" ){
        showToastMsg('Error', 'Please Enter Quantity', 'error')
        qty.focus()
    }
    else if (price.trim() == 'NaN' || price.trim() == '' ){
        showToastMsg('Error', 'Please Enter Price', 'error')
        qty.focus()
    }
    else{

        var data = {
            'qty': qty,
            'price':price,
            'prod_id':prod_id,
            'sale_id':obj_id,
            'cat_id' : category_id , 
            'product_no' : product_no , 
            'product_name' : product_name ,
        }

        var response = await callAjax('/Add_Prod_On_Sale/' , data )
        if (response.status == 1){
            $("#inventory_div").html(response.render_str)
            showToastMsg('Success' , response.msg , 'success')
        }

    }

}