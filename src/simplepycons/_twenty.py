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


class TwentyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "twenty"

    @property
    def original_file_name(self) -> "str":
        return "twenty.svg"

    @property
    def title(self) -> "str":
        return "Twenty"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Twenty</title>
     <path d="M20.97 0H3.03A3.03 3.03 0 0 0 0 3.03v17.94A3.03 3.03 0 0
 0 3.03 24h17.94A3.03 3.03 0 0 0 24 20.97V3.03A3.03 3.03 0 0 0 20.97
 0ZM4.813 8.936a2.376 2.376 0 0 1 2.374-2.375h4.573c.067 0
 .129.04.157.103a.172.172 0 0 1-.03.185l-1.002 1.088a.924.924 0 0
 1-.678.299H7.2a.713.713 0 0 0-.713.713v1.796a.418.418 0 0
 1-.418.419h-.836a.418.418 0 0 1-.419-.419V8.936zm14.224 6.128a2.376
 2.376 0 0 1-2.374 2.375h-1.944a2.376 2.376 0 0
 1-2.375-2.375v-3.401c0-.231.087-.454.243-.625l1.134-1.23a.172.172 0 0
 1 .298.115v5.13c0 .393.32.713.713.713h1.92c.393 0
 .713-.32.713-.713V8.949a.713.713 0 0 0-.713-.713h-2.233c-.255
 0-.499.108-.674.295l-6.658 7.235h4c.232 0
 .419.187.419.418v.837a.418.418 0 0 1-.419.418h-5.39a.886.886 0 0
 1-.886-.886v-.443c0-.223.083-.436.234-.6l7.465-8.109a2.603 2.603 0 0
 1 1.916-.84h2.235a2.376 2.376 0 0 1 2.375 2.375v6.128z" />
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
