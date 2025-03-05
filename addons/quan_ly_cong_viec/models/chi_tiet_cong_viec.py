from odoo import models, fields, api


class chitietcongviec(models.Model):
    _name = 'chitietcongviec'
    _description = 'Bảng chứa thông tin chi tiết công việc'
    ma_CTCV = fields.Char("Mã  chi tiết công việc", required=True)
    ten = fields.Char("Tên công việc")
    ngay_bat_dau = fields.Date("Ngày bắt đầu công việc")
    ngay_ket_thuc = fields.Date(" Ngày kết thúc công việc")
    trang_thai = fields.Selection([
        ('moi', 'Mới'),
        ('dang_lam', 'Đang thực hiện'),
        ('hoan_thanh', 'Hoàn thành'),
        ('huy', 'Hủy bỏ')
        ], string="Trạng Thái", default='moi')
    
    nhan_su = fields.Char("Nhân viên được bàn giao")


