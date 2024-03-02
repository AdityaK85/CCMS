import { log, callAjax, fieldsValidator, removeError, sweetAlertMsg, showToastMsg } from '../../CommonJS/common.js';
log('::: File found')
$('#recommendations_submenu_sidebar').addClass("mm-show");
window.removeError = removeError;

window.ClearAllFields = function() {
    var field = document.querySelectorAll('input', 'select')
    field.forEach(function(val){
        val.value = ''
    }) 
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