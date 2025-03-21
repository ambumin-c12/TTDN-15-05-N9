# quan_ly_cong_viec/models/task.py
from odoo import models, fields, api

class Task(models.Model):
    _name = 'task'
    _description = 'Công việc'
    _inherit = ['mail.thread']

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
    progress = fields.Float(string="Tiến độ (%)", default=0.0, help="Phần trăm hoàn thành công việc (0-100%)")
    attachment_ids = fields.One2many('ir.attachment', 'res_id', string="Tệp đính kèm", domain=[('res_model', '=', 'task')])
    my_task_ids = fields.One2many('my_task', 'task_id', string="Công việc cá nhân")

    @api.onchange('progress')
    def _onchange_progress(self):
        for task in self:
            if task.progress >= 100:
                task.state = 'done'
            elif task.progress > 0 and task.state == 'draft':
                task.state = 'in_progress'

    def _get_assigned_tasks(self):
        current_employee = self.env['employee'].search([('user_id', '=', self.env.user.id)], limit=1)
        if current_employee:
            return self.search(['|', ('leader_id', '=', current_employee.id), ('member_ids', 'in', current_employee.id)])
        return self.env['task']

    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals)
        task._update_my_tasks()
        return task

    def write(self, vals):
        res = super(Task, self).write(vals)
        self._update_my_tasks()
        return res

    def _update_my_tasks(self):
        self.my_task_ids.unlink()
        if self.leader_id and self.leader_id.user_id:
            self.env['my_task'].create({
                'task_id': self.id,
                'user_id': self.leader_id.user_id.id,
                'assigned_role': 'leader',
                'name': self.name,
                'description': self.description,
                'deadline': self.deadline,
                'progress': self.progress,
            })
        for member in self.member_ids:
            if member.user_id:
                self.env['my_task'].create({
                    'task_id': self.id,
                    'user_id': member.user_id.id,
                    'assigned_role': 'member',
                    'name': self.name,
                    'description': self.description,
                    'deadline': self.deadline,
                    'progress': self.progress,
                })

    @api.model
    def _init_my_tasks(self):
        tasks = self.search([])
        for task in tasks:
            task._update_my_tasks()