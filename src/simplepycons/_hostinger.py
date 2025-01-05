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


class HostingerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hostinger"

    @property
    def original_file_name(self) -> "str":
        return "hostinger.svg"

    @property
    def title(self) -> "str":
        return "Hostinger"

    @property
    def primary_color(self) -> "str":
        return "#673DE6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hostinger</title>
     <path d="M16.415 0v7.16l5.785 3.384V2.949L16.415 0ZM1.8
 0v11.237h18.815L14.89 8.09l-7.457-.003V3.024L1.8 0Zm14.615
 20.894v-5.019l-7.514-.005c.007.033-5.82-3.197-5.82-3.197l19.119.091V24l-5.785-3.106ZM1.8
 13.551v7.343l5.633 2.949v-6.988L1.8 13.551Z" />
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
