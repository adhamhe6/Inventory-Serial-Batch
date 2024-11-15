from odoo import models, fields, api

class ProductSerial(models.Model):
    _name = 'product.serial'
    _description = 'Product Serial Number'

    name = fields.Char(string='Serial Number', required=True, copy=False, readonly=True, default='New')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    location_id = fields.Many2one('stock.location', string='Location')
    status = fields.Selection(
        [('available', 'Available'), ('reserved', 'Reserved'), ('sold', 'Sold')],
        string='Status', default='available'
    )

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('product.serial') or 'New'
        return super(ProductSerial, self).create(vals)
