# quan_ly_cong_viec/models/employee.py
from odoo import models, fields

class Employee(models.Model):
    _name = 'employee'
    _description = 'Nhân viên'

    name = fields.Char(string="Tên nhân viên", required=True)
    department_id = fields.Many2one('department', string="Phòng ban")
    user_id = fields.Many2one('res.users', string="Tài khoản người dùng")