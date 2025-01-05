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


class RollupdotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rollupdotjs"

    @property
    def original_file_name(self) -> "str":
        return "rollupdotjs.svg"

    @property
    def title(self) -> "str":
        return "rollup.js"

    @property
    def primary_color(self) -> "str":
        return "#EC4A3F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>rollup.js</title>
     <path d="M3.42.0002a.37.37 0 00-.369.37V19.885c.577-1.488
 1.557-3.6168 3.1378-6.5297C11.8885 2.876 12.6355 1.8191 15.6043
 1.8191c1.56 0 3.1338.704 4.1518 1.9549A7.9616 7.9616 0
 0013.1014.0002zM16.1393 2.544c-1.19.01-2.257.466-2.6979 1.498-.967
 2.2558 1.624 4.7667 2.7569 4.5677 1.4419-.255-.255-3.5628-.255-3.5628
 2.2049 4.1558 1.6969 2.8838-2.2899 6.6996C9.6666 15.5623 5.596
 23.6188 5.002 23.9568a.477.477 0 01-.08.043H20.558a.373.373 0
 00.33-.538l-4.0878-8.0915a.37.37 0 01.144-.488 7.9596 7.9596 0
 004.0048-6.9126c0-1.4249-.373-2.7608-1.03-3.9198-.9269-.9519-2.4298-1.5159-3.7787-1.5059z"
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
