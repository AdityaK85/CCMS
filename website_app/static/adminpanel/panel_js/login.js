import { log, callAjax, fieldsValidator, removeError, sweetAlertMsg, showToastMsg } from '../../CommonJS/common.js';

// $("#users_list").addClass("mm-active");

$(document).ready(function () {
    $(document).bind("keypress", function (e) {
      if (e.keyCode == 13) {
        $("#btn_login").trigger("click");
      }
    });
});



window.Login_Admin = async function(this_) {

    var username = $('#username').val();
    var password = $('#admin_password').val();


    if (username == "") {

        showToastMsg("Username", "Please enter username", 'error');
        $('#username').focus()
    }
    else if (password == "") {
        
        showToastMsg("Password", "Please enter password", 'error');
        $('#password').focus()
    }
    else {

        var data = {

            'username': username,
            'password': password,
        }

        var response = await callAjax('/admin_login_aj/',data , this_ ,'Authenticating...' , 'successed');

        if (response.status == 1)
        {
            $(this_).html('Login successed')
            $(this_).css('background', 'green')
            window.location.href = "/Dashboard" 
        }
        else if (response.status == 0)
        {
            showToastMsg("Error", response.msg, 'error')
            $(this_).html('Login Failed')
            $(this_).css('background', 'red')
        }
        else{
            showToastMsg("Error", 'Something Went Wrong', 'error')
        }
    }
  }





  window.logout = async function(){
    var preference = await sweetAlertMsg('Confirm Logout', "Do you want to logout from application?", 'question', 'cancel', 'Yes', )
    if (preference){
        location.href = '/logout_admin'
    }
  }