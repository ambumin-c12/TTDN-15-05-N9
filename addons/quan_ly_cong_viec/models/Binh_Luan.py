from odoo import models, fields, api


class cong_viec(models.Model):
    _name = 'Binh_Luan'
    _description = 'Bảng chứa Bình Luận'

    ma_binh_luan = fields.Char("Mã Bình Luận", required=True)
    cong_viec_LQuan = fields.Date("Công Việc Liên Quan")
    nguoi_BL = fields.Char("Người Bình Luận")
    noi_dung = fields.Char("Nội Dung Bình Luận")
    ngay_dang = fields.Char("Ngày Đăng")