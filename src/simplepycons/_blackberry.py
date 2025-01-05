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


class BlackberryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "blackberry"

    @property
    def original_file_name(self) -> "str":
        return "blackberry.svg"

    @property
    def title(self) -> "str":
        return "Blackberry"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Blackberry</title>
     <path d="M2.05 3.54L1.17 7.7H4.45C6.97 7.7 7.73 6.47 7.73
 5.36C7.73 4.54 7.26 3.54 5.21 3.54H2.05M10.54 3.54L9.66
 7.7H12.94C15.5 7.7 16.22 6.47 16.22 5.36C16.22 4.54 15.75 3.54 13.7
 3.54H10.54M18.32 7.23L17.39 11.39H20.67C23.24 11.39 24 10.22 24
 9.05C24 8.23 23.53 7.23 21.5 7.23H18.32M.88 9.8L0 13.96H3.28C5.85
 13.96 6.56 12.73 6.56 11.62C6.56 10.8 6.09 9.8 4.04 9.8H.88M9.43
 9.8L8.5 13.96H11.77C14.34 13.96 15.11 12.73 15.11 11.62C15.11 10.8
 14.64 9.8 12.59 9.8H9.42M17.09 13.73L16.22 17.88H19.5C22 17.88 22.77
 16.71 22.77 15.54C22.77 14.72 22.3 13.73 20.26 13.73H17.09M8.2
 16.3L7.32 20.46H10.6C13.11 20.46 13.87 19.23 13.87 18.12C13.87 17.3
 13.41 16.3 11.36 16.3H8.2Z" />
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
