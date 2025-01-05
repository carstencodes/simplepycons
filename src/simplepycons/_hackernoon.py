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


class HackerNoonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hackernoon"

    @property
    def original_file_name(self) -> "str":
        return "hackernoon.svg"

    @property
    def title(self) -> "str":
        return "Hacker Noon"

    @property
    def primary_color(self) -> "str":
        return "#00FE00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hacker Noon</title>
     <path d="M5.701
 0v6.223H8.85V4.654h1.576v7.842H12V4.654h1.574v1.569h3.15V0zm11.024
 6.223v3.136h1.574V6.223zm1.574
 3.136v4.705h1.576v-1.568h1.574v-1.568h-1.574V9.359zm0
 4.705h-1.574v3.137h1.574zm-1.574
 3.137h-3.15v1.569H8.85V17.2H5.7V24h11.024zm-11.024
 0v-3.137H4.125v3.137zm-1.576-3.137V9.36H2.551v4.705zm0-4.705h1.576V6.223H4.125Z"
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
