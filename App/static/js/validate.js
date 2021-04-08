// check password when register
$(document).ready(function () {
    //$("form[name='register']").validate({
        //password: {
            //min
        //}
    //})
    $("#register_btn").click(function (){
        var password = $("#password").val();
        var confirmPassword = $("#confirmPassword").val();
        if(password != confirmPassword){
            $("#mes_err_pass2").removeClass("display_none");
            $("#confirmPassword").focus();
            return false;                 
        }else{
            return true;        
        }
    });
});