#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class TrendMicroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trendmicro"

    @property
    def original_file_name(self) -> "str":
        return "trendmicro.svg"

    @property
    def title(self) -> "str":
        return "Trend Micro"

    @property
    def primary_color(self) -> "str":
        return "#D71921"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trend Micro</title>
     <path d="M12 0C5.38 0 0 5.37 0 12C0 14.45 .734 16.72 2 18.62C1.5
 17.45 1.58 15.94 2.19 14.29L2.2 14.25L2.25 14.12L2.3 14L2.32
 13.95C2.54 13.4 2.82 12.83 3.16 12.26C3.21 12.16 3.25 12.07 3.3
 12L1.86 12L2.21 11.21C3.4 10.88 5.38 10.22 7.27 8.39L7.32
 8.39H8.32L7.03 11.14L9.1 11.14L8.72 11.96L6.66 11.96S5.69 13.9 5.36
 15.28C5.11 16.82 5.36 18 6.74 18.41C7.59 18.67 8.66 18.61 9.81
 18.29C12.5 17.45 15.34 15.62 17.43 13.18C20.87 9.19 20.94 5.1 17.58
 4.05C15.43 3.38 12.39 4.13 9.58 5.8C13.08 3.54 16.94 2.5 19.59
 3.31C20.09 3.46 20.53 3.68 20.89 3.94A11.97 11.97 0 0 0 12 0M22.17
 5.63C23 7.81 21.97 11.07 19.2 14.29C15.04 19.13 8.47 22.05 4.5
 20.83A4.46 4.46 0 0 1 3.24 20.21A11.96 11.96 0 0 0 12 24C18.63 24 24
 18.63 24 12C24 9.66 23.33 7.5 22.17 5.63Z" />
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