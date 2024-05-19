#metadata for module
{
    "name": "Real Estate Ads",
    "version" : "1.0",
    "website" : "https://www.db1.com",
    "author" : "Tanya",
    "description" : """
        module to show available properties
    """,
    "category" : "Sales",
    "depends" : ["base"],
    "data" : [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'security/model_access.xml',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/menu_items.xml',
        #Data Files
        #'data/property_type.xml'
        'data/estate.property.type.csv'
    ],
    "installable" : True,
    "application" : True,
    "license" : "LGPL-3"
}