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


class ExpediaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "expedia"

    @property
    def original_file_name(self) -> "str":
        return "expedia.svg"

    @property
    def title(self) -> "str":
        return "Expedia"

    @property
    def primary_color(self) -> "str":
        return "#191E3B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Expedia</title>
     <path d="M19.067 0H4.933A4.94 4.94 0 0 0 0 4.933v14.134A4.932
 4.932 0 0 0 4.933 24h14.134A4.932 4.932 0 0 0 24 19.067V4.933C24.01
 2.213 21.797 0 19.067 0ZM7.336 19.341c0
 .19-.148.337-.337.337h-2.33a.333.333 0 0
 1-.337-.337v-2.33c0-.189.148-.336.337-.336H7c.19 0
 .337.147.337.337zm12.121-1.486-2.308
 2.298c-.169.168-.422.053-.422-.2V9.57l-6.44 6.44a.533.533 0 0
 1-.421.17H8.169a.32.32 0 0
 1-.338-.338v-1.697c0-.2.053-.316.169-.422l6.44-6.44H4.058c-.253
 0-.369-.253-.2-.421l2.297-2.309c.137-.137.285-.232.517-.232H18.15c.854
 0 1.539.686 1.539 1.54v11.478c-.01.231-.095.368-.232.516z" />
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
