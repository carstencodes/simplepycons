#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class NamecheapIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "namecheap"

    @property
    def original_file_name(self) -> "str":
        return "namecheap.svg"

    @property
    def title(self) -> "str":
        return "Namecheap"

    @property
    def primary_color(self) -> "str":
        return "#DE3723"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Namecheap</title>
     <path d="M17.295
 17.484c.227.403.57.728.985.931-.309.15-.647.229-.99.232h-3.068a2.26
 2.26 0 0 1-1.957-1.143L6.705 6.511a2.27 2.27 0 0
 0-.974-.922c.309-.153.652-.233.997-.232h3.05c.81.003 1.558.438 1.959
 1.143l5.558 10.984zm-9.329-7.392L6.269
 6.755c-.209-.392-.582-.657-.984-.829-.204.165-.391.35-.522.581-.184.349-4.391
 8.648-4.569 8.987a2.245 2.245 0 0 0 4.016
 1.999l3.756-7.401zm15.846-1.593a2.245 2.245 0 0
 0-1.162-2.955v-.001a2.243 2.243 0 0 0-.892-.187l-.003-.011c-.816
 0-1.569.443-1.965 1.157l-3.749 7.414 1.689
 3.323c.213.399.59.664.998.839.252-.2.473-.444.605-.742l4.479-8.837z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
