from odoo import models, fields

class employee(models.Model):
    _name = 'employee.management'  # Tên model 
    _description = 'Employee Management'

    name = fields.Char(string="Tên", required = True)
    age = fields. Integer (string='Tuổi')
    department = fields.Char(string='Phòng ban')
