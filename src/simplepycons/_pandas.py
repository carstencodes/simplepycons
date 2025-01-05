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


class PandasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pandas"

    @property
    def original_file_name(self) -> "str":
        return "pandas.svg"

    @property
    def title(self) -> "str":
        return "pandas"

    @property
    def primary_color(self) -> "str":
        return "#150458"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>pandas</title>
     <path d="M16.922 0h2.623v18.104h-2.623zm-4.126
 12.94h2.623v2.57h-2.623zm0-7.037h2.623v5.446h-2.623zm0
 11.197h2.623v5.446h-2.623zM4.456 5.896h2.622V24H4.455zm4.213
 2.559h2.623v2.57H8.67zm0
 4.151h2.623v5.447H8.67zm0-11.187h2.623v5.446H8.67Z" />
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
