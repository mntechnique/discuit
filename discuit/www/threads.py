# GPL v3 - MN Technique and contributors
import frappe
import json
from frappe import database

def get_context(context):
	thr = frappe.get_all("Thread", fields=["name", "th_thread_title","th_categories"])
	thread_post_count = []
	for i in thr:
		thread_post_count.append({
			"name": i.name,
			"post_count": frappe.db.count("Post", filters={"pst_thread":i.name}),
			"thread_title": i.th_thread_title,
			"thread_category":i.th_categories
		})
	context.threads = thread_post_count
	context.no_cache = 1
	return context

@frappe.whitelist()
def create_thread(thread_title, thread_category):
     thread = frappe.new_doc('Thread')
     thread.th_thread_title = thread_title
     thread.th_categories = thread_category
     thread.th_status = "Open"
     thread.insert()
     thread.save()
     frappe.db.commit()
     
     return "Thread {tid} added.".format(tid=thread.name)

@frappe.whitelist()
def update_thread(thread_id, thread_title, thread_category):
     thread = frappe.get_doc('Thread', thread_id)
     thread.th_thread_title = thread_title
     thread.th_categories = thread_category
     thread.save()
     frappe.db.commit()

@frappe.whitelist()
def get_thread_categories():
	out = []
	for i in frappe.get_all("Forum Category"):
		out.append({ "text" : i['name'], "value": i["name"].replace(' ', '_').lower()})
	return out