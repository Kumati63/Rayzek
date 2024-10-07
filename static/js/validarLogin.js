$(document).ready(function() {
    $(document).on("contextmenu", function(e) {
        e.preventDefault();
    });

    // Ocultar mensajes y deshabilitar botón de envío al inicio
    $("#no").hide();
    $("#yes").hide();
    $("#submit-button").prop("disabled", true);
    toggleStyles(true);

    // Validar email y contraseña al perder el foco
    $('#email, #contrasena').on("blur", checkFormValidity);

    $('#email').on("blur", function() {
        if ($(this).val().length === 0) {
            $(this).css("border-color", "red");
            swal("Debe ingresar un Email");
        } else {
            $(this).css("border-color", "white");
            validaremail(); // Llamar validación del email
        }
    });

    $('#contrasena').on("blur", function() {
        if ($(this).val().length === 0) {
            $(this).css("border-color", "red");
            swal("Debe ingresar una contraseña");
        } else {
            $(this).css("border-color", "white");
        }
    });
});

// Función que verifica si ambos campos están llenos para habilitar el botón
function checkFormValidity() {
    const emailVal = $('#email').val().length > 0;
    const contrasenaVal = $('#contrasena').val().length > 0;

    if (emailVal && contrasenaVal) {
        $("#submit-button").prop("disabled", false);
        toggleStyles(false); // Habilitar botón con estilos normales
    } else {
        $("#submit-button").prop("disabled", true);
        toggleStyles(true);  // Deshabilitar botón
    }
}

function validar_login() {
    if (document.form.email.value == "") {
        swal("Debe ingresar un Email");
        document.form.email.focus();
        return false;
    }

    if (document.form.contrasena.value == "") {
        swal("Debe ingresar una contraseña");
        document.form.contrasena.focus();
        return false;
    }

    document.form.submit();
}

function validaremail() {
    $.ajax({
        type: "POST",
        url: 'functions/validaremail.php',
        data: "email-usu=" + $("#email").val(),
        success: function(response) {
            if (response == 0) {
                $("#no").show();
                $("#yes").hide();
                $('#email').css("border-color", "red");
            } else {
                $("#no").hide();
                $("#yes").show();
                $('#email').css("border-color", "green");
                checkFormValidity(); // Llamar a la función para verificar si todo es válido
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
