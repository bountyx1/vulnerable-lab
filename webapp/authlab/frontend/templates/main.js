var False = false;
var True = true;
var host = "{{host}}"
var user = {{user|safe}}
var token = "{{token|safe}}"

function deleteCookie(cname) {
    var d = new Date(); 
    d.setTime(d.getTime() - (1000*60*60*24)); 
    var expires = "expires=" + d.toGMTString(); 
    window.document.cookie = cname+"="+"; "+expires;
 
}

function logout()
{
deleteCookie("token")
sessionStorage.clear()	
location.reload();

}