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