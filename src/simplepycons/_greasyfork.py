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


class GreasyForkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "greasyfork"

    @property
    def original_file_name(self) -> "str":
        return "greasyfork.svg"

    @property
    def title(self) -> "str":
        return "Greasy Fork"

    @property
    def primary_color(self) -> "str":
        return "#670000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Greasy Fork</title>
     <path d="M5.89 2.227a.28.28 0 0 1 .266.076l5.063 5.062c.54.54.509
 1.652-.031 2.192l8.771 8.77c1.356 1.355-.36 3.097-1.73
 1.728l-8.772-8.77c-.54.54-1.651.571-2.191.031l-5.063-5.06c-.304-.304.304-.911.608-.608l3.714
 3.713L7.59 8.297 3.875 4.582c-.304-.304.304-.911.607-.607l3.715 3.714
 1.067-1.066L5.549 2.91c-.228-.228.057-.626.342-.683ZM12 0C5.374 0 0
 5.375 0 12s5.374 12 12 12c6.625 0 12-5.375 12-12S18.625 0 12 0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/JasonBarnabe/greasyfork/bl'''

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
