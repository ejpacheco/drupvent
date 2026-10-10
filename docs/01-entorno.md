# Entorno del proyecto

## Versiones

| Componente | Versión |
|---|---|
| Drupal | 11.4.9 (plantilla `drupal/legacy-project`, perfil `standard`) |
| PHP | 8.4 (con la extensión `bcmath` disponible) |
| Base de datos | MariaDB 11.8 con InnoDB, aislamiento `READ-COMMITTED` |
| Drush | 13.8 |
| Entorno local | DDEV 1.25 con nginx-fpm. URL: https://drupvent.ddev.site |

- **Idioma** del sitio: español (`es`).
- **Zona horaria**: `America/Bogota`.
- **Temas**: Olivero para el sitio público y Claro para la administración.

## Estructura de carpetas

El docroot es la **raíz del repositorio** (plantilla legacy):

```
core/             Núcleo de Drupal (gestionado por Composer, no versionado)
vendor/           Dependencias de Composer (no versionado)
modules/custom/   Módulos propios (todavía no hay ninguno)
modules/contrib/  Módulos contribuidos (gestionados por Composer)
config/sync/      Configuración exportada del sitio (versionada)
docs/             Esta documentación
```

## Gestión de la configuración

La estructura del sitio (tipos de contenido, campos, taxonomías, vistas, bloques y roles) se crea **como lo haría un site builder**, desde la interfaz o con Drush, y se exporta a `config/sync`.

```bash
ddev drush cex -y            # Exportar la configuración tras un cambio
ddev drush cim -y            # Importar la configuración en otro entorno
ddev drush config:status     # Ver las diferencias entre la base de datos y config/sync
```

Los términos de taxonomía y los nodos son **contenido**, no configuración. No viajan con `config/sync` y hay que crearlos en cada entorno.

## Herramientas de calidad

El proyecto todavía **no tiene** PHPUnit, PHPStan ni phpcs/coder (`drupal/core-dev` no está instalado). Su instalación está pendiente de decidir (ver [02-decisiones.md](02-decisiones.md)).

## Riesgo de seguridad conocido

Como el docroot es la raíz del repositorio y nginx no aplica los archivos `.htaccess`, los siguientes archivos responden HTTP 200 desde el navegador (comprobado el 2026-10-10):

- `/composer.lock`
- `/vendor/composer/installed.json`
- `/config/sync/*.yml`, es decir, toda la configuración exportada, incluidos roles y permisos

El archivo `config/sync/.htaccess` que genera Drupal **solo protege en Apache**.

**Solución propuesta:** migrar a la plantilla `drupal/recommended-project`, con el docroot en `web/` y `vendor/` y `config/` fuera de él. Está pendiente de aprobación.
