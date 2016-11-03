import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def get_frappe_date_format():
	global_default_format = frappe.defaults.get_global_default("date_format") or "yyyy-mm-dd"
	return global_default_format.replace('yyyy', 'yy')

def has_website_permission(doc, ptype, user, verbose=False):
	if doc.doctype == "Post":
		return True

	# doctype = doc.doctype
	# customers, suppliers = get_customers_suppliers(doctype, user)
	# if customers:
	# 	return frappe.get_all(doctype, filters=[(doctype, "customer", "in", customers),
	# 		(doctype, "name", "=", doc.name)]) and True or False
	# elif suppliers:
	# 	fieldname = 'suppliers' if doctype == 'Request for Quotation' else 'supplier'
	# 	return frappe.get_all(doctype, filters=[(doctype, fieldname, "in", suppliers),
	# 		(doctype, "name", "=", doc.name)]) and True or False
	# else:
	# 	return False