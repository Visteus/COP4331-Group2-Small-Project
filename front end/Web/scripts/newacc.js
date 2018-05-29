/* COP 4331 Projcet 1
 * New account JavaScript
 */
function doNewAcc()
{
	var username = document.getElementById("newUsername").value;
	var password1 = document.getElementById("newPass1").value;
	var password2 = document.getElementById("newPass2").value;
	var jPayload;
	
	if(password1 === password2)
	{
		//Reset the error text just in case
		document.getElementById("errorNU").innerHTML = "";
		
		//Create payload
		jPayload = '{"username" : "' + username + '", "password" : "' + password1 + '"}';
		
		try
		{
			//Send payload
		}
		catch(err)
		{
			document.getElementById("errorNU").innerHTML = err.message;
		}
	}
	else
	{
		document.getElementById("errorNU").innerHTML = "Error: Passwords must match";
	}
}
