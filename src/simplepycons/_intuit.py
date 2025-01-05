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


class IntuitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "intuit"

    @property
    def original_file_name(self) -> "str":
        return "intuit.svg"

    @property
    def title(self) -> "str":
        return "Intuit"

    @property
    def primary_color(self) -> "str":
        return "#236CFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Intuit</title>
     <path d="M12.32 12.38c0 1.174.974 2.033 2.211 2.033 1.237 0
 2.212-.859 2.212-2.033v-2.7h-1.198v2.56c0 .633-.44 1.06-1.017
 1.06s-1.017-.424-1.017-1.06V9.68h-1.198l.008
 2.699zm7.624-1.619h1.429v3.563h1.198V10.76H24V9.68h-4.056v1.082zM19.17
 9.68h-1.198v4.645h1.198V9.679zM7.482
 10.761h1.43v3.563h1.197V10.76h1.428V9.68H7.482v1.082zM1.198
 9.68H0v4.645h1.198V9.679zm5.653
 1.94c0-1.174-.974-2.032-2.212-2.032-1.238 0-2.212.858-2.212
 2.032v2.705h1.198v-2.56c0-.633.44-1.06 1.017-1.06s1.018.425 1.018
 1.06v2.56h1.197L6.85 11.62h.001z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.intuit.com/company/press-room/log'''
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
