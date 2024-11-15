from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    tracking_type = fields.Selection(
        [('none', 'None'), ('serial', 'Serial Number'), ('batch', 'Batch Number')],
        string='Tracking Type',
        default='none'
    )
