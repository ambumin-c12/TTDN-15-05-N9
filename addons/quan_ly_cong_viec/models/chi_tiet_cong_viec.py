from odoo import models, fields, api


class cong_viec(models.Model):
    _name = 'chi_tiet_cong_viec'
    _description = 'Bảng chứa thông tin chi tiết công việc'

    ma = fields.Char("Mã ", required=True)
    ten = fields.Char("Tên công việc")
    ngay_bat_dau = fields.Date("Ngày bắt đầu công việc")
    ngay_ket_thuc = fields.Date(" Ngày kết thứ công việc")
    trang_thai = fields.Char("Trạng thái công việc")
    nhan_vien1 = fields.Char("Nhân viên được bàn giao")

