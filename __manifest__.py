{
    "name": "Etiquetas de producto con impuesto",
    "version": "1.0",
    "description": "Módulo para generar etiquetas de producto con precios que incluyen impuestos",
    "summary": "Generación de etiquetas de producto con impuesto",
    "author": "DGV",
    "website": "https://github.com/AlfaSystemas5457/product_label_tax",
    "license": "LGPL-3",
    "category": "inventory",
    "depends": [
        "product",
        "account",
        "stock",
    ],
    "data": [
        "views/product_label_layout_views.xml",
        "report/product_label_templates.xml",
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}
