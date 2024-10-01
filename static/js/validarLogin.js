$(function() {
    $(document).ready(function() {
        $(document).on("contextmenu", function(e) {
            e.preventDefault();
        });
    });
    $("#no").hide();
    $("#yes").hide();
    $("#submit-button").prop("disabled",true);
    toggleStyles(true);
    $('#email').on( "blur", function() 
    {
        if ($(this).val().length === 0) {
            $(this).css("border-color","red"); ;
        }else{
            $(this).css("border-color","white");
            validaremail();
        }
    });
    $('#contrasena').on( "blur", function() {
        if ($(this).val().length === 0) {
            $(this).css("border-color","red");
        }else{
            $(this).css("border-color","white");
        }
    });
});

function validar_login(){
    
    if(document.form.email.value==""){
        swal("Debe ingresar un Email");
        document.form.email.focus();
        return false;
    }

    if (document.form.contrasena.value==""){
        swal("Debe ingresar una contrasena");
        document.form.contrasena.focus();
        return false;
    }

    document.form.submit();
}

function validaremail()
{
    $.ajax({
    type: "POST",
    url: 'functions/validaremail.php',
    data: "email-usu="+$("#email").val(),
    success: function(response)
        {
            if (response==0){
                $("#no").show();
                $("#yes").hide();
                $('#email').css("border-color","red");
            }else{
                $("#no").hide();
                $("#yes").show();
                $('#email').css("border-color","green"); 
                $("#submit-button").prop("disabled",false);
                toggleStyles(false);
            }
        }
    });
    
}
function toggleStyles(applyStyles) {
    if (applyStyles) {
        $("#submit-button").css({
            "background-color": "gray",
            "color": "black",
            "border": "none"
        });
    } else {
        $("#submit-button").removeAttr("style");
    }
}