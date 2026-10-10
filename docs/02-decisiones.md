# Registro de decisiones

## Decisiones tomadas

### D1. La estructura de datos se crea como configuración de site builder
**Fecha:** 2026-10-10 · **Estado:** Aceptada

Los tipos de contenido, campos, taxonomías, vistas y bloques se crean como configuración del sitio y se exportan a `config/sync`. **No** se distribuyen dentro de módulos custom (`config/install`).

**Motivo:** el equipo prefiere administrar la estructura desde la interfaz de Drupal, con los campos editables por un site builder.

**Consecuencia:** el código custom se limita a la lógica que la configuración no puede resolver: reglas de negocio, formularios propios y bloques.

*Antecedente:* en un primer intento el tipo de contenido Producto se creó dentro de un módulo `business_product`. Se descartó, y la configuración pasó a `config/sync` sin módulo.

### D2. Los productos son nodos
**Fecha:** 2026-10-10 · **Estado:** Aceptada

Los productos se gestionan con un único tipo de contenido `producto`, no con un tipo por categoría. Aprovecha Views, Field UI, las revisiones (historial de cambios de precio) y los permisos de Drupal.

### D3. Las categorías de producto son una taxonomía
**Fecha:** 2026-10-10 · **Estado:** Aceptada

El vocabulario `categoria_producto` se puede administrar desde la interfaz y es independiente de cualquier otra clasificación.

### D4. Los campos SKU y Tipo de producto no se usan
**Fecha:** 2026-10-10 · **Estado:** Aceptada

Se eliminaron del tipo de contenido Producto porque no son necesarios para el negocio.

### D5. Los productos y el inventario se operan desde formularios custom en bloques
**Fecha:** 2026-10-10 · **Estado:** Aceptada en lo general (los detalles están en [04-inventario.md](04-inventario.md))

Los usuarios crean y editan productos y registran inventario desde formularios custom (Form API) colocados en bloques. Esos formularios actualizan los nodos correspondientes. Los formularios de nodo de `/node/add` quedan solo para el administrador.

### D6. La existencia nunca se escribe directamente
**Fecha:** 2026-10-10 · **Estado:** Propuesta

Toda variación de existencias se registra como un movimiento de inventario. La existencia de cada producto es la suma de sus movimientos. Un servicio la recalcula dentro de una transacción y con el producto bloqueado, para evitar inconsistencias cuando hay operaciones simultáneas.

## Decisiones pendientes

| # | Pregunta | Recomendación |
|---|---|---|
| P1 | ¿Migrar a `recommended-project` (docroot en `web/`)? | Sí, por el riesgo de seguridad descrito en [01-entorno.md](01-entorno.md) |
| P2 | ¿Instalar `drupal/core-dev` para las pruebas automatizadas? | Sí, en `require-dev` |
| P3 | ¿El bloque de inventario tiene movimiento individual, conteo físico o ambos? | Ambos |
| P4 | ¿En qué rutas y con qué tema van las páginas de gestión? | `/gestion/productos` y `/gestion/inventario` |
| P5 | ¿Se permiten existencias negativas? | No, salvo con un permiso especial |
| P6 | ¿Se registra el costo unitario en las entradas desde ya? | Sí, para calcular el margen más adelante |
| P7 | ¿Nombre del módulo custom? | `drupvent_inventario` |
| P8 | Impuestos: ¿IVA o impoconsumo? ¿Los precios lo incluyen? | Por definir antes de la sección de ventas |
| P9 | ¿Las ventas, sus líneas y los pagos son nodos o entidades custom? | Por evaluar antes de la sección de ventas, según el volumen esperado |
