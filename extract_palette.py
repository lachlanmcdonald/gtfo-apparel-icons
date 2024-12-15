import json
from os import path, walk
from pathlib import Path

import yaml


def find_palettes(directory):
    temp = []
    for root, _dirs, files in walk(directory):
        for file in files:
            if "palette" in file.lower() and path.splitext(file)[1] == ".prefab":
                temp.append(path.join(root, file))
    return temp


def rgb_to_hex(d):
    r = int(d["r"] * 255)
    g = int(d["g"] * 255)
    b = int(d["b"] * 255)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def extract_palette(directory):
    palette_files = find_palettes(directory)
    palette = {}

    for palette_path in palette_files:
        with open(palette_path, mode="r", encoding="utf8") as f:
            raw = f.read()
            mono_index = raw.index("MonoBehaviour:")
            data = yaml.safe_load(raw[mono_index:])

            assert "MonoBehaviour" in data
            assert "m_primaryTone" in data["MonoBehaviour"]
            assert "m_secondaryTone" in data["MonoBehaviour"]
            assert "m_tertiaryTone" in data["MonoBehaviour"]
            assert "m_quaternaryTone" in data["MonoBehaviour"]
            assert "m_quinaryTone" in data["MonoBehaviour"]
            assert "m_color" in data["MonoBehaviour"]["m_primaryTone"]
            assert "m_color" in data["MonoBehaviour"]["m_secondaryTone"]
            assert "m_color" in data["MonoBehaviour"]["m_tertiaryTone"]
            assert "m_color" in data["MonoBehaviour"]["m_quaternaryTone"]
            assert "m_color" in data["MonoBehaviour"]["m_quinaryTone"]

            primaryTone = data["MonoBehaviour"]["m_primaryTone"]["m_color"]
            secondaryTone = data["MonoBehaviour"]["m_secondaryTone"]["m_color"]
            tertiaryTone = data["MonoBehaviour"]["m_tertiaryTone"]["m_color"]
            quaternaryTone = data["MonoBehaviour"]["m_quaternaryTone"]["m_color"]
            quinaryTone = data["MonoBehaviour"]["m_quinaryTone"]["m_color"]

            basename = path.basename(palette_path)
            palette[basename] = [
                rgb_to_hex(primaryTone),
                rgb_to_hex(secondaryTone),
                rgb_to_hex(tertiaryTone),
                rgb_to_hex(quaternaryTone),
                rgb_to_hex(quinaryTone),
            ]
    return palette


def extract_names(directory):
    with open(path.join(directory, "GameData_VanityItemsTemplateDataBlock_bin.json"), mode="r", encoding="utf8") as f:
        data = json.load(f)
    assert "Blocks" in data

    lang = {}
    for block in data["Blocks"]:
        basename = block["prefab"].split("/")[-1]

        if basename.startswith("Palette"):
            lang[basename] = block["publicName"]
    return lang


DIR = Path("exports")
DIR.mkdir(exist_ok=True)

with Path(DIR, "names.json").open("w+") as f:
    names = extract_names(path.dirname(__file__))
    json.dump(names, f, indent=2, sort_keys=True)

with Path(DIR, "palette.json").open("w+") as f:
    palette = extract_palette(path.dirname(__file__))
    json.dump(palette, f, indent=2, sort_keys=True)
