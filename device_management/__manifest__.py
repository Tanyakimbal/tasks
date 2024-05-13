#metadata for module
{
    "name": "Device Management",
    "version" : "1.0",
    "website" : "https://www.db1.com",
    "author" : "Tanya",
    "description" : """
        module to show devices and issues, complaints and replacements related to them.
    """,
    "category" : "IT",
    "depends" : ['hr', 'base'],
    "data" : [
        'security/ir.model.access.csv',
        'views/device_view.xml',
        'views/device_issue_view.xml',
        'views/device_complaint_view.xml',
        'views/device_replacement_view.xml',
        'views/menu_device_item.xml',
    ],
    "installable" : True,
    "application" : True,
    "license" : "LGPL-3"
}