function isEmailValid(email){
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function hasFormError(email,contact){
    if(email == ""){
        alert('Email obligatorio');
        return true;
    }else if(!isEmailValid(email)){
        alert('Formato de email incorrecto');
        return true;
    }else if(contact == ""){
        alert('Nombre de compañía obligatorio');
        return true;
    }
    return false;
}

function cleanForm(){
    $("#contact_email").val("");
    $("#company_name").val("");
    $("#download_pdf").hide();
}

function sendContactFormData(crsfToken = ""){
    var contact = $("#company_name").val();
    var email = $("#contact_email").val();
    if (hasFormError(email,contact)) return 0;        
    
    $.ajax({
        url: window.location.href,
        type: "POST",
        data: {contact: contact,
               email: email,
               csrfmiddlewaretoken: crsfToken
            },
        success: function() {
            alert('Información enviada. Descarga el pdf para más información.');
            $("#download_pdf").show();
        },
        error: function() {
            alert('Ocurrió un error en el envío. Estamos trabajando en ello.');
        }    
    });
}