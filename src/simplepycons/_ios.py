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


class IosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ios"

    @property
    def original_file_name(self) -> "str":
        return "ios.svg"

    @property
    def title(self) -> "str":
        return "iOS"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iOS</title>
     <path d="M1.1 6.05C.486 6.05 0 6.53 0 7.13A1.08 1.08 0 0 0 1.1
 8.21C1.72 8.21 2.21 7.73 2.21 7.13C2.21 6.53 1.72 6.05 1.1 6.05M8.71
 6.07C5.35 6.07 3.25 8.36 3.25 12C3.25 15.67 5.35 17.95 8.71
 17.95C12.05 17.95 14.16 15.67 14.16 12C14.16 8.36 12.05 6.07 8.71
 6.07M19.55 6.07C17.05 6.07 15.27 7.45 15.27 9.5C15.27 11.13 16.28
 12.15 18.4 12.64L19.89 13C21.34 13.33 21.93 13.81 21.93 14.64C21.93
 15.6 20.96 16.28 19.58 16.28C18.17 16.28 17.11 15.59 17
 14.53H15C15.08 16.65 16.82 17.95 19.46 17.95C22.25 17.95 24 16.58 24
 14.4C24 12.69 23 11.72 20.68 11.19L19.35 10.89C17.94 10.55 17.36 10.1
 17.36 9.34C17.36 8.38 18.24 7.74 19.54 7.74C20.85 7.74 21.75 8.39
 21.85 9.46H23.81C23.76 7.44 22.09 6.07 19.55 6.07M8.71 7.82C10.75
 7.82 12.06 9.45 12.06 12C12.06 14.57 10.75 16.2 8.71 16.2C6.65 16.2
 5.35 14.57 5.35 12C5.35 9.45 6.65 7.82 8.71 7.82M.111
 9.31V17.76H2.1V9.31H.11Z" />
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
