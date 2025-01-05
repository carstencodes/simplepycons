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


class DThreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "d3"

    @property
    def original_file_name(self) -> "str":
        return "d3.svg"

    @property
    def title(self) -> "str":
        return "D3"

    @property
    def primary_color(self) -> "str":
        return "#F9A03C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>D3</title>
     <path d="M13.312 12C13.312 5.718 8.22.625
 1.937.625H0v5h1.938c3.521 0 6.375 2.854 6.375 6.375s-2.854
 6.375-6.375 6.375H0v5h1.938c6.281 0 11.374-5.093 11.374-11.375zM24
 7.563C24 3.731 20.893.625 17.062.625h-8a13.4154 13.4154 0 0 1 4.686
 5h3.314c1.069 0 1.938.868 1.938 1.938 0 1.07-.869 1.938-1.938
 1.938h-1.938c.313 1.652.313 3.348 0 5h1.938c1.068 0 1.938.867 1.938
 1.938s-.869 1.938-1.938 1.938h-3.314a13.4154 13.4154 0 0 1-4.686
 5h8c1.621 0 3.191-.568 4.438-1.605 2.943-2.45
 3.346-6.824.895-9.77A6.9459 6.9459 0 0 0 24 7.563z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/d3/d3-logo/tree/6d9c471aa8'''

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
            "D3.js",
        ]
