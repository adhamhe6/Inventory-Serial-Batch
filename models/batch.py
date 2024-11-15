from odoo import models, fields

class ProductBatch(models.Model):
    _name = 'product.batch'
    _description = 'Product Batch'

    name = fields.Char(string='Batch Number', required=True, copy=False)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity')
    expiry_date = fields.Date(string='Expiry Date')
    location_id = fields.Many2one('stock.location', string='Location')
