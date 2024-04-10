import { log, callAjax, fieldsValidator, removeError, sweetAlertMsg, showToastMsg } from '../../CommonJS/common.js';

$('#recommendations_submenu_sidebar').addClass("mm-show");
window.removeError = removeError;

window.ClearAllFields = function() {
    var field = document.querySelectorAll('input', 'select')
    field.forEach(function(val){
        val.value = ''
    }) 
}


window.generateRandomCode = function(prefix, length) {
    const randomNumber = Math.floor(Math.random() * Math.pow(10, length));
    $("#vendor_code").val(prefix + randomNumber.toString().padStart(length, '0'))
}

if ($('#obj_id').val() == ""){
    generateRandomCode('VENDOR2024', 4)
}

window.SavePurchased = async function(this_, val_id){
    var fields = await fieldsValidator(['vendor_code','vendor_name','purchased_dt', 'phone','mail'])
    if (fields){
        var data = new FormData;
        for ( var key in fields) {
            data.append(key, fields[key])
        }
        data.append('other_link', $("#other_link").val())
        data.append('note', $("#note").val())
        data.append('val_id',val_id)
        var response = await callAjax('/SavePurchased/' , data , this_ , 'Saving...' , 'Saved' , true )
        if (response.status == 1){
            showToastMsg('Success' , response.msg , 'success')
            await new Promise(resolve => setTimeout(resolve, 1500));
            location.reload()
            // ClearAllFields()
        }
    }
}


var current_dt = new Date();
var Today_dt = current_dt.toISOString().split('T')[0];
$('#from_dt').attr('max', Today_dt);

$('#from_dt').change(function()
{
    var from_date = $("#from_dt").val();
    $('#to_dt').attr('min',from_date)
});


$('#to_dt').change(function()
{
    var to_date = $("#to_dt").val();
    $('#from_dt').attr('max',to_date)
});




$('#from_dt_inven').attr('max', Today_dt);

$('#from_dt_inven').change(function()
{
    var from_date = $("#from_dt_inven").val();
    $('#to_dt_inven').attr('min',from_date)
});


$('#to_dt_inven').change(function()
{
    var to_date = $("#to_dt_inven").val();
    $('#from_dt_inven').attr('max',to_date)
});


window.filter_sale_report = async function(this_){
    var from_dt = $("#from_dt").val()
    var to_dt = $("#to_dt").val()
    
    log(from_dt , to_dt)
    if (from_dt.trim() != '' &&  to_dt.trim() == '') {
        showToastMsg("Error", "Please enter To date.", 'error');
        $("#to_dt").focus()
    } 
    else if (from_dt.trim() == '' &&  to_dt.trim() != '') {
        showToastMsg("Error", "Please enter From date.", 'error');
        $('#from_dt').focus()
    }
    else {
        var data = {
            'from_dt':from_dt,
            'to_dt':to_dt,
        }
        var response = await callAjax('/filter_report/', data , this_ , 'Filtering...', 'Filtered');
        if (response.status == 1) {
            $("#total_rev").html(response.total_rev)
        }
        else {
            showToastMsg("Error", 'Something Went Wrong...', 'error')
        }   
    }

}


window.filter_inventory_report = async function(this_){
    var from_dt = $("#from_dt_inven").val()
    var to_dt = $("#to_dt_inven").val()

    log(from_dt , to_dt)
    if (from_dt.trim() != '' &&  to_dt.trim() == '') {
        showToastMsg("Error", "Please enter To date.", 'error');
        $("#to_dt").focus()
    } 
    else if (from_dt.trim() == '' &&  to_dt.trim() != '') {
        showToastMsg("Error", "Please enter From date.", 'error');
        $('#from_dt').focus()
    }
    else {
        var data = {
            'from_dt':from_dt,
            'to_dt':to_dt,
        }
        var response = await callAjax('/filter_report/', data , this_ , 'Filtering...', 'Filtered');
        if (response.status == 1) {
            $("#inventory_rev").html(response.inventory_rev)
        }
        else {
            showToastMsg("Error", 'Something Went Wrong...', 'error')
        }   
    }

}