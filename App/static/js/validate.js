// check password when register
$(document).ready(function () {
    jQuery.validator.addMethod("password_check",
        function(value, element, param) {
            if (this.optional(element)) {
                return true;
            } else if (!/[a-zA-Z]/.test(value)) {
                return false;
            } else if (!/[0-9]/.test(value)) {
                return false;
            }
            return true;
        },
        "Mật khẩu phải bao gồm cả chữ và số"
    );
    jQuery.validator.addMethod("specialChar_check",
        function(value, element, param) {
            if (this.optional(element)) {
                return true;
            } else if (/[{}|~`"'[\]+,:;=?|'<>.^*()-]/.test(value)) {
                return false;
            }
            return true;
        },
    );

    $('#form-register').validate({
        rules: {
            email: {
                required: true
            },
            userName: {
                required: true,
                maxlength: 25,
                specialChar_check: true
            },
            password: {
                required: true,
                minlength: 8,
                maxlength: 20,
                password_check: true,
                specialChar_check: true
            },
            confirmPassword: {
                equalTo: "#password"
            }
        },
        messages: {
            email: {
                required: "Email không được bỏ trống"
            },
            userName: {
                required: "Tên người dùng không được bỏ trống",
                maxlength: "Tên người dùng tối đa 25 ký tự",
                specialChar_check: "Tên người dùng không được phép có ký tự đặc biệt"
            },
            password: {
                required: "Mật khẩu không được bỏ trống",
                minlength: "Mật khẩu phải ít nhất có 8 ký tự",
                maxlength: "Mật khẩu tối đa 25 ký tự",
                specialChar_check: "Mật khẩu không được phép có ký tự đặc biệt"
            },
            confirmPassword: {
                equalTo: "Mật khẩu không khớp"
            }
        }
    });
    $('#form-change-pass').validate({
        rules: {
            currentPassword: {
                required: true
            },
            newPassword: {
                required: true,
                minlength: 8,
                maxlength: 20,
                password_check: true,
                specialChar_check: true
            },
            confirmPassword: {
                equalTo: "#newPassword"
            }
        },
        messages: {
            currentPassword: {
                required: "Mật khẩu hiện tại không được bỏ trống",
            },
            newPassword: {
                required: "Mật khẩu mới không được bỏ trống",
                minlength: "Mật khẩu mới phải ít nhất có 8 ký tự",
                maxlength: "Mật khẩu mới tối đa 25 ký tự",
                specialChar_check: "Mật khẩu mới không được phép có ký tự đặc biệt"
            },
            confirmPassword: {
                equalTo: "Mật khẩu không khớp"
            }
        }
    });
});
