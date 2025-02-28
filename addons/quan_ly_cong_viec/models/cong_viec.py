from odoo import models, fields, api


class cong_viec(models.Model):
    _name = 'cong_viec'
    _description = 'Bảng chứa thông tin công việc'

    ma_cong_viec = fields.Char("Mã công việc", required=True)
    ten_cong_viec = fields.Char("Tên công việc")
    ngay_tao = fields.Date("Thời gian khởi tạo")
    ngay_ket_thuc = fields.Date("Thời gian kết thúc")
