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


class SvgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "svg"

    @property
    def original_file_name(self) -> "str":
        return "svg.svg"

    @property
    def title(self) -> "str":
        return "SVG"

    @property
    def primary_color(self) -> "str":
        return "#FFB13B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SVG</title>
     <path d="M12 0c-1.497 0-2.749.965-3.248 2.17a3.45 3.45 0 00-.238
 1.416 3.459 3.459 0 00-1.168-.834 3.508 3.508 0 00-1.463-.256 3.513
 3.513 0 00-2.367 1.02c-1.06 1.058-1.263 2.625-.764
 3.83.179.432.47.82.82 1.154a3.49 3.49 0 00-1.402.252C.965 9.251 0
 10.502 0 12c0 1.497.965 2.749 2.17 3.248.437.181.924.25
 1.414.236-.357.338-.65.732-.832 1.17-.499 1.205-.295 2.772.764 3.83
 1.058 1.06 2.625 1.263 3.83.764.437-.181.83-.476
 1.168-.832-.014.49.057.977.238 1.414C9.251 23.035 10.502 24 12
 24c1.497 0 2.749-.965 3.248-2.17a3.45 3.45 0
 00.238-1.416c.338.356.73.653 1.168.834 1.205.499 2.772.295 3.83-.764
 1.06-1.058 1.263-2.625.764-3.83a3.459 3.459 0 00-.834-1.168 3.45 3.45
 0 001.416-.238C23.035 14.749 24 13.498 24
 12c0-1.497-.965-2.749-2.17-3.248a3.455 3.455 0
 00-1.414-.236c.357-.338.65-.732.832-1.17.499-1.205.295-2.772-.764-3.83a3.513
 3.513 0 00-2.367-1.02 3.508 3.508 0
 00-1.463.256c-.437.181-.83.475-1.168.832a3.45 3.45 0
 00-.238-1.414C14.749.965 13.498 0 12 0zm-.041 1.613a1.902 1.902 0
 011.387 3.246v3.893L16.098 6A1.902 1.902 0 1118 7.902l-2.752
 2.752h3.893a1.902 1.902 0 110 2.692h-3.893L18 16.098A1.902 1.902 0
 1116.098 18l-2.752-2.752v3.893a1.902 1.902 0 11-2.692 0v-3.893L7.902
 18A1.902 1.902 0 116 16.098l2.752-2.752H4.859a1.902 1.902 0
 110-2.692h3.893L6 7.902A1.902 1.902 0 117.902 6l2.752
 2.752V4.859a1.902 1.902 0 011.305-3.246z" />
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
