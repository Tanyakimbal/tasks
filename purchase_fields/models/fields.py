from odoo import models, fields, api

class PurchaseEdit(models.Model):
    _inherit = "purchase.order"

    employee = fields.Many2one('hr.employee', string='Employee')
    product_alternate = fields.Many2one('product.product', string="Product")
    description_alternate = fields.Text(string="Description")
    quantity_alternate = fields.Float(string="Quantity")

    def _compute_no_of_product(self):
        for rec in self:
            product_sum = sum(rec.order_line.mapped('product_qty'))
            rec.no_of_product = product_sum
            for z in rec.order_line:
                print(z.product_id.name)

    no_of_product = fields.Integer(string="No of Products", compute=_compute_no_of_product)

class SettingsEdit(models.TransientModel):
    _inherit = "res.config.settings"

    my_name = fields.Char(string="Name")


