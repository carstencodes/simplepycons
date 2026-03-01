#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class LoopsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "loops"

    @property
    def original_file_name(self) -> "str":
        return "loops.svg"

    @property
    def title(self) -> "str":
        return "Loops"

    @property
    def primary_color(self) -> "str":
        return "#FC5200"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Loops</title>
     <path d="M13.608 1.622h-3.231A10.39 10.39 0 0 0 0 12.002a10.39
 10.39 0 0 0 10.377 10.376h3.243A10.39 10.39 0 0 0 24 12.001 10.39
 10.39 0 0 0 13.608 1.622M1.284 12a9.085 9.085 0 0 1 10.6-8.96 9.044
 9.044 0 0 1 7.568 8.955 5.85 5.85 0 0 1-4.87 5.756 7.12 7.12 0 0 0
 2.923-5.756 7.121 7.121 0 0 0-12.17-5.038 7.14 7.14 0 0 0-2.087 5.038
 10.35 10.35 0 0 0 4.83 8.783A9.1 9.1 0 0 1 1.291
 12zm10.704-5.606A5.83 5.83 0 0 1 16.204 12a5.83 5.83 0 0 1-4.216
 5.603A5.83 5.83 0 0 1 7.772 12a5.83 5.83 0 0 1 4.216-5.606m1.62
 14.686h-.036a9 9 0 0 1-1.474-.125 9.04 9.04 0 0
 1-7.558-8.651V12a5.844 5.844 0 0 1 4.87-5.756A7.12 7.12 0 0 0 6.485
 12a7.12 7.12 0 0 0 5.35 6.907A7.143 7.143 0 0 0 20.756 12a10.34 10.34
 0 0 0-4.828-8.784A9.086 9.086 0 0 1 22.702 12a9.086 9.086 0 0 1-9.092
 9.08" />
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
