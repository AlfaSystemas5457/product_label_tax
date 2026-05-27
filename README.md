# Etiquetas de producto con impuesto

Este módulo agrega la opción de mostrar el **precio con impuesto incluido** en las etiquetas de producto, sin necesidad de modificar la configuración contable de los impuestos (`price_include`).

## Funcionalidad

- Agrega un campo booleano **"Precio con impuesto"** en el wizard de impresión de etiquetas.
- Cuando está activado, el precio mostrado en la etiqueta incluye los impuestos configurados en el producto.
- Cuando está desactivado, el precio se muestra sin impuestos (comportamiento original de Odoo).
- Funciona con todos los formatos de etiqueta: 2x7, 4x7, 4x12, Dymo y ZPL.

## Dependencias

- `product`
- `account`
- `stock`

## Instalación

1. Colocar el módulo en `extra-addons/`.
2. Actualizar la lista de aplicaciones desde el modo desarrollador.
3. Instalar "Etiquetas de producto con impuesto".

## Uso

1. Ir a un producto y seleccionar **Imprimir → Etiquetas**.
2. Elegir un formato que muestre precio (ej. `2 x 7 con precio`).
3. Seleccionar una lista de precios.
4. Activar **"Precio con impuesto"**.
5. Hacer clic en **Imprimir**.

El cálculo toma el precio de la lista de precios, le aplica los impuestos del producto usando `compute_all()`, y muestra `total_included` en la etiqueta.

## Licencia

LGPL-3
