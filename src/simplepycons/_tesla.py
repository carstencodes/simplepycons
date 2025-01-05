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


class TeslaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tesla"

    @property
    def original_file_name(self) -> "str":
        return "tesla.svg"

    @property
    def title(self) -> "str":
        return "Tesla"

    @property
    def primary_color(self) -> "str":
        return "#CC0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tesla</title>
     <path d="M12 5.362l2.475-3.026s4.245.09 8.471 2.054c-1.082
 1.636-3.231 2.438-3.231 2.438-.146-1.439-1.154-1.79-4.354-1.79L12 24
 8.619 5.034c-3.18 0-4.188.354-4.335 1.792 0
 0-2.146-.795-3.229-2.43C5.28 2.431 9.525 2.34 9.525 2.34L12
 5.362l-.004.002H12v-.002zm0-3.899c3.415-.03 7.326.528 11.328
 2.28.535-.968.672-1.395.672-1.395C19.625.612 15.528.015 12 0
 8.472.015 4.375.61 0 2.349c0 0 .195.525.672 1.396C4.674 1.989 8.585
 1.435 12 1.46v.003z" />
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
