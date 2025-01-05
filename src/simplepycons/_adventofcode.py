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


class AdventOfCodeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adventofcode"

    @property
    def original_file_name(self) -> "str":
        return "adventofcode.svg"

    @property
    def title(self) -> "str":
        return "Advent Of Code"

    @property
    def primary_color(self) -> "str":
        return "#FFFF66"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Advent Of Code</title>
     <path d="m14.05 13.236 6.498 9.606L18.91 24l-6.905-9.47L5.1
 24l-1.637-1.158 6.498-9.606L.553 9.22l.615-1.69 9.596 3.463L11.087
 0h1.826l.323 10.993 9.596-3.462.615 1.69-9.387 4.015z" />
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
