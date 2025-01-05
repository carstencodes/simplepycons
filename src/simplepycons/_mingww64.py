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


class MingwwSixtyFourIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mingww64"

    @property
    def original_file_name(self) -> "str":
        return "mingww64.svg"

    @property
    def title(self) -> "str":
        return "MinGW-w64"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MinGW-w64</title>
     <path d="m -3e-4,9.3955 4.187,-4.187 4.1869,4.187 -4.187,4.187 z
 m 0,10.417 4.187,-4.1869 4.1869,4.187 -4.187,4.1869 z m
 5.2086,-5.2085 4.1869,-4.187 4.187,4.187 -4.187,4.187 z m 0,-10.417 L
 9.3953,0 13.5822,4.187 9.3952,8.3738 Z m 5.2085,5.2084 4.187,-4.1869
 4.1869,4.187 -4.187,4.1869 z M 15.6253,4.187 19.8123,0 l 4.1869,4.187
 -4.187,4.1869 z m -5.208,15.626 4.187,-4.1869 4.1869,4.187 L
 14.6042,24 Z m 5.2086,-5.2085 4.187,-4.187 4.1868,4.187 -4.1869,4.187
 z" />
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
