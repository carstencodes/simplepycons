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


class TripdotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tripdotcom"

    @property
    def original_file_name(self) -> "str":
        return "tripdotcom.svg"

    @property
    def title(self) -> "str":
        return "Trip.com"

    @property
    def primary_color(self) -> "str":
        return "#287DFA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trip.com</title>
     <path d="M17.834 9.002c-.68
 0-1.29.31-1.707.799v-.514h-1.708v8.348h1.897v-2.923c.416.344.943.551
 1.518.551 1.677 0 3.036-1.401 3.036-3.13s-1.36-3.13-3.036-3.13zm-.19
 4.516c-.733 0-1.328-.62-1.328-1.385s.595-1.385 1.328-1.385c.734 0
 1.328.62 1.328 1.385s-.594 1.385-1.328 1.385zm6.356.607a1.138 1.138 0
 1 1-2.277 0 1.138 1.138 0 0 1 2.277 0zM13.205 7.428a1.062 1.062 0 1
 1-2.125 0 1.062 1.062 0 0 1 2.125 0zm-2.011
 1.859h1.897v5.692h-1.897V9.287zM6.83
 8.225H4.364v6.754H2.466V8.225H0V6.63h6.83v1.594zm3.035 1.033c.13 0
 .255.012.38.03v1.74a1.55 1.55 0 0 0-.297-.031c-.88 0-1.594.612-1.594
 1.593v2.389H6.451V9.287h1.707v.9c.363-.558.991-.93 1.707-.93z" />
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
