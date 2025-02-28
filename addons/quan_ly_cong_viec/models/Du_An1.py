from odoo import models, fields, api


class cong_viec(models.Model):
    _name = 'Du_An'
    _description = 'Bảng chứa thông tin công việc dự án'

    ma_du_an = fields.Char("Mã dự án", required=True)
    ten_du_anan = fields.CharChar("Tên của dự án")
    mo_ta = fields.Char("Mô tả")
    ngay_bat_daudau = fields.DateDate("Ngày bắt đầu")
    ngay_ket_thuc = fields.DateDate("Ngày kết thúc")
    trang_thai = fields.Char("Trạng thái")
    nguoi_tao = fields.Char("Người tạo")
    ngay_cap_nhat = fields.Date("Ngày cập nhật dự án")