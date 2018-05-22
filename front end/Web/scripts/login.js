/* COP4331 Project 1
 * Login page JavaScript
 */

//Handles user login.
function doLogin()
{
	try
	{	
		var logName = document.getElementById("usernameBox").value;
		var logPass = document.getElementById("passwordBox").value;
	
		//Actually verify login credentials
		sessionStorage.setItem('name', logName);
		
		window.open("contactbook.html", "_self");
	}
	catch(err)
	{
		document.getElementById("errorMsg1").innerHTML = err.message;
	}
	
}