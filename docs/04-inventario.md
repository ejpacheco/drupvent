# Inventario

**Estado:** Propuesta. Pendiente de confirmar las decisiones P3 a P7 de [02-decisiones.md](02-decisiones.md).

## Principios

1. **Los nodos son el almacenamiento.** Los tipos de contenido Producto y Movimiento de inventario se definen como configuración (D1).
2. **Los formularios custom en bloques son la forma de operar** (D5).
3. **Un único servicio, `InventoryManager`, contiene las reglas.** Los formularios recogen los datos y llaman al servicio; el futuro formulario de ventas usará el mismo.
4. **La existencia nunca se escribe directamente** (D6). Cada cambio genera un movimiento que lo respalda.

## Configuración (site builder)

### Tipo de contenido `movimiento_inventario`

| Campo | Tipo | Notas |
|---|---|---|
| Producto | Referencia a nodo `producto` | Obligatorio |
| Tipo de movimiento | Lista | Inventario inicial, entrada por compra, salida por venta, ajuste positivo, ajuste negativo, merma, devolución |
| Cantidad | Decimal (12,3) | Siempre positiva. El signo lo determina el tipo |
| Costo unitario | Decimal (14,2) | Opcional, para las entradas |
| Documento de origen | Texto | Opcional. Más adelante se relacionará con ventas y compras |
| Observación | Texto | Motivo del movimiento |
| Fecha y usuario | Campos propios del nodo | Fecha de creación y autor |

### Cambio en `producto`

Se añade el campo **Existencia actual** (decimal 12,3), oculto en el formulario. Solo lo actualiza `InventoryManager`.

### Vistas y páginas

- `/gestion/productos`: listado de productos con enlace "Editar" y el bloque de registro de productos.
- `/gestion/inventario`: existencias, productos con bajo inventario, últimos movimientos y el bloque de inventario.

Los bloques se colocan en *Diseño de bloques*, limitados a esas rutas.

### Rol

**Encargado de inventario.**

## Código (módulo custom)

### `InventoryManager`

1. Asigna el signo según el tipo: las entradas, los ajustes positivos, las devoluciones y el inventario inicial suman; las salidas, los ajustes negativos y las mermas restan.
2. Abre una transacción y bloquea el producto.
3. Rechaza el movimiento si deja la existencia negativa, salvo que el usuario tenga permiso para ello.
4. Crea el nodo del movimiento con un título automático, por ejemplo *"Merma · Pan tajado · 3 unidades"*.
5. Recalcula la existencia como la suma de todos los movimientos del producto y la guarda en el producto sin crear una revisión nueva.

### Bloque "Registro de productos"

- **Crear:** todos los campos del producto más una **existencia inicial** opcional, que genera un movimiento de tipo *Inventario inicial*.
- **Editar:** el formulario se precarga desde el enlace del listado (`?editar=<nid>`). La existencia **no** se puede editar aquí.

### Bloque "Inventario"

- **Movimiento individual:** producto (autocompletar), tipo, cantidad, costo y observación.
- **Conteo físico:** tabla de productos, filtrable por categoría, con la existencia del sistema y una columna para el conteo real. Al guardar, se genera un ajuste positivo o negativo por cada diferencia, con el motivo "Conteo físico". Las filas vacías se ignoran.

### Integridad

- Los movimientos guardados **no se pueden editar ni borrar**, ni siquiera por el administrador. Los errores se corrigen con movimientos compensatorios.
- Un comando drush recalcula y verifica las existencias a partir de los movimientos.

### Permisos propios

`gestionar productos`, `registrar movimientos de inventario`, `realizar conteo físico` y `permitir existencia negativa`.

## Riesgo conocido

Cuando se implementen las ventas, cada línea vendida generará un movimiento. Con un volumen alto, eso pueden ser cientos de miles de nodos al año. Hay que medir el volumen real y reevaluar el tipo de almacenamiento antes de la sección de ventas (P9).
