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
  //Clear text fields
	var cFirst = document.getElementById("fName").value = "",
	cLast = document.getElementById("lName").value = "",
	cEmail = document.getElementById("email").value = "",
	cPhone = document.getElementById("phone").value = "";

	//Create payload
	var jPayload = '{"first" : "' + cFirst + '", "last" : "' + cLast + '", "email" : "' + cEmail + '", "phone" : "' + cPhone + '"}';
}
