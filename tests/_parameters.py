import json
import pathlib

from unicodedata import normalize, category

from num2words import num2words

def _normalize_name(arbitrary: str, short_name: str | None = None, build_index: bool = True) -> str:
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


def _create_class_name(normalized_name: str) -> str:
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

def _load_icons():
    _path = pathlib.Path(".").parent / "vendor" / "simple-icons" / "data" / "simple-icons.json"

    with _path.open("rb") as fp:
        _icons = json.load(fp)

    _icon_names = [ (i["title"], i.get("slug", None)) for i in _icons ]

    return _icon_names


_names = _load_icons()

normalized_names = [_normalize_name(n, s) for (n, s) in _names]
icon_class_names = [_create_class_name(_normalize_name(n, None, False)) for (n, _) in _names]
get_method_names = ["get_" + n + "_icon" for n in normalized_names]

