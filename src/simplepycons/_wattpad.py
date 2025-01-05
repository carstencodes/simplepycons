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


class WattpadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wattpad"

    @property
    def original_file_name(self) -> "str":
        return "wattpad.svg"

    @property
    def title(self) -> "str":
        return "Wattpad"

    @property
    def primary_color(self) -> "str":
        return "#FF500A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wattpad</title>
     <path d="M13.034 3.09c-1.695.113-3.9 2.027-6.9
 6.947.245-2.758.345-4.716-.857-5.743-.823-.702-2.764-.974-3.926.536C.18
 6.349-.09 9.312.024 12.432c.238 6.518 2.544 8.487 4.59
 8.487h.001c3.623 0 4.13-4.439 6.604-8.4-.09 1.416-.008 2.668.266
 3.532 1.078 3.398 4.784 3.663 6.467.21 2.374-4.87 3.058-6.016
 5.453-9.521 1.58-2.314-.252-3.812-2.374-2.735-1.09.554-2.86
 1.935-5.065 4.867.387-2.23.28-5.996-2.932-5.782z" />
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
