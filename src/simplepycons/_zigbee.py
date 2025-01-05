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


class ZigbeeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zigbee"

    @property
    def original_file_name(self) -> "str":
        return "zigbee.svg"

    @property
    def title(self) -> "str":
        return "Zigbee"

    @property
    def primary_color(self) -> "str":
        return "#EB0443"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zigbee</title>
     <path d="M11.988 0a11.85 11.85 0 00-8.617 3.696c7.02-.875
 11.401-.583 13.289-.34 3.752.583 3.558 3.404 3.558 3.404L8.237
 19.112c2.299.22 6.897.366 13.796-.631a11.86 11.86 0
 001.912-6.469C23.945 5.374 18.595 0 11.988 0zm.232
 4.31c-2.451-.014-5.772.146-9.963.723C.854 7.003.055 9.41.055
 12.012.055 18.626 5.38 24 11.988 24c3.63 0 6.85-1.63
 9.053-4.182-7.286.948-11.813.631-13.75.388-3.775-.56-3.557-3.404-3.557-3.404L15.691
 4.474a38.635 38.635 0 00-3.471-.163Z" />
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
