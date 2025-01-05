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


class StackOverflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stackoverflow"

    @property
    def original_file_name(self) -> "str":
        return "stackoverflow.svg"

    @property
    def title(self) -> "str":
        return "Stack Overflow"

    @property
    def primary_color(self) -> "str":
        return "#F58025"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stack Overflow</title>
     <path d="M15.725 0l-1.72 1.277 6.39 8.588 1.716-1.277L15.725
 0zm-3.94 3.418l-1.369 1.644 8.225 6.85 1.369-1.644-8.225-6.85zm-3.15
 4.465l-.905 1.94 9.702 4.517.904-1.94-9.701-4.517zm-1.85 4.86l-.44
 2.093 10.473 2.201.44-2.092-10.473-2.203zM1.89
 15.47V24h19.19v-8.53h-2.133v6.397H4.021v-6.396H1.89zm4.265
 2.133v2.13h10.66v-2.13H6.154Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://stackoverflow.com/legal/trademark-gui'''
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
