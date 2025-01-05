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


class KiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kia"

    @property
    def original_file_name(self) -> "str":
        return "kia.svg"

    @property
    def title(self) -> "str":
        return "Kia"

    @property
    def primary_color(self) -> "str":
        return "#05141F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kia</title>
     <path d="M13.923 14.175c0 .046.015.072.041.072a.123.123 0 0 0
 .058-.024l7.48-4.854a.72.72 0 0 1 .432-.13h1.644c.252 0
 .422.168.422.42v3.139c0 .38-.084.6-.42.801l-1.994 1.2a.137.137 0 0
 1-.067.024c-.024
 0-.048-.019-.048-.088v-3.663c0-.043-.012-.071-.041-.071a.113.113 0 0
 0-.058.024l-5.466 3.551a.733.733 0 0 1-.42.127h-3.624c-.254
 0-.422-.168-.422-.422V9.757c0-.033-.015-.064-.044-.064a.118.118 0 0
 0-.057.024L7.732 11.88c-.036.024-.046.041-.046.058 0
 .014.008.029.032.055l2.577 2.575c.034.034.058.06.058.089 0
 .024-.039.043-.084.043H7.94c-.183
 0-.324-.026-.423-.125l-1.562-1.56a.067.067 0 0 0-.048-.024.103.103 0
 0 0-.048.015l-2.61 1.57a.72.72 0 0 1-.423.122H.425C.168 14.7 0 14.53
 0 14.279v-3.08c0-.38.084-.6.422-.8L2.43 9.192a.103.103 0 0 1
 .052-.016c.032 0 .048.03.048.1V13.4c0 .043.01.063.041.063a.144.144 0
 0 0 .06-.024L9.407 9.36a.733.733 0 0 1 .446-.124h3.648c.252 0
 .422.168.422.42l-.002 4.518z" />
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
