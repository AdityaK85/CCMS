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