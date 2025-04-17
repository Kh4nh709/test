{
    'name': "Employee Management",
    'summary': "Module quản lý Employees á",
    'description': """
        This module displays all employees in Odoo.
    """,
    'author': "Phạm Trần Vân Khương",
    'license': 'LGPL-3',
    "category": "Custom",
    'version':'1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',  # Thêm dòng này
        'views/employee_views.xml',
    ],
    'installable': True,
    'application': True,
}