$(document).ready(function(){

window.signup = function()
{


	
var username = $("#username").val();
var password = $("#password").val();
var email = $("#email").val();

var data={"username":username,"email":email,"password":password}
var data=JSON.stringify(data)

$.ajax({
    type: 'POST',
    url: '/api/user/signup',
    data: data, 
    success: function(data) { 
 	alert("Success")
 	location.href = "signin";
    },
    contentType: "application/json",
    dataType: 'json',
    error: function (jqXHR, textStatus, errorThrown) {
                  if (jqXHR.status == 400) {
                      alert(jqXHR.responseText);
                  } else {
                      alert('Unexpected error.');
                  }
              }
});
}


window.reset = function()
{
var email = $("#email").val();
var data = {"email":email}
var data = JSON.stringify(data)
$.ajax({
    type: 'POST',
    url: '/api/reset/password_reset',
    data:data,
    contentType: "application/json",
    dataType: 'json',
    success: function(data) { 

      alert(JSON.stringify(data));
    }
  });
}







window.profile_update = function()
{
var email = $("#email").val();
var username = $("#username").val();
var fname = $("#fname").val();
var id = $("#uid").val();
var data = {"email":email,"fname":fname,"username":username}
var data = JSON.stringify(data)
$.ajax({
    type: 'PUT',
    url: '/api/user/'+id,
    data:data,
    headers: {"Authorization":"token "+token},
    contentType: "application/json",
    dataType: 'json',
    success: function(data) { 

      alert(JSON.stringify(data));
    }
  });
}


window.change = function()
{
var email = $("#email").val();
var password = $("#password").val();
var data = {"email":email,"password":password}
var data = JSON.stringify(data)
$.ajax({
    type: 'PUT',
    url: '/api/reset/change',
    data:data,
    contentType: "application/json",
    dataType: 'json',
    success: function(data) { 

      alert(JSON.stringify(data));
      location.href="/signin";
    }
  });
}


window.signin = function()
{
var password = $("#password").val();
var email = $("#email").val();

var data={"email":email,"password":password}
var data=JSON.stringify(data)

$.ajax({
    type: 'POST',
    url: '/api/user/signin',
    data: data, 
    success: function(data) { 
    	sessionStorage.setItem("token", data["token"]);
    	location.href = "/dashboard"
    },
    contentType: "application/json",
    dataType: 'json',
    error: function (jqXHR, textStatus, errorThrown) {
                  if (jqXHR.status == 400) {
                      alert(jqXHR.responseText);
                  } else {
                      alert('Unexpected error.');
                  }
              }
});


}



});
