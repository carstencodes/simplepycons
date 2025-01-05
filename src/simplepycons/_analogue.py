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


class AnalogueIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "analogue"

    @property
    def original_file_name(self) -> "str":
        return "analogue.svg"

    @property
    def title(self) -> "str":
        return "Analogue"

    @property
    def primary_color(self) -> "str":
        return "#1A1A1A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Analogue</title>
     <path d="M5.468 12.804a5.145 5.145 0 10-.644 10.27 5.145 5.145 0
 00.644-10.27zm17.841 2.562L16.45 3.484a5.146 5.146 0 00-8.912
 5.15l6.86 11.878a5.148 5.148 0 007.031 1.885 5.146 5.146 0
 001.881-7.031z" />
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
