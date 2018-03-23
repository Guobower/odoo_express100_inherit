# -*- coding: utf-8 -*-

from odoo import models, fields, api
import urllib

class myodoo(models.Model):
    _inherit = "stock.picking"
    express_company = fields.Many2one('kuaidi_company.kuaidi_company',u"快递公司")
    # express_company = fields.Char(u"快递公司")
    express_order = fields.Char(u"快递单号")
    express_message = fields.Text(u"快递信息")
    total = fields.Float(u"总计数量",compute="compute_total",store=True,default=0)

    @api.multi
    def getHtml(self):
        page = urllib.urlopen("http://www.kuaidi100.com/query?type=%s&postid=%s" % (self.express_company,self.express_order))
        html = page.read()
        self.express_message=html

    @api.depends('move_lines')
    def compute_total(self):
        for record in self.move_lines:
            self.total += record.product_uom_qty

