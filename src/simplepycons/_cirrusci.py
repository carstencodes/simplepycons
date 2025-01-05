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


class CirrusCiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cirrusci"

    @property
    def original_file_name(self) -> "str":
        return "cirrusci.svg"

    @property
    def title(self) -> "str":
        return "Cirrus CI"

    @property
    def primary_color(self) -> "str":
        return "#4051B5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cirrus CI</title>
     <path d="M19.422.453a1.113 1.113 0 0 0-1.113 1.115 1.113 1.113 0
 0 0 1.112 1.114c1.31 0 2.35 1.042 2.35 2.363 0 1.32-1.04 2.363-2.35
 2.363H1.112A1.113 1.113 0 0 0 0 8.52a1.113 1.113 0 0 0 1.113
 1.117h18.31c1.308 0 2.35 1.042 2.35 2.363 0 1.32-1.042 2.363-2.35
 2.363H1.112A1.113 1.113 0 0 0 0 15.48a1.113 1.113 0 0 0 1.113
 1.112h18.31c1.308 0 2.35 1.042 2.35 2.363 0 1.32-1.042 2.363-2.35
 2.363H1.112A1.113 1.113 0 0 0 0 22.432a1.113 1.113 0 0 0 1.113
 1.115h18.31a1.113 1.113 0 0 0 .206-.022c2.42-.112 4.37-2.12 4.37-4.57
 0-1.393-.642-2.634-1.63-3.478C23.356 14.632 24 13.393 24
 12c0-1.393-.643-2.632-1.63-3.477C23.357 7.68 24 6.438 24
 5.045c0-2.52-2.06-4.592-4.578-4.592z" />
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
