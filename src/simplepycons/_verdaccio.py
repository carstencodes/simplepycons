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


class VerdaccioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "verdaccio"

    @property
    def original_file_name(self) -> "str":
        return "verdaccio.svg"

    @property
    def title(self) -> "str":
        return "Verdaccio"

    @property
    def primary_color(self) -> "str":
        return "#4B5E40"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Verdaccio</title>
     <path d="M17.376 9.84L18.72
 7.2h-4.8v.566h.864l-.192.377H12.96v.566h1.344l-.288.565H12v.566h1.728zm-4.255
 8.64l3.68-7.265h-3.68l-1.064 2.103L8.959 7.2H5.28l5.712 11.28zM8.88
 0h6.24A8.86 8.86 0 0124 8.88v6.24A8.86 8.86 0 0115.12 24H8.88A8.86
 8.86 0 010 15.12V8.88A8.86 8.86 0 018.88 0z" />
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
