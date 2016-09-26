import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def get_frappe_date_format():
	global_default_format = frappe.defaults.get_global_default("date_format") or "yyyy-mm-dd"
	return global_default_format.replace('yyyy', 'yy')