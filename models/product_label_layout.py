from odoo import fields, models


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    price_with_tax = fields.Boolean(
        "Precio con impuesto",
        default=True,
        help="Si está activado, el precio mostrado en la etiqueta incluirá los impuestos.",
    )

    def _prepare_report_data(self):
        xml_id, data = super()._prepare_report_data()
        data["price_with_tax"] = self.price_with_tax
        return xml_id, data
