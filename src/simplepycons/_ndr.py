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


class NdrIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ndr"

    @property
    def original_file_name(self) -> "str":
        return "ndr.svg"

    @property
    def title(self) -> "str":
        return "NDR"

    @property
    def primary_color(self) -> "str":
        return "#0C1754"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NDR</title>
     <path d="M5.184 19.325l-3.137-5.648v5.649H0V9.64h2.149l3.267
 6.025V9.641h2.047v9.684zm2.279-9.684V.537H8.61v9.104zm0
 13.822v-4.138H8.61v4.138zM12.037 9.64c2.395 0 3.63 1.147 3.63
 3.368v2.918c0 2.28-1.19 3.398-3.63 3.398H8.61V9.641zm-.19 7.855c1.163
 0 1.728-.581
 1.728-1.771v-2.498c0-1.176-.58-1.757-1.727-1.757h-1.03v6.026zm9.845
 1.83l-1.728-3.718h-1.161v3.717h-2.15V9.641h3.384c2.381 0 3.513.944
 3.513 2.962 0 1.335-.493 2.134-1.597 2.613L24
 19.326zm-1.568-5.475c.857 0 1.365-.494 1.365-1.32
 0-.858-.377-1.177-1.365-1.177H18.76v2.498h1.365z" />
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
