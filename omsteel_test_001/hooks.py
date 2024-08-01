app_name = "omsteel_test_001"
app_title = "Omsteel Test 001"
app_publisher = "khattab"
app_description = "Omsteel Test 001"
app_email = "info@khattab.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------


# app_include_css = "/assets/omsteel_test_001/css/font_style.css"

# include js, css files in header of desk.html
# app_include_css = "/assets/omsteel_test_001/css/omsteel_test_001.css"
# app_include_js = "/assets/omsteel_test_001/js/omsteel_test_001.js"

# include js, css files in header of web template
# web_include_css = "/assets/omsteel_test_001/css/omsteel_test_001.css"
# web_include_js = "/assets/omsteel_test_001/js/omsteel_test_001.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "omsteel_test_001/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "omsteel_test_001/public/icons.svg"

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
# jinja = {
# 	"methods": "omsteel_test_001.utils.jinja_methods",
# 	"filters": "omsteel_test_001.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "omsteel_test_001.install.before_install"
# after_install = "omsteel_test_001.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "omsteel_test_001.uninstall.before_uninstall"
# after_uninstall = "omsteel_test_001.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "omsteel_test_001.utils.before_app_install"
# after_app_install = "omsteel_test_001.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "omsteel_test_001.utils.before_app_uninstall"
# after_app_uninstall = "omsteel_test_001.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "omsteel_test_001.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"omsteel_test_001.tasks.all"
# 	],
# 	"daily": [
# 		"omsteel_test_001.tasks.daily"
# 	],
# 	"hourly": [
# 		"omsteel_test_001.tasks.hourly"
# 	],
# 	"weekly": [
# 		"omsteel_test_001.tasks.weekly"
# 	],
# 	"monthly": [
# 		"omsteel_test_001.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "omsteel_test_001.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "omsteel_test_001.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "omsteel_test_001.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["omsteel_test_001.utils.before_request"]
# after_request = ["omsteel_test_001.utils.after_request"]

# Job Events
# ----------
# before_job = ["omsteel_test_001.utils.before_job"]
# after_job = ["omsteel_test_001.utils.after_job"]

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
# 	"omsteel_test_001.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


# ================  Adding ========================

app_include_css = "/assets/omsteel_test_001/css/font_style.css"


override_doctype_class = {
    "Work Order": "omsteel_test_001.overrides.work_order.CustomWorkOrder",
    "Stock Entry": "omsteel_test_001.overrides.stock_entry.CustomStockEntry",
}

doc_events = {
    "BOM": {
        "validate": [
            "omsteel_test_001.omsteel_test_001.production_items_table.move_data_from_production_items_table_to_scrap_items",
            # "omsteel_test_001.omsteel_test_001.production_items_table.calc_qty",
        ],
    },
    "Stock Entry": {
        "validate": [
            "omsteel_test_001.omsteel_test_001.production_items_table.check_batch_bundle_and_batch_no",
        ]
    },
    "Work Order": {
        "validate": [
            # "omsteel_test_001.omsteel_test_001.production_items_table.mod_qty",
        ]
    }
}

doctype_js = {
    "Stock Entry": "public/js/bom_omsteel.js",
    "Work Order": "public/js/bom_omsteel.js",
    "BOM": "public/js/bom_omsteel.js",
}

fixtures = [{"dt": "Custom Field", "filters": [["module", "=", "Omsteel Test 001"]]}]
