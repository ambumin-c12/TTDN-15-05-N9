from odoo import models, fields, api

class NhanVien(models.Model):
    _name = 'nhan_vien1'  # Đổi tên theo chuẩn module Odoo
    _description = 'Bảng chứa thông tin nhân viên'
    
    ma_dinh_danh = fields.Char("Mã Định Danh", required=True, copy=False, index=True)
    ten_nv = fields.Char("Tên Nhân Viên", required=True)
    ngay_sinh = fields.Date("Ngày Sinh")
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ')
    ], string='Giới tính', default='male')

    que_quan = fields.Char("Quê Quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số Điện Thoại")

    # Many2many với công việc
    ma_cong_viec = fields.Many2many(
        'your_module.congviec',  # Đổi cho đúng với model Công Việc
        'nhan_vien_cong_viec_rel',
        'ma_dinh_danh', 'ma_cong_viec',
        string="Công Việc"
    )



