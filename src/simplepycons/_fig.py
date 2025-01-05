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


class FigIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fig"

    @property
    def original_file_name(self) -> "str":
        return "fig.svg"

    @property
    def title(self) -> "str":
        return "Fig"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fig</title>
     <path d="M4.543 0A4.543 4.543 0 0 0 0 4.543v14.914A4.543 4.543 0
 0 0 4.543 24h14.914A4.543 4.543 0 0 0 24 19.457V4.543A4.543 4.543 0 0
 0 19.457 0H4.543zm10.715 2.572h3.086a3.326 3.326 0 0 1 .656.065 3.28
 3.28 0 0 1
 .898.326c.093.05.181.106.268.164.087.058.172.12.252.186a3.264 3.264 0
 0 1 .789.96c.05.093.098.188.139.286a3.21 3.21 0 0 1 .187.61 3.276
 3.276 0 0 1 .067.66v12.343a3.276 3.276 0 0 1-.146.97 3.21 3.21 0 0
 1-.108.3 3.259 3.259 0 0 1-.301.552 3.28 3.28 0 0
 1-.627.694c-.08.066-.165.127-.252.185a3.242 3.242 0 0 1-.553.3 3.222
 3.222 0 0 1-1.27.255h-3.085a3.326 3.326 0 0 1-.658-.065 3.242 3.242 0
 0 1-2.344-1.922 3.222 3.222 0 0 1-.256-1.27V5.829a3.324 3.324 0 0 1
 .393-1.555 3.221 3.221 0 0 1 1.04-1.146 3.241 3.241 0 0 1 .553-.3
 3.26 3.26 0 0 1 1.272-.255z" />
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
