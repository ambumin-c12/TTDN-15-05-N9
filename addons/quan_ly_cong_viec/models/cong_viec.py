from odoo import models, fields, api


class cong_viec(models.Model):
    _name = 'congviec'
    _description = 'Bảng chứa thông tin công việc'

    ma_cong_viec = fields.Char("Mã công việc", required=True,)
    ma_binh_luan = fields.One2many('binhluan', 'ma_cong_viec', string="Bình Luận")
    ten_cong_viec = fields.Char("Tên công việc")
    ma_dinh_danh = fields.Many2many('nhan_vien1', 'nhan_vien_cong_viec_rel', 'ma_cong_viec', 'ma_dinh_danh', string="Nhân viên")
    ngay_tao = fields.Date("Thời gian khởi tạo", default=fields.Date.today())
    ngay_ket_thuc = fields.Date("Thời gian kết thúc")



