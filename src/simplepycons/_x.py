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


class XIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "x"

    @property
    def original_file_name(self) -> "str":
        return "x.svg"

    @property
    def title(self) -> "str":
        return "X"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>X</title>
     <path d="M14.234 10.162 22.977 0h-2.072l-7.591 8.824L7.251
 0H.258l9.168 13.343L.258 24H2.33l8.016-9.318L16.749 24h6.993zm-2.837
 3.299-.929-1.329L3.076 1.56h3.182l5.965 8.532.929 1.329 7.754
 11.09h-3.182z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://about.x.com/en/who-we-are/brand-toolk'''
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
        yield from [
            "Twitter",
        ]
