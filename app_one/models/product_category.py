from odoo import models, fields

class ProductCategory(models.Model):
    _inherit = "product.category"

    location_address = fields.Char(
        string="Website Address",
        size=250,
        help="Location address for this product category"
    )