from odoo import models


def _compute_price_with_tax(products, pricelist, env):
    """Compute tax-included prices for a list of products.

    Returns a dict {product_id: price_with_tax} for quick lookup in QWeb templates.
    """
    price_with_tax_by_product = {}
    for product in products:
        if pricelist:
            base_price = pricelist._get_product_price(
                product, 1,
                currency=pricelist.currency_id or product.currency_id
            )
        else:
            base_price = product.list_price
        if product.taxes_id:
            taxes = product.taxes_id._filter_taxes_by_company(env.company)
            price_with_tax = taxes.compute_all(base_price, product.currency_id)['total_included']
        else:
            price_with_tax = base_price
        price_with_tax_by_product[product.id] = price_with_tax
    return price_with_tax_by_product


class ReportProductLabel2x7(models.AbstractModel):
    _inherit = 'report.product.report_producttemplatelabel2x7'

    def _get_report_values(self, docids, data):
        values = super()._get_report_values(docids, data)
        values.setdefault('price_with_tax_by_product', {})
        if data.get('price_with_tax'):
            values['price_with_tax_by_product'] = _compute_price_with_tax(
                values['quantity'].keys(), values.get('pricelist'), self.env
            )
        return values


class ReportProductLabel4x7(models.AbstractModel):
    _inherit = 'report.product.report_producttemplatelabel4x7'

    def _get_report_values(self, docids, data):
        values = super()._get_report_values(docids, data)
        values.setdefault('price_with_tax_by_product', {})
        if data.get('price_with_tax'):
            values['price_with_tax_by_product'] = _compute_price_with_tax(
                values['quantity'].keys(), values.get('pricelist'), self.env
            )
        return values


class ReportProductLabel4x12(models.AbstractModel):
    _inherit = 'report.product.report_producttemplatelabel4x12'

    def _get_report_values(self, docids, data):
        values = super()._get_report_values(docids, data)
        values.setdefault('price_with_tax_by_product', {})
        if data.get('price_with_tax'):
            values['price_with_tax_by_product'] = _compute_price_with_tax(
                values['quantity'].keys(), values.get('pricelist'), self.env
            )
        return values


class ReportProductLabel4x12NoPrice(models.AbstractModel):
    _inherit = 'report.product.report_producttemplatelabel4x12noprice'

    def _get_report_values(self, docids, data):
        values = super()._get_report_values(docids, data)
        values.setdefault('price_with_tax_by_product', {})
        if data.get('price_with_tax'):
            values['price_with_tax_by_product'] = _compute_price_with_tax(
                values['quantity'].keys(), values.get('pricelist'), self.env
            )
        return values


class ReportProductLabelDymo(models.AbstractModel):
    _inherit = 'report.product.report_producttemplatelabel_dymo'

    def _get_report_values(self, docids, data):
        values = super()._get_report_values(docids, data)
        values.setdefault('price_with_tax_by_product', {})
        if data.get('price_with_tax'):
            values['price_with_tax_by_product'] = _compute_price_with_tax(
                values['quantity'].keys(), values.get('pricelist'), self.env
            )
        return values


class ReportStockLabelProductProduct(models.AbstractModel):
    _inherit = 'report.stock.label_product_product_view'

    def _get_report_values(self, docids, data):
        values = super()._get_report_values(docids, data)
        values.setdefault('price_with_tax_by_product', {})
        if data.get('price_with_tax'):
            values['price_with_tax_by_product'] = _compute_price_with_tax(
                values['quantity'].keys(), values.get('pricelist'), self.env
            )
        return values
