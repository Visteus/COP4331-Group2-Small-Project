/* COP 4331 Projcet 1
 * Contact book JavaScript
 */
 function doLogout ()
 {
	 window.open("login.html","_self");
 }
 
 window.onload = function setUsrSpan()
 {
	try
	{
		var logName = sessionStorage.getItem('name');
		document.getElementById("userSpan").innerHTML = "Logged in as " + logName + ".";
	}
	catch(err)
	{
		document.getElementById("errorCB").innerHTML = err.message;
	}
 }
 
//Sends new contact information to server
function confirmAdd()
{
	var cFirst = document.getElementById("fName").value;
	var cLast = document.getElementById("lName").value;
	var cEmail = document.getElementById("email").value;
	var cPhone = document.getElementById("phone").value;
	
	//Create payload
	var jPayload = '{"first" : "' + cFirst + '", "last" : "' + cLast + '", "email" : "' + cEmail + '", "phone" : "' + cPhone + '"}';
}
