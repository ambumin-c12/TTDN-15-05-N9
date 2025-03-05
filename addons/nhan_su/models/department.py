# quan_ly_cong_viec/models/department.py
from odoo import models, fields

class Department(models.Model):
    _name = 'department'
    _description = 'Phòng ban'

    name = fields.Char(string="Tên phòng ban", required=True)
    manager_id = fields.Many2one('employee', string="Trưởng phòng")