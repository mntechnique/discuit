# GPL v3 - MN Technique and contributors
import frappe

def get_context(context):
	thr = frappe.get_all("Thread", fields=["name", "th_thread_title"])
	thread_post_count = []
	for i in thr:
		thread_post_count.append({
			"name": i.name,
			"post_count": frappe.db.count("Post", filters={"pst_thread":i.name}),
			"thread_title": i.th_thread_title
		})
	context.threads = thread_post_count
	context.nocache = 1
	return context

@frappe.whitelist()
def create_thread(th_thread_title, th_categories):
     #return "Thread Added: {p}; {tt}; {fc}".format(p=project, tt=thread_title, fc=thread_categories)
     threads = frappe.new_doc('Thread')
     threads.th_thread_title = thread_title
     threads.th_categories = thread_categories
     threads.th_status = "Open"
     threads.insert()
     frappe.db.commit()
     
     return "Thread {tid} added.".format(tid=thread.name)

@frappe.whitelist()
def save_thread(th_thread_title, th_categories):
     #return "Thread Edited: {t}; {tt}; {fc}".format(t=thread_id, tt=thread_title, fc=thread_categories)
     threads = frappe.get_doc('Thread', th_thread_title)
     threads.th_thread_title = thread_title
     threads.th_categories = thread_categories
     threads.save()
     frappe.db.commit()