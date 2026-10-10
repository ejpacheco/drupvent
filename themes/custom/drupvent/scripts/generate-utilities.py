"""Generates utilities.css with a Tailwind-compatible subset of utility classes."""
import sys

def esc(name):
    return name.replace(':', '\\:').replace('/', '\\/').replace('.', '\\.')

def rule(cls, decl):
    return f".{esc(cls)} {{ {decl} }}"

out = []
def section(title):
    out.append(f"\n/* {title} */")

def add(cls, decl):
    out.append(rule(cls, decl))

# Rules that also get responsive variants.
responsive = []
def radd(cls, decl):
    add(cls, decl)
    responsive.append((cls, decl))

space = {'0': '0', 'px': '1px', '0.5': '0.5', '1': '1', '1.5': '1.5', '2': '2', '2.5': '2.5', '3': '3', '4': '4',
         '5': '5', '6': '6', '8': '8', '10': '10', '12': '12', '16': '16', '20': '20', '24': '24'}
def sp(v):
    if v == '0':
        return '0'
    if v == 'px':
        return '1px'
    return f"calc(var(--spacing) * {v})"

section('Display')
for c, d in [('block', 'block'), ('inline-block', 'inline-block'), ('inline', 'inline'), ('flex', 'flex'),
             ('inline-flex', 'inline-flex'), ('grid', 'grid'), ('table', 'table'), ('hidden', 'none')]:
    radd(c, f"display: {d};")

section('Flexbox')
for c, d in [('flex-row', 'flex-direction: row;'), ('flex-col', 'flex-direction: column;'),
             ('flex-wrap', 'flex-wrap: wrap;'), ('flex-nowrap', 'flex-wrap: nowrap;'),
             ('flex-1', 'flex: 1 1 0%;'), ('flex-auto', 'flex: 1 1 auto;'), ('flex-none', 'flex: none;'),
             ('grow', 'flex-grow: 1;'), ('shrink-0', 'flex-shrink: 0;'),
             ('items-start', 'align-items: flex-start;'), ('items-center', 'align-items: center;'),
             ('items-end', 'align-items: flex-end;'), ('items-baseline', 'align-items: baseline;'),
             ('items-stretch', 'align-items: stretch;'),
             ('justify-start', 'justify-content: flex-start;'), ('justify-center', 'justify-content: center;'),
             ('justify-end', 'justify-content: flex-end;'), ('justify-between', 'justify-content: space-between;'),
             ('self-start', 'align-self: flex-start;'), ('self-center', 'align-self: center;'),
             ('self-end', 'align-self: flex-end;')]:
    radd(c, d)

section('Grid')
for n in [1, 2, 3, 4, 5, 6, 12]:
    radd(f"grid-cols-{n}", f"grid-template-columns: repeat({n}, minmax(0, 1fr));")
for n in [1, 2, 3, 4, 6]:
    radd(f"col-span-{n}", f"grid-column: span {n} / span {n};")
radd('col-span-full', 'grid-column: 1 / -1;')

section('Gap')
for k in space:
    if k == 'px':
        continue
    add(f"gap-{k}", f"gap: {sp(k)};")
    add(f"gap-x-{k}", f"column-gap: {sp(k)};")
    add(f"gap-y-{k}", f"row-gap: {sp(k)};")

section('Padding')
for k in space:
    v = sp(k)
    add(f"p-{k}", f"padding: {v};")
    add(f"px-{k}", f"padding-left: {v}; padding-right: {v};")
    add(f"py-{k}", f"padding-top: {v}; padding-bottom: {v};")
    add(f"pt-{k}", f"padding-top: {v};")
    add(f"pr-{k}", f"padding-right: {v};")
    add(f"pb-{k}", f"padding-bottom: {v};")
    add(f"pl-{k}", f"padding-left: {v};")

section('Margin')
for k in space:
    v = sp(k)
    add(f"m-{k}", f"margin: {v};")
    add(f"mx-{k}", f"margin-left: {v}; margin-right: {v};")
    add(f"my-{k}", f"margin-top: {v}; margin-bottom: {v};")
    add(f"mt-{k}", f"margin-top: {v};")
    add(f"mr-{k}", f"margin-right: {v};")
    add(f"mb-{k}", f"margin-bottom: {v};")
    add(f"ml-{k}", f"margin-left: {v};")
add('mx-auto', 'margin-left: auto; margin-right: auto;')
add('ml-auto', 'margin-left: auto;')
add('mr-auto', 'margin-right: auto;')

section('Space between children')
for k in space:
    if k == 'px':
        continue
    v = sp(k)
    out.append(f".{esc('space-y-' + k)} > :not([hidden]) ~ :not([hidden]) {{ margin-top: {v}; }}")
    out.append(f".{esc('space-x-' + k)} > :not([hidden]) ~ :not([hidden]) {{ margin-left: {v}; }}")

section('Sizing')
for c, d in [('w-full', 'width: 100%;'), ('w-auto', 'width: auto;'), ('w-screen', 'width: 100vw;'),
             ('h-full', 'height: 100%;'), ('h-screen', 'height: 100vh;'), ('min-h-screen', 'min-height: 100vh;'),
             ('min-w-0', 'min-width: 0;')]:
    radd(c, d)
for k in ['4', '5', '6', '8', '10', '12', '16', '20', '24']:
    add(f"w-{k}", f"width: {sp(k)};")
    add(f"h-{k}", f"height: {sp(k)};")
for c, v in [('xs', '20rem'), ('sm', '24rem'), ('md', '28rem'), ('lg', '32rem'), ('xl', '36rem'),
             ('2xl', '42rem'), ('3xl', '48rem'), ('4xl', '56rem'), ('5xl', '64rem'), ('6xl', '72rem'),
             ('7xl', '80rem'), ('prose', '65ch'), ('full', '100%'), ('none', 'none')]:
    add(f"max-w-{c}", f"max-width: {v};")

section('Typography')
for c in ['xs', 'sm', 'base', 'lg', 'xl', '2xl', '3xl', '4xl', '5xl']:
    radd(f"text-{c}", f"font-size: var(--text-{c}); line-height: var(--leading-{c});")
for c in ['normal', 'medium', 'semibold', 'bold']:
    add(f"font-{c}", f"font-weight: var(--font-{c});")
add('font-sans', 'font-family: var(--font-sans);')
add('font-mono', 'font-family: var(--font-mono);')
for c, d in [('text-left', 'text-align: left;'), ('text-center', 'text-align: center;'),
             ('text-right', 'text-align: right;')]:
    radd(c, d)
for c, d in [('uppercase', 'text-transform: uppercase;'), ('lowercase', 'text-transform: lowercase;'),
             ('capitalize', 'text-transform: capitalize;'), ('italic', 'font-style: italic;'),
             ('underline', 'text-decoration-line: underline;'), ('no-underline', 'text-decoration-line: none;'),
             ('tracking-tight', 'letter-spacing: -0.025em;'), ('tracking-wide', 'letter-spacing: 0.025em;'),
             ('tracking-wider', 'letter-spacing: 0.05em;'), ('leading-none', 'line-height: 1;'),
             ('leading-tight', 'line-height: 1.25;'), ('leading-normal', 'line-height: 1.5;'),
             ('leading-relaxed', 'line-height: 1.625;'), ('tabular-nums', 'font-variant-numeric: tabular-nums;'),
             ('whitespace-nowrap', 'white-space: nowrap;'),
             ('truncate', 'overflow: hidden; text-overflow: ellipsis; white-space: nowrap;')]:
    add(c, d)

section('Colors')
palette = ['slate', 'gray', 'red', 'orange', 'amber', 'green', 'emerald', 'sky', 'blue', 'indigo']
shades = ['50', '100', '200', '300', '400', '500', '600', '700', '800', '900', '950']
for c in ['white', 'black']:
    add(f"text-{c}", f"color: var(--{c});")
    add(f"bg-{c}", f"background-color: var(--{c});")
    add(f"border-{c}", f"border-color: var(--{c});")
add('bg-transparent', 'background-color: transparent;')
add('border-transparent', 'border-color: transparent;')
for p in palette:
    for s in shades:
        add(f"text-{p}-{s}", f"color: var(--{p}-{s});")
        add(f"bg-{p}-{s}", f"background-color: var(--{p}-{s});")
        add(f"border-{p}-{s}", f"border-color: var(--{p}-{s});")
for s in ['50', '100', '500', '600', '700']:
    add(f"text-primary-{s}", f"color: var(--color-primary-{s});")
    add(f"bg-primary-{s}", f"background-color: var(--color-primary-{s});")
    add(f"border-primary-{s}", f"border-color: var(--color-primary-{s});")
out.append(".hover\\:underline:hover { text-decoration-line: underline; }")
for p, s in [('gray', '50'), ('gray', '100'), ('gray', '200')]:
    out.append(f".hover\\:bg-{p}-{s}:hover {{ background-color: var(--{p}-{s}); }}")
out.append(".hover\\:bg-primary-500:hover { background-color: var(--color-primary-500); }")
out.append(".hover\\:text-primary-700:hover { color: var(--color-primary-700); }")

section('Borders')
for c, d in [('border', 'border-width: 1px;'), ('border-0', 'border-width: 0;'), ('border-2', 'border-width: 2px;'),
             ('border-t', 'border-top-width: 1px;'), ('border-b', 'border-bottom-width: 1px;'),
             ('border-l', 'border-left-width: 1px;'), ('border-r', 'border-right-width: 1px;'),
             ('border-l-4', 'border-left-width: 4px;'), ('border-dashed', 'border-style: dashed;')]:
    add(c, d)
out.append(".divide-y > :not([hidden]) ~ :not([hidden]) { border-top-width: 1px; }")
add('rounded-none', 'border-radius: 0;')
for c, v in [('rounded-sm', '--radius-sm'), ('rounded', '--radius'), ('rounded-md', '--radius-md'),
             ('rounded-lg', '--radius-lg'), ('rounded-xl', '--radius-xl'), ('rounded-2xl', '--radius-2xl'),
             ('rounded-full', '--radius-full')]:
    add(c, f"border-radius: var({v});")

section('Effects')
for c, v in [('shadow-sm', '--shadow-sm'), ('shadow', '--shadow'), ('shadow-md', '--shadow-md'),
             ('shadow-lg', '--shadow-lg'), ('shadow-xl', '--shadow-xl')]:
    add(c, f"box-shadow: var({v});")
add('shadow-none', 'box-shadow: none;')
for n in ['0', '25', '50', '75', '100']:
    add(f"opacity-{n}", f"opacity: {int(n) / 100:g};")
add('ring-1', 'box-shadow: 0 0 0 1px rgb(0 0 0 / 0.05);')
add('transition', 'transition: color, background-color, border-color, box-shadow, opacity var(--duration) var(--ease);')

section('Layout')
for c, d in [('relative', 'position: relative;'), ('absolute', 'position: absolute;'), ('fixed', 'position: fixed;'),
             ('sticky', 'position: sticky;'), ('inset-0', 'inset: 0;'), ('top-0', 'top: 0;'),
             ('right-0', 'right: 0;'), ('z-10', 'z-index: 10;'), ('z-50', 'z-index: 50;'),
             ('overflow-hidden', 'overflow: hidden;'), ('overflow-auto', 'overflow: auto;'),
             ('overflow-x-auto', 'overflow-x: auto;'), ('cursor-pointer', 'cursor: pointer;'),
             ('pointer-events-none', 'pointer-events: none;'), ('select-none', 'user-select: none;'),
             ('list-disc', 'list-style-type: disc;'), ('list-decimal', 'list-style-type: decimal;'),
             ('list-inside', 'list-style-position: inside;')]:
    add(c, d)
add('sr-only', 'position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0;')

for bp, w in [('sm', '640px'), ('md', '768px'), ('lg', '1024px'), ('xl', '1280px')]:
    out.append(f"\n/* Breakpoint {bp}: {w} */\n@media (min-width: {w}) {{")
    for cls, decl in responsive:
        out.append("  " + rule(f"{bp}:{cls}", decl))
    out.append("}")

header = """/**
 * @file
 * Utility classes with the same names and values as Tailwind CSS (v3 subset).
 *
 * GENERATED FILE. Edit scripts/generate-utilities.py and run:
 *   python3 themes/custom/drupvent/scripts/generate-utilities.py
 *
 * Responsive variants (sm:, md:, lg:, xl:) exist for display, flexbox, grid,
 * sizing, text size and text alignment utilities.
 */
"""
target = __file__.rsplit('/scripts/', 1)[0] + '/css/utilities/utilities.css'
with open(target, 'w') as f:
    f.write(header + "\n".join(out) + "\n")
print(f"Written {target}")
