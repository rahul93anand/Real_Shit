$(document).ready(function(){



$("#signin").click(function(){


var email = $("#email").val();
var password = $("#password").val();

    $.post("/signin/",
        {

          email: email,
          password: password,
          csrfmiddlewaretoken: '{{csrf_token}}'
         },
        function(data,status){
                alert(data);
        });

});





});