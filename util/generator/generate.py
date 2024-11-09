#!/usr/bin/env python3
#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#

from datetime import datetime
from json import load as json_load
from pathlib import Path
from string import Template
from sys import stderr
from typing import IO
from unicodedata import normalize, category
from xml.etree import ElementTree as ET

from num2words import num2words


ET.register_namespace('', "http://www.w3.org/2000/svg")


def normalize_name(arbitrary: str, short_name: str | None = None, build_index: bool = True) -> str:
    def unicode_to_ascii(s: str) -> str:
        normal_form_d = "NFD"
        non_marking_mark = "Mn"

        return ''.join(
            c for c in normalize(normal_form_d, s) if category(c) != non_marking_mark
        )

    if short_name is not None:
        return short_name

    if not build_index:
        arbitrary = " ".join([s.capitalize() for s in arbitrary.split(" ")])

    removals = {
        " ",
        "-",
        "'",
        "°",
        "/",
        "!",
        "_",
        ":"
    }

    replacements = {
        "+": "plus",
        "&": "and",
        ".": "dot",
        "#": "Sharp",
    }

    for remove in removals:
        arbitrary = arbitrary.replace(remove, "")

    for old, new in replacements.items():
        arbitrary = arbitrary.replace(old, new)

    arbitrary = unicode_to_ascii(arbitrary)

    if build_index:
        arbitrary = arbitrary.lower()

    return arbitrary


def create_class_name(normalized_name: str) -> str:
    numbers: list[int] = []

    number: str = ""
    word: str = ""
    for c in normalized_name:
        if c.isdigit():
            number += c
        elif len(number) > 0:
            num = int(number)
            number = ""
            numbers.append(num)
            c = c.upper()

        word += c

    normalized_name = word

    if len(number) > 0:
        num = int(number)
        numbers.append(num)

    if len(numbers) > 0:
        numbers.sort()
        numbers_and_words = {n: num2words(n) for n in numbers}

        for numeric, word in numbers_and_words.items():
            replacement = word.replace("-", " ")
            replacement = "".join(s.capitalize() for s in replacement.split(" "))
            normalized_name = normalized_name.replace(str(numeric), replacement)

    if normalized_name[0].islower():
        normalized_name = normalized_name[0].upper() + normalized_name[1:]

    return f"{normalized_name}Icon"


def format_icon_text(text: str) -> str:
    element = ET.fromstring(text)
    ET.indent(element, space="    ", level=0)
    text: str = ET.tostring(element, encoding="unicode", method="xml")
    lines = text.splitlines()

    resulting_lines = []
    split_after = 45
    for line in lines:
        if len(line) > split_after:
            line_items = line.split(" ")
            part = ""
            for line_item in line_items:
                if (len(line_item) + 1 + len(part)) > split_after:
                    resulting_lines.append(part)
                    part = f" {line_item}"
                else:
                    part = f"{part} {line_item}"
            if len(part) > 0:
                resulting_lines.append(part)
            split_after = 70
        else:
            resulting_lines.append(line)

    resulting_lines = [ln for ln in resulting_lines if len(ln.strip()) > 0]

    return "\n".join(resulting_lines)


def hard_line_break(text: str) -> str:
    split_after = 45
    line = ""
    while len(text) > split_after:
        head, text = text[:split_after], text[split_after:]
        split_after = 70
        line = f"{line}\n{head}"

    return line.strip()


def soft_line_break(items: list[str]) -> str:
    if len(items) > 0:
        lines = ["["]
        lines.extend([f"            \"{i}\"," for i in items])
        lines.append("        ]")
        return "\n".join(lines)

    return "[]"


def import_line_break(import_line: str) -> str:
    if len(import_line) > 79:
        from_kw, file, import_kw, cls_name = tuple(import_line.split(" ", 4))
        return f"{from_kw} {file} {import_kw} (\n    {cls_name.strip()}\n)\n"

    return import_line


def add_license_header(writer: IO[str]) -> None:
    writer.write(f"""#
# SPDX-License-Identifier: MIT
#
# Copyright (c) {datetime.now().year} Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""")


current_dir = Path(__file__).parent.absolute().resolve()
project_dir = current_dir.parent.parent.absolute().resolve()

src_package_dir = project_dir / "src" / "simplepycons"

icons_module_dir = project_dir / "vendor" / "simple-icons"
data_file = icons_module_dir / "_data" / "simple-icons.json"
icons_dir = icons_module_dir / "icons"

for code_file in src_package_dir.glob("_*.py"):
    if code_file.exists() and code_file.is_file() and not code_file.stem.startswith("__"):
        code_file.unlink(True)

with open(data_file, "r") as f:
    icon_data = json_load(f)

icons_by_titles = icon_data["icons"]
icons_by_titles = {normalize_name(i["title"], i.get("slug", None)): i for i in icons_by_titles}

icons_files = icons_dir.glob("*.svg")

class_template = Template(
    """# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class $class_name(Icon):
    $class_docstring
    @property
    def name(self) -> "str":
        return "$icon_name"

    @property
    def original_file_name(self) -> "str":
        return "$file_name"

    @property
    def title(self) -> "str":
        return "$title"

    @property
    def primary_color(self) -> "str":
        return "#$hex"

    @property
    def raw_svg(self) -> "str":
        return '''$raw_text'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''$guidelines'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''$source'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = '''$license_type'''
        _url: "str | None" = '''$license_url'''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from $aliases
"""
)

module_doc_template = Template('''""""""\n''')
class_doc_template = Template('''""""""''')


all_icons = {}
missing_info = False
class_names = {}

for icon_file in icons_files:
    with (open(str(icon_file), "r") as f):
        icon_text = f.read()
        icon_name = icon_file.stem

        canonical_icon_name = icon_name.lower()

        all_icons[canonical_icon_name] = {
            "title": icon_name,
            "hex": "MISSING",
            "source": "unknown",
            "guidelines": "NONE",
            "license_type": "",
            "license_url": "",
            "aliases": [],
        }

        icon_text = format_icon_text(icon_text)

        all_icons[canonical_icon_name]["file_name"] = icon_file.name
        all_icons[canonical_icon_name]["raw_text"] = icon_text
        all_icons[canonical_icon_name]["icon_name"] = icon_name

        if canonical_icon_name in icons_by_titles:
            all_icons[canonical_icon_name].update(icons_by_titles[canonical_icon_name])
            for key in ("source", "guidelines"):
                all_icons[canonical_icon_name][key] = hard_line_break(all_icons[canonical_icon_name][key])

            if "aliases" in icons_by_titles[canonical_icon_name]:
                if "aka" in icons_by_titles[canonical_icon_name]["aliases"]:
                    all_icons[canonical_icon_name]["aliases"] = soft_line_break(
                        icons_by_titles[canonical_icon_name]["aliases"]["aka"]
                    )
                else:
                    all_icons[canonical_icon_name]["aliases"] = []
            if "license" in icons_by_titles[canonical_icon_name]:
                for key in ("url", "type"):
                    if key in icons_by_titles[canonical_icon_name]["license"]:
                        icons_by_titles[canonical_icon_name][f"license_{key}"] = hard_line_break(
                            all_icons[canonical_icon_name]["license"][key])
        else:
            print(f"Failed to get icon meta data for {canonical_icon_name} from icon file {icon_file}", file=stderr)
            missing_info = True

        class_name = normalize_name(all_icons[canonical_icon_name]["title"], None, False)
        class_name = create_class_name(class_name)
        ctr = 1
        ocn = class_name
        while class_name in class_names:
            class_name = ocn + str(ctr)
            print(
                f"class {ocn} has already been create for {class_names[ocn]}.\n"
                f"  Trying to generate {class_name} for {icon_file}",
                file=stderr)
            ctr += 1

        all_icons[canonical_icon_name]["class_name"] = class_name
        class_names[class_name] = icon_file


_init_py = src_package_dir / "__init__.py"

all_template_vars = class_template.get_identifiers()

generated = []

for f_name, icon_data in all_icons.items():
    name = f_name
    if "icon_name" in icon_data:
        name = icon_data["icon_name"]

    file_name = f"_{name}.py"

    file_path = src_package_dir / file_name
    icon_data["class_docstring"] = class_doc_template.substitute(**icon_data)

    missing_data = [v for v in all_template_vars if v not in icon_data]
    if len(missing_data) > 0:
        print(f"Data missing {missing_data} for {name}", file=stderr)
        continue

    with file_path.open("w") as f:
        add_license_header(f)
        f.write(module_doc_template.substitute(**icon_data))
        f.write(class_template.substitute(**icon_data))

    generated.append((f"_{name}", icon_data["class_name"]))

all_icons_file = src_package_dir / "all.py"

registry_file = src_package_dir / "registry.py"
registry_file_type_hints = src_package_dir / "registry.pyi"

with all_icons_file.open("w") as f:
    add_license_header(f)
    f.write('""""""\n')
    f.write("# pylint: disable=C0302\n")
    f.write("# Justification: Code is generated\n")
    f.write("\n\n")

    f.write("from typing import TYPE_CHECKING\n")
    f.write("\n")
    for data in generated:
        f.write(import_line_break(f"from .{data[0]} import {data[1]}\n"))

    f.write("\n")

    f.write("if TYPE_CHECKING:\n")
    f.write("    from typing import Final\n")

    f.write("\n\n")

    f.write("ALL_ICONS: \"Final[list[str]]\" = [\n")
    for data in generated:
        f.write(f"    {data[1]}.__name__,\n")
    f.write("]\n\n")
    f.write("__all__: \"Final[list[str]]\" = [\"ALL_ICONS\"] + ALL_ICONS\n\n")

with registry_file.open("w") as f:
    add_license_header(f)
    f.write('""""""\n')
    f.write("# pylint: disable=C0302\n")
    f.write("# Justification: Code is generated\n")
    f.write("\n\n")

    f.write("from typing import TYPE_CHECKING\n")
    f.write("from .icons import IconCollection\n")
    for data in generated:
        f.write(import_line_break(f"from .{data[0]} import {data[1]}\n"))

    f.write("\n")

    f.write("if TYPE_CHECKING:\n")
    f.write("    from typing import Final\n")

    f.write("\n\n")

    f.write("ICONS: \"Final[IconCollection]\" = IconCollection({\n")
    for data in generated:
        f.write(f"    '{data[0].lstrip('_')}': {data[1]},\n")
    f.write("})\n\n")
    f.write("__all__: \"Final[list[str]]\" = [\"ICONS\"]\n\n")

with registry_file_type_hints.open("w") as f:
    add_license_header(f)
    f.write('""""""\n')
    f.write("# pylint: disable=C0302\n")
    f.write("# Justification: Code is generated\n")
    f.write("\n\n")

    f.write("from typing import Final\n")
    f.write("from .icons import IconFactory\n")

    f.write("\n\n")
    f.write("class _IconCollection:\n")
    f.write("    __name__: \"Final[str]\"\n")
    for data in generated:
        f.write(f"    get_{data[0].lstrip('_')}_icon: \"Final[IconFactory]\"\n")

    f.write("\n\nICONS: \"Final[_IconCollection]\"\n\n")

if missing_info:
    raise SystemExit(1)
