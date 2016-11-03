# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from frappe import _

app_name = "discuit"
app_title = "Discuit"
app_publisher = "MN Technique"
app_description = "Forum app"
app_icon = "icon-comment"
app_color = "greenyellow"
app_email = "support@mntechnique.com"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/discuit/css/discuit.css"
# app_include_js = "/assets/discuit/js/discuit.js"

# include js, css files in header of web template
web_include_css = ["/assets/css/summernote.css", "/assets/css/selectize.css", "/assets/css/mnt.css", "/assets/css/scrollup.css"]
web_include_js = ["/assets/js/summernote.js", "/assets/js/selectize.js", "/assets/js/mnt.js"]

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"


# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }
# Website user home page (by function)
# get_website_user_home_page = "discuit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "discuit.install.before_install"
# after_install = "discuit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "discuit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Post": "discuit.api.check_discuit_post_permissions",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"discuit.tasks.all"
# 	],
# 	"daily": [
# 		"discuit.tasks.daily"
# 	],
# 	"hourly": [
# 		"discuit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"discuit.tasks.weekly"
# 	]
# 	"monthly": [
# 		"discuit.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "discuit.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "discuit.event.get_events"
# }