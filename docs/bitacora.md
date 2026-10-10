# Bitácora

## 2026-10-10

- **Inspección inicial del proyecto.** Drupal 11.4.9, PHP 8.4 y MariaDB 11.8 en DDEV. Sitio recién instalado, sin tipos de contenido ni módulos custom. Se detectó que `config/sync`, `vendor/` y `composer.lock` son accesibles desde el navegador (ver [01-entorno.md](01-entorno.md)).
- **Propuesta de arquitectura** presentada: modelo de datos, estrategia de existencias, reportes y fases del MVP.
- **Tipo de contenido Producto y taxonomía Categoría de producto.** Se crearon primero dentro de un módulo `business_product`. Por decisión del equipo (D1), el módulo se eliminó y la configuración quedó en `config/sync`. Los campos se desbloquearon para poder editarlos desde la interfaz.
- **Eliminados los campos SKU y Tipo de producto** (D4).
- **Cambios hechos desde la interfaz** e incluidos en la exportación: se desinstaló el módulo `announcements_feed` y se borró el vocabulario *Etiquetas* (`tags`), con lo que el rol `content_editor` perdió sus permisos sobre etiquetas.
- **Diseño de la sección de inventario** con formularios custom en bloques (D5), pendiente de confirmar ([04-inventario.md](04-inventario.md)).
- **Creada la carpeta `docs/`.**
- **Tema `drupvent`** creado en `themes/custom/drupvent` (D7). Incluye variables de diseño, preflight, componentes para el marcado de Drupal, unas 1.100 clases utilitarias generadas y plantillas Twig. Se instaló como tema por defecto del sitio público, y los bloques se heredaron de Olivero. Se verificó por HTTP: `/` y `/user/login` responden 200, no hay errores en el log y la CSS agregada incluye los estilos ([05-tema.md](05-tema.md)).
- **Cambio hecho desde la interfaz** e incluido en la exportación: se creó el tipo de contenido *Página básica* (`node.type.page`).
