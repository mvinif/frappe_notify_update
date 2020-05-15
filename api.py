from __future__ import unicode_literals
import frappe
import frappe.defaults
from frappe.utils import nowdate, cstr, flt, cint, now ,getdate
from frappe import throw, _
from frappe.utils import formatdate, get_number_format_info
import requests
import json
import datetime

@frappe.whitelist()
def notify_update(doc,action):

	# define which doctype will be monitores, can be more than one, just insert in list
	check_doctypes = ['example_doc']
	doc = doc.as_dict()
	try:
		if doc.ref_doctype in check_doctypes:
			updated_doc = json.loads(doc.data)
			msg = """
<h2>Doctype information change notification</h2>
<br>
<strong>Doctype:</strong> {doctype}<br>
<strong>Doc Name:</strong> {name}<br>
<strong>Updated by:</strong> {user}<br>
<strong>Date: </strong> {dt}<br>
""".format(doctype=doc.ref_doctype, name=doc.docname, user=frappe.session.user, dt=frappe.utils.get_datetime(doc.modified).strftime('%d/%m/%Y %H:%M:%S'))

			# loop through each change made
			for changes in updated_doc["changed"]:
				msg += "<br><strong>Item ID.:</strong> {id}<br><br><strong>Before:</strong> {before}<br><strong>After:</strong> {after}".format(id=changes[0], before=changes[1], after=changes[2])
			recipients = "team@company.com"
			subject = "[Update notication] Doc. {} - {}".format(doc.ref_doctype, doc.docname)

			# send notification email
			frappe.sendmail(recipients=recipients, subject= subject, message=msg, now=True)

	except Exception as e:
		print(e)
		pass