$(document).ready(function(){





$("#contactsubmit").click(function(){

var name = $("#name").val();
var email = $("#email").val();
var message = $("#message").val();

       $.post("/contact_us/",
        {
          name: name,
          email: email,
          message : message,
          csrfmiddlewaretoken: '{{csrf_token}}'
        },
        function(data,status){
            alert("Data: " + data + "\nStatus: " + status);
        });

});




});