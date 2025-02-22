app_name = "burundi_compliance"
app_title = "Burundi Compliance"
app_publisher = "Navari Limited"
app_description = "Burundi OBR Tax Inegration"
app_email = "mania@navari.co.ke"
app_license = "mit"
# required_apps = []

fixtures=[
    "EBIMS APIs",
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/burundi_compliance/css/burundi_compliance.css"
# app_include_js = "/assets/burundi_compliance/js/burundi_compliance.js"

# include js, css files in header of web template
# web_include_css = "/assets/burundi_compliance/css/burundi_compliance.css"
# web_include_js = "/assets/burundi_compliance/js/burundi_compliance.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "burundi_compliance/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views

doctype_js = {
    "Sales Invoice":"burundi_compliance/client_scripts/get_invoice.js",
    "Company":"burundi_compliance/client_scripts/confirm_tin.js",
    "doctype" : "public/js/doctype.js"}


# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "burundi_compliance/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
jinja = {
    
	"methods": "burundi_compliance.burundi_compliance.utils.qr_code_generator.get_qr_code",
	#"filters": "burundi_compliance.utils.jinja_filters"
}

# Installation
# ------------

# before_install = "burundi_compliance.install.before_install"
# after_install = "burundi_compliance.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "burundi_compliance.uninstall.before_uninstall"
# after_uninstall = "burundi_compliance.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "burundi_compliance.utils.before_app_install"
# after_app_install = "burundi_compliance.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "burundi_compliance.utils.before_app_uninstall"
# after_app_uninstall = "burundi_compliance.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "burundi_compliance.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Invoice":{
        
       "on_submit": "burundi_compliance.burundi_compliance.overrides.sales_invoice.on_submit",
        "before_cancel": "burundi_compliance.burundi_compliance.overrides.cancel_invoice.cancel_invoice",
        
        
    },
    "Purchase Receipt":{
        "on_submit":"burundi_compliance.burundi_compliance.overrides.purchase_receipt.on_submit",
    },
    "Delivery Note":{
        "on_submit":"burundi_compliance.burundi_compliance.overrides.delivery_note.on_submit_update_stock"
    },
    "Stock Entry":{
        "on_submit":"burundi_compliance.burundi_compliance.overrides.stock_entry.on_submit"
    },
    "Stock Reconciliation":{
        "on_submit":"burundi_compliance.burundi_compliance.overrides.stock_reconciliation.on_submit"
    },
    
    "Purchase Invoice":{
        "on_submit": "burundi_compliance.burundi_compliance.overrides.purchase_invoice.on_submit_update_stock",
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"burundi_compliance.tasks.all"
# 	],
# 	"daily": [
# 		"burundi_compliance.tasks.daily"
# 	],
# 	"hourly": [
# 		"burundi_compliance.tasks.hourly"
# 	],
# 	"weekly": [
# 		"burundi_compliance.tasks.weekly"
# 	],
# 	"monthly": [
# 		"burundi_compliance.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "burundi_compliance.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "burundi_compliance.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "burundi_compliance.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["burundi_compliance.utils.before_request"]
# after_request = ["burundi_compliance.utils.after_request"]

# Job Events
# ----------
# before_job = ["burundi_compliance.utils.before_job"]
# after_job = ["burundi_compliance.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"burundi_compliance.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

