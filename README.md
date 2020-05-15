
# Doc update verification in Frappe/ERPNext

This method is a simple way to keep monitoring which file was updated and by whom, also providing the previous information changed

## Usage
To ideal usage of this method, firstly we need :

 - Setup a default outgoing email account in Frappe configuration
 - Configure hook.py file
 - Insert main.py in frappe app
 - Configure which doctypes are going be monitored inside the file main.py
 
After the configuration the method runs automatically once someone made a change
 
 ## Functionality
 Each update trigger the function, which verify if the doctype is n the monitored list, once validated, the method keep running to send the e-amil notification
