/* COP4331 Project 1
 */

//Handles user login.
function doLogin()
{
	try
	{	
		var logName = document.getElementById("usernameBox").value;
		var logPass = document.getElementById("passwordBox").value;
	
		document.getElementById("userSpan").innerHTML = "Logged in as " + logName + ".";
		toggleDiv("loginPage", false);
		toggleDiv("userPage", true);
	}
	catch(err)
	{
		document.getElementById("errorMsg1").innerHTML = err.message;
	}
	
}

//Handles user logout.
function doLogout()
{
	document.getElementById("usernameBox").value = "";
	document.getElementById("passwordBox").value = "";
	toggleDiv("loginPage", true);
	toggleDiv("userPage", false);
	toggleDiv("newAccPage", false);
}

//Shows new account page
function showNewAccPg()
{
	toggleDiv("loginPage", false);
	toggleDiv("newAccPage", true);
}

//Handles creating a new account
function doNewAcc()
{
	
}

//Exit from new account page back to main menu
function cancel()
{
	toggleDiv("loginPage", true);
	toggleDiv("newAccPage", false);
}

//Show or hide a div.
function toggleDiv(divID, show)
{
	var v;
	var d;
	
	if(show)
	{
		v = "visible";
		d = "block";
		
	}
	else
	{
		v = "hidden";
		d = "none";
	}
	
	document.getElementById(divID).style.visibility = v;
	document.getElementById(divID).style.display = d;
}