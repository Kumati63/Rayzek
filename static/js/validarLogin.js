$(document).ready(function() {
    $(document).on("contextmenu", function(e) {
        e.preventDefault();
    });

    // Ocultar mensajes y deshabilitar botón de envío al inicio
    $("#no").hide();
    $("#yes").hide();
    $("#submit-button").prop("disabled", true);
    toggleStyles(true);

    // Al cargar la página, verifica si hay datos guardados en localStorage
    if (localStorage.getItem('remember') === 'true') {
        $('#email').val(localStorage.getItem('email')); // Rellenar el email guardado
        $('#forget').prop('checked', true); // Mantener el checkbox marcado
    }

    // Evento cuando el usuario envía el formulario o marca/desmarca el checkbox
    $('#forget').on('change', function() {
        if ($(this).is(':checked')) {
            // Si el checkbox está marcado, guardar el email y la contraseña en localStorage
            localStorage.setItem('remember', 'true');
            localStorage.setItem('email', $('#email').val());
        } else {
            // Si el checkbox está desmarcado, borrar los datos de localStorage
            localStorage.removeItem('remember');
            localStorage.removeItem('email');
        }
    });

    // Validar email y contraseña al perder el foco
    $('#email, #contrasena').on("blur", checkFormValidity);

    $('#email').on("blur", function() {
        const emailValue = $(this).val();
        if (emailValue.length === 0) {
            $(this).css("border-color", "red");
            swal("Debe ingresar un email");
        } else if (!validateEmail(emailValue)) {
            $(this).css("border-color", "red");
            swal("Email inválido. Asegúrese de que tenga el formato correcto.");
        } else {
            $(this).css("border-color", "white");
        }

        // Realizar la verificación del email con AJAX
        $.ajax({
            url: verificarEmailUrl,  // Usamos la variable que tiene la URL correcta
            data: {
                'email': emailValue
            },
            dataType: 'json',  // Esperamos una respuesta JSON
            success: function(data) {
                console.log("Respuesta de AJAX:", data);  // Verifica qué devuelve el servidor
                if (!data.disponible) {
                    $('#email').css("border-color", "green");
                    swal("El Email está registrado.");
                } else {
                    $('#email').css("border-color", "red");
                    swal("El Email no está registrado.");
                    $("#submit-button").prop("disabled", true);
                }
            },
            error: function(xhr, status, error) {
                // Este bloque se ejecuta si hay un error en la solicitud AJAX
                console.error("Error en la solicitud AJAX:", status, error);
                $('#email').css("border-color", "red");
                swal("Ocurrió un error al verificar el correo electrónico.");
            }
        });
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

function validateEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
}
