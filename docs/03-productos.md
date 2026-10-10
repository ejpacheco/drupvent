# Productos

**Estado:** Implementado (configuración en `config/sync`).

## Tipo de contenido `producto`

| Etiqueta | Nombre de máquina | Tipo | Obligatorio | Notas |
|---|---|---|---|---|
| Nombre | `title` | Título del nodo | Sí | |
| Categoría | `field_categoria_producto` | Referencia a término (`categoria_producto`) | Sí | Lista desplegable ordenada por nombre |
| Unidad de medida | `field_unidad_medida` | Lista de texto | Sí | Unidad, Kilogramo, Gramo, Litro o Mililitro. Por defecto, Unidad |
| Precio de venta | `field_precio_venta` | Decimal (14,2) | Sí | Mínimo 0 |
| Costo de referencia | `field_costo_referencia` | Decimal (14,2) | No | Mínimo 0. Costo estimado para calcular el margen |
| Controla inventario | `field_controla_inventario` | Booleano | No | Por defecto, Sí |
| Existencia mínima | `field_stock_minimo` | Decimal (12,3) | No | Mínimo 0. Umbral para la alerta de bajo inventario |
| Descripción | `field_descripcion` | Texto largo | No | |
| Activo | `status` | Estado de publicación | — | Por defecto, activo. Los productos inactivos no se venden |

### Ajustes del tipo de contenido

- **Revisiones activadas**, que dejan un historial de los cambios de precio y costo.
- No se promociona a la portada.
- Sin vista previa y sin mostrar la información de autor y fecha.
- Sin ajustes de menú.
- En el formulario se ocultan el autor, la fecha, el alias de URL, la promoción y el idioma.

### Precisión numérica

- **Importes:** `DECIMAL(14,2)`.
- **Cantidades:** `DECIMAL(12,3)`, para poder vender por peso o volumen.
- Drupal entrega estos valores como cadenas de texto. Los cálculos en código deben hacerse con `bcmath`, nunca con `float`.

## Taxonomía `categoria_producto`

Vocabulario **Categoría de producto**. Términos iniciales: Panadería, Heladería, Bebidas, Insumos, Otros.

> Los términos son contenido. No están en `config/sync` y hay que crearlos manualmente en cada entorno nuevo.

## Archivos de configuración

```
config/sync/node.type.producto.yml
config/sync/taxonomy.vocabulary.categoria_producto.yml
config/sync/field.storage.node.field_*.yml
config/sync/field.field.node.producto.field_*.yml
config/sync/core.base_field_override.node.producto.{title,status,promote}.yml
config/sync/core.entity_form_display.node.producto.default.yml
config/sync/core.entity_view_display.node.producto.default.yml
```

## Pendiente

- Formulario custom de registro y edición de productos dentro de un bloque (ver [04-inventario.md](04-inventario.md)).
- Campo de solo lectura "Existencia actual", que se mantendrá desde los movimientos de inventario.
- Vista de listado de productos.
