from odoo import models, fields, api

class MyTask(models.Model):
    _name = 'my_task'
    _description = 'Công việc của tôi'
    _inherit = ['mail.thread']

    task_id = fields.Many2one('task', string="Công việc", required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', string="Người dùng", required=True)
    assigned_role = fields.Selection([
        ('leader', 'Trưởng nhóm'),
        ('member', 'Thành viên'),
    ], string="Vai trò", required=True)
    name = fields.Char(string="Tên công việc", required=True)
    description = fields.Text(string="Mô tả")
    deadline = fields.Date(string="Ngày hết hạn")
    progress = fields.Float(string="Tiến độ (%)", default=0.0)
    attachment_ids = fields.One2many('ir.attachment', 'res_id', string="Tệp đính kèm", domain=[('res_model', '=', 'my_task')])
    note = fields.Text(string="Ghi chú")

    @api.onchange('progress')
    def _onchange_progress(self):
        for my_task in self:
            if my_task.task_id:
                my_task.task_id.progress = my_task.progress
                if my_task.progress >= 100:
                    my_task.task_id.state = 'done'
                elif my_task.progress > 0 and my_task.task_id.state == 'draft':
                    my_task.task_id.state = 'in_progress'

    def write(self, vals):
        res = super(MyTask, self).write(vals)
        if 'progress' in vals and self.task_id:
            self.task_id.write({'progress': vals['progress']})
        return res