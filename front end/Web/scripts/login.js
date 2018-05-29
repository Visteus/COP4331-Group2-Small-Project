/* COP4331 Project 1
 * Login page JavaScript
 */

//Handles user login.
function doLogin()
{
	var logName = document.getElementById("usernameBox").value;
	var logPass = document.getElementById("passwordBox").value;
	var payload, plString, response;
	var xmlRequest = new XMLHttpRequest();
	//Commented out until we have a URL.
	//var url = ???

	//Actually verify login credentials
	sessionStorage.setItem('name', logName);
	//Create JSON payload
	payload = {"username" : logName, "password" : logPass};
	plString = JSON.stringify(payload);
	
	//Commented out until we have a URL.
	//xmlRequest.open("POST", url, false);
	//xmlRequest.setRequestHeader("Content-type", "application/json; charset=UTF-8");
	
	//Send JSON payload
	try
	{	
		//Commented out until we have a URL.
		//xmlRequest.send(plString);
		//response = JSON.parse(xmlRequest.responseText);
		
		window.open("contactbook.html", "_self");
	}
	catch(err)
	{
		document.getElementById("errorMsg1").innerHTML = err.message;
	}
	
}
