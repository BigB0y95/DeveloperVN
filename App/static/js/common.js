// check password when register
$(document).ready(function () {
    $("#register_btn").click(function (){
        var password = $("#password").val();
        var confirmPassword = $("#confirmPassword").val();
        if(password.length < 6 || password.length > 20){
            $("#mes_err_pass1").removeClass("display_none");
            $("#mes_err_pass2").addClass("display_none");
            return false;
        }else{
            if(password == confirmPassword){
                return true;
            }else{
                $("#mes_err_pass2").removeClass("display_none");
                $("#mes_err_pass1").addClass("display_none");
                return false;           
            }
        }     
    });
});