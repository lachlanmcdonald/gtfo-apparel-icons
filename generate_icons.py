from pathlib import Path
import json
import re
import os

DIR = Path(__file__).parent / "exports"
SVG_PATH = Path(__file__).parent / "svgs"

os.makedirs(SVG_PATH, exist_ok=True)


def generate_svg(title, a, b, c, d, e):
	return '\n'.join([
		'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5.02 15.54 221.07 221.07">',
		f'\t<title>{title}</title>',
		f'\t<path fill="{a}" d="m213.27 84.8-16.42 16.42-66.49-66.49 16.43-16.42 66.48 66.49Zm0 82.55-66.48 66.49-16.43-16.43 66.49-66.49 16.42 16.43ZM64.23 233.84l-66.48-66.49 16.42-16.42 66.49 66.48-16.43 16.43ZM-2.25 84.8l66.48-66.5 16.43 16.42-66.49 66.5L-2.25 84.8Z"/>',
		f'\t<path fill="{b}" d="m105.51 15.54 110.53 110.53-110.53 110.54L-5.02 126.07 105.5 15.54Zm27.62 43.86H77.89L38.84 98.46v55.23l39.05 39.06h55.24l39.05-39.06V98.46L133.13 59.4Z"/>',
		f'\t<path fill="{c}" d="m131.47 63.4 36.71 36.71v51.92l-36.71 36.71H79.55l-36.71-36.7V100.1l36.71-36.7h51.92Zm5.4 31.3a44.74 44.74 0 0 0-31.36-12.99 44.74 44.74 0 0 0-31.37 13 44.74 44.74 0 0 0-13 31.36 44.75 44.75 0 0 0 13 31.37 44.74 44.74 0 0 0 31.37 13c12.1 0 23.45-5.08 31.37-13a44.74 44.74 0 0 0 13-31.37c0-12.1-5.08-23.45-13-31.37Z"/>',
		f'\t<path fill="{d}" d="M145.87 126.07c0 11.3-4.4 21.13-11.82 28.54a39.73 39.73 0 0 1-28.54 11.83 39.73 39.73 0 0 1-28.54-11.83 39.73 39.73 0 0 1-11.82-28.54 39.7 39.7 0 0 1 11.82-28.54 39.73 39.73 0 0 1 28.54-11.82 39.7 39.7 0 0 1 28.54 11.82 39.73 39.73 0 0 1 11.82 28.54Zm-40.36-28.99-29 29 29 28.99 29-29-29-28.99Z"/>',
		f'\t<path fill="{e}" d="m82.18 126.07 23.33 23.34 23.33-23.34-23.33-23.33-23.33 23.33Z"/>',
		'</svg>',
	])


with (DIR / 'names.json').open('r') as f:
	NAMES = json.load(f)

with (DIR / 'palette.json').open('r') as f:
	PALETTES = json.load(f)

for prefab_name, palette in PALETTES.items():
	if prefab_name not in NAMES:
		print(f'Prefab does not have name: {prefab_name}')
	else:
		name = NAMES[prefab_name]
		svg = generate_svg(name, *palette)
		safe_name = re.sub(r"[^a-z0-9]", "_", name.lower().strip())
		svg_path = SVG_PATH / f'palette-{safe_name}.svg'

		with svg_path.open('w+') as f:
			f.write(svg)
