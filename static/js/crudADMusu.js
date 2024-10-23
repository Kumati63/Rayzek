$(function() {
    $(document).ready(function() {
        $(document).on("contextmenu", function(e) {
            e.preventDefault();
        });
    });
    
    // Deshabilitar el botón de envío al inicio
    $("#submit-button").prop("disabled", true);
    toggleStyles(true);

    // Verificar cada campo cuando pierda el foco o cambie
    $('#nombre, #email, #contrasena, #contrasena2').on("blur", checkFormValidity);
    $('#File').on("change", checkFormValidity);

    $('#nombre').on( "blur", function() 
    {
        if ($(this).val().length === 0) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe ingresar un Nombre");
        }else{
            $(this).css("border-color","white");
        }
    });

    $('#nombre').on('input', function() {
        var sanitizedValue = $(this).val().replace(/[^a-z ]/gi, '');
        $(this).val(sanitizedValue);
    });

    $('#email').on("blur", function() {
        const emailValue = $(this).val();
        if (emailValue.length === 0) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe ingresar un email");
        } else if (!validateEmail(emailValue)) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Email inválido. Asegúrese de que tenga el formato correcto.");
        } else {
            $(this).css("border-color", "white");
        }
    });

    $('#contrasena').on( "blur", function() {
        if ($(this).val().length === 0) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe ingresar una contraseña");
        }else{
            $(this).css("border-color","white");
        }
    });

    //javascript para prohibir ciertos caracteres
    $('#contrasena').on('input', function() {
        var sanitizedValue = $(this).val().replace(/[^a-z0-9 !#$%&()*+-./:;=?@[\]{|}~]/gi, '');
        $(this).val(sanitizedValue);
    });

    $('#contrasena2').on("blur", function() {
        if ($(this).val().length === 0) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe ingresar la repetición de la contraseña");
        } else {
            // Verificar si las dos contraseñas coinciden
            if ($(this).val() !== $('#contrasena').val()) {
                $(this).css({
                    "border-color": "red",
                    "border-width": "3px",
                    "border-style": "solid"
                });
                $('#contrasena').css("border-color", "red");
                swal("Las contraseñas deben coincidir");
            } else {
                $(this).css("border-color", "white");
                $('#contrasena').css("border-color", "white");
            }
        }
    });

    //javascript para prohibir ciertos caracteres
    $('#contrasena2').on('input', function() {
        var sanitizedValue = $(this).val().replace(/[^a-z0-9 !#$%&()*+-./:;=?@[\]{|}~]/gi, '');
        $(this).val(sanitizedValue);
    });

    
    $('#File').on("change", function() {
        var fileInput = $(this)[0].files[0]; // Obtener el archivo seleccionado
    
        // Limpiar el borde antes de realizar validaciones
        $(this).css({
            "border-color": "",
            "border-width": "",
            "border-style": ""
        });

        if (!fileInput) {
            // Si no se ha seleccionado ningún archivo
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe subir un archivo"); // Muestra el mensaje de alerta
            return;
        }
    
        // Verificar la extensión del archivo
        var fileExtension = fileInput.name.split('.').pop().toLowerCase();
        var validExtensions = ["jpg", "jpeg", "png", "gif"];
    
        if ($.inArray(fileExtension, validExtensions) == -1) {
            // Si la extensión no es válida
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe subir una imagen válida (jpg, jpeg, png, gif)");
        } else {
            // Si el archivo es válido, mostrar la imagen
            $(this).css({
                "border-color": "",
                "border-width": "",
                "border-style": ""
            });
    
            // Crear un FileReader para mostrar la imagen
            var reader = new FileReader();
            reader.onload = function(e) {
                // Mostrar la imagen en el div con id "imagePreview" usando las clases correctas
                $('#imagePreview').html('<img src="' + e.target.result + '" alt="Imagen de perfil" class="image">');
            }
            reader.readAsDataURL(fileInput); // Leer el archivo como una URL de datos
        }
    });

    $('#Medidor').on( "blur", function() {
        if ($(this).val().length === 0) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe ingresar un Identificador para el Medidor");
        }else{
            $(this).css("border-color","white");
        }
    });

    $('#Casa').on( "blur", function() {
        if ($(this).val().length === 0) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            swal("Debe ingresar un Nombre de Grupo");
        }else{
            $(this).css("border-color","white");
        }
    });
    
    
});


function validarSignup(){
    

    if(document.form.nombre.value==""){
        swal("Debe ingresar un Nombre");
        document.form.nombre.focus();
        return false;
    }

    if(document.form.email.value=="")
        {
            swal("Debe ingresar un email");
            document.form.email.focus();
            return false;
        }else{
            if(!validateEmail())
            {
                swal("Email invalido");
                document.form.email.focus();
                return false;
            }
        }

    if(document.form.contrasena.value=="")
    {
        swal("Debe ingresar una contrasena");
        document.form.contrasena.focus();
        return false;
    }

    if(document.form.contrasena2.value=="")
    {
        swal("Debe ingresar la repetición de la contrasena");
        document.form.contrasena2.focus();
        return false;
    }

    // Validar contraseñas al cambiar el segundo campo de contraseña
    $('#contrasena2').on("blur", function() {
        if ($(this).val() !== $('#contrasena').val()) {
            $(this).css({
                "border-color": "red",
                "border-width": "3px",
                "border-style": "solid"
            });
            $('#contrasena').css("border-color", "red");
            swal("Las contraseñas deben coincidir");
        } else {
            $(this).css("border-color", "white");
            $('#contrasena').css("border-color", "white");
        }
    });

    document.form.submit();
}

function validateEmail(email) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return emailPattern.test(email);
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

function checkFormValidity() {
    const nombre = $('#nombre').val().length > 0;
    const email = $('#email').val().length > 0 && validateEmail($('#email').val());
    const contrasena = $('#contrasena').val().length > 0;
    const contrasena2 = $('#contrasena2').val().length > 0 && $('#contrasena').val() === $('#contrasena2').val();
    const file = $('#File')[0].files.length > 0;

    if (nombre && email && contrasena && contrasena2 && file) {
        $("#submit-button").prop("disabled", false);
        toggleStyles(false); // Habilitar el botón con estilos normales
    } else {
        $("#submit-button").prop("disabled", true);
        toggleStyles(true);  // Deshabilitar el botón y aplicar estilos grises
    }
}