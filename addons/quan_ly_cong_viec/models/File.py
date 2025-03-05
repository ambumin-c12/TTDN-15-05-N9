from odoo import models, fields, api


class File(models.Model):
    _name = 'file'
    _description = 'Bảng chứa thông tin file'

    ma_file = fields.Char("Mã file", required=True)
    ten_file = fields.Char("Tên file")
    cong_viec_LQ = fields.Char("Công việc liên quan đến file")
    nguoi_tai_len = fields.Char("Người đã tải lên file")
    duong_dan_luu_file = fields.Char("Đường dẫn") 
    ngay_tai_len = fields.Date("Ngày tải lên")
