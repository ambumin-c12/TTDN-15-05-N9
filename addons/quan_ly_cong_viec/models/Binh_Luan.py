from odoo import models, fields, api

class Binh_Luan(models.Model):
    _name = 'binhluan'
    _description = 'Bảng chứa Bình Luận'

    ma_binh_luan = fields.Char("Mã Bình Luận", required=True, copy=False, index=True)
    ma_cong_viec = fields.Many2one('congviec', string="Công Việc Liên Quan", ondelete='cascade')
    ma_dinh_danh = fields.Many2one('res.users', string="Người Bình Luận", default=lambda self: self.env.user)
    noi_dung = fields.Text("Nội Dung Bình Luận")
    ngay_dang = fields.Date("Ngày Đăng", default=fields.Date.today)


