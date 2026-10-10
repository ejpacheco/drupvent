# Tema Drupvent

**Estado:** Implementado. Es el tema por defecto del sitio público; la administración sigue con Claro.

Ubicación: `themes/custom/drupvent`.

## Enfoque

Los estilos reproducen los **valores por defecto de Tailwind CSS v3**: reset "preflight", paleta de colores, espaciado, escala tipográfica, radios, sombras y nombres de las clases utilitarias.

Es **CSS puro**:
- No hay dependencia de Tailwind, Node.js ni ningún paso de compilación.
- No se usan fuentes externas; la tipografía es la pila del sistema, igual que en Tailwind.
- El tema no hereda de ningún otro (`base theme: false`), así que el marcado depende solo de las plantillas de core y de las del propio tema.

## Estructura

```
drupvent.info.yml          Regiones y librería global
drupvent.libraries.yml     Orden de carga de la CSS
logo.svg                   Logo provisional
css/
  base/tokens.css          Variables de diseño (paleta, espaciado, tipografía, radios, sombras)
  base/preflight.css       Reset equivalente a Tailwind Preflight
  base/typography.css      Estilos del body y del texto enriquecido
  layout/page.css          Cabecera, contenedor, columna principal + barra lateral, pie
  components/buttons.css   .button, .button--primary, .button--danger, .form-submit
  components/forms.css     Campos, checkbox/radio, descripciones, errores, fieldset (similar a @tailwindcss/forms)
  components/messages.css  Mensajes de estado tipo alerta
  components/navigation.css Menús, pestañas, ruta de navegación, paginador
  components/tables.css    Tablas
  utilities/utilities.css  Clases utilitarias (ARCHIVO GENERADO)
scripts/
  generate-utilities.py    Generador de utilities.css
templates/
  layout/     page, block, block--system-branding-block, block--page-title-block, page-title
  navigation/ menu, menu-local-tasks, menu-local-task, breadcrumb
  misc/       status-messages
```

## Variables de diseño (`tokens.css`)

| Grupo | Ejemplos |
|---|---|
| Paleta | `--gray-50` … `--gray-950`. También `slate`, `red`, `orange`, `amber`, `green`, `emerald`, `sky`, `blue` e `indigo` |
| Semánticas | `--color-primary-600`, `--color-text`, `--color-text-muted`, `--color-border`, `--color-bg`, `--color-surface` |
| Espaciado | `--spacing` (0.25rem), que se usa como `calc(var(--spacing) * 4)` |
| Tipografía | `--text-sm` / `--leading-sm` … `--text-5xl`. Pesos: `--font-medium`, `--font-semibold`… |
| Radios y sombras | `--radius-md`, `--radius-lg`, `--shadow-sm`, `--shadow-md`… |

**Para cambiar el color de marca** se editan solo las variables `--color-primary-*`, que hoy apuntan a `indigo`.

## Clases utilitarias

Tienen los mismos nombres y valores que en Tailwind:

```html
<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
  <div class="bg-white rounded-lg shadow-sm p-6">
    <p class="text-sm font-medium text-gray-500">Ventas del día</p>
    <p class="mt-2 text-3xl font-semibold text-gray-900">$ 1.250.000</p>
  </div>
</div>
```

**Incluidas:**
- Display, flexbox y grid (`grid-cols-*`, `col-span-*`).
- `gap`, padding y margin (escala 0–24), `space-x/y`.
- Tamaños: `w-*`, `h-*`, `max-w-*`.
- Tipografía, colores de texto, fondo y borde de toda la paleta, más `primary`.
- Bordes, `rounded`, sombras, opacidad, posición, `sr-only` y algunos `hover:`.

**Variantes responsive** (`sm:`, `md:`, `lg:`, `xl:`): solo para display, flexbox, grid, tamaños, tamaño de texto y alineación.

**No es Tailwind completo.** Si se necesita una clase que no existe, se añade al generador y se regenera:

```bash
python3 themes/custom/drupvent/scripts/generate-utilities.py
```

No se debe editar `utilities.css` a mano: el generador lo sobrescribe.

## Componentes de Drupal

El tema da estilo al marcado estándar de Drupal, de modo que los formularios custom (Form API) quedan con apariencia Tailwind **sin añadir clases**:
- Botones: el botón principal (`#button_type => 'primary'`) sale en color de marca, y `button--danger` en rojo.
- Campos, etiquetas obligatorias con `*`, descripciones y errores de validación.
- Mensajes de estado, pestañas (local tasks), menús, ruta de navegación, tablas y paginador.
- Los bloques de la barra lateral se muestran como tarjetas blancas. La clase `.card` permite el mismo estilo en cualquier otro sitio.

## Regiones

`header`, `primary_menu`, `secondary_menu`, `breadcrumb`, `highlighted`, `content_above`, `content`, `sidebar`, `footer_top`, `footer_bottom`.

Al instalar el tema, Drupal copió los bloques de Olivero a estas regiones. La ubicación de los bloques está exportada en `config/sync/block.block.drupvent_*.yml`.

## Pendiente

- **Logo definitivo.** `logo.svg` es provisional y se puede reemplazar el archivo, o subir otro desde *Apariencia → Configuración*.
- **Modo oscuro:** no implementado.
- **Revisión visual en navegador:** no se hizo. Se verificó por HTTP que las páginas renderizan sin errores y que la CSS agregada incluye los estilos del tema.
