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


class CssThreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "css3"

    @property
    def original_file_name(self) -> "str":
        return "css3.svg"

    @property
    def title(self) -> "str":
        return "CSS3"

    @property
    def primary_color(self) -> "str":
        return "#1572B6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CSS3</title>
     <path d="M1.5 0h21l-1.91 21.563L11.977 24l-8.565-2.438L1.5
 0zm17.09 4.413L5.41 4.41l.213 2.622 10.125.002-.255 2.716h-6.64l.24
 2.573h6.182l-.366 3.523-2.91.804-2.956-.81-.188-2.11h-2.61l.29
 3.855L12 19.288l5.373-1.53L18.59 4.414z" />
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
