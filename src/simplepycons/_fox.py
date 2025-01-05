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


class FoxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fox"

    @property
    def original_file_name(self) -> "str":
        return "fox.svg"

    @property
    def title(self) -> "str":
        return "FOX"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FOX</title>
     <path d="M3.069 9.7h3.42L6.3
 6.932H0v10.136h3.069V13.8h2.789v-2.778H3.069ZM24 6.932h-3.291L19.48
 9.1l-1.231-2.168h-3.292l2.871 5.076-2.871 5.06h3.308l1.215-2.142
 1.213 2.142H24l-2.871-5.06Zm-12.592 0A5.067 5.067 0 1 0 16.475
 12a5.067 5.067 0 0 0-5.067-5.065Zm.888 7.146a.867.867 0 0
 1-.873.847.847.847 0 0 1-.837-.858V9.919a.882.882 0 0 1
 .837-.9.913.913 0 0 1 .873.9Z" />
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
