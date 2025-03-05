# quan_ly_cong_viec/models/task.py
from odoo import models, fields

class Task(models.Model):
    _name = 'task'
    _description = 'Công việc'

    name = fields.Char(string="Tên công việc", required=True)
    description = fields.Text(string="Mô tả")
    deadline = fields.Date(string="Ngày hết hạn")
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('in_progress', 'Đang thực hiện'),
        ('done', 'Hoàn thành'),
    ], string="Trạng thái", default='draft')
    leader_id = fields.Many2one('employee', string="Trưởng nhóm", required=True)
    member_ids = fields.Many2many('employee', string="Thành viên")
    department_id = fields.Many2one('department', string="Phòng ban")