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


class RaycastIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "raycast"

    @property
    def original_file_name(self) -> "str":
        return "raycast.svg"

    @property
    def title(self) -> "str":
        return "Raycast"

    @property
    def primary_color(self) -> "str":
        return "#FF6363"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Raycast</title>
     <path d="M6.004 15.492v2.504L0 11.992l1.258-1.249Zm2.504
 2.504H6.004L12.008 24l1.253-1.253zm14.24-4.747L24 11.997 12.003 0
 10.75 1.251 15.491 6h-2.865L9.317 2.692 8.065 3.944l2.06
 2.06H8.691v9.31H18v-1.432l2.06 2.06
 1.252-1.252-3.312-3.32V8.506ZM6.63 5.372 5.38 6.625l1.342 1.343
 1.251-1.253Zm10.655 10.655-1.247 1.251 1.342 1.343 1.253-1.251zM3.944
 8.059 2.692 9.31l3.312 3.314v-2.506zm9.936 9.937h-2.504l3.314 3.312
 1.25-1.252z" />
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
