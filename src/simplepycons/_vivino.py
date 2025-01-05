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


class VivinoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vivino"

    @property
    def original_file_name(self) -> "str":
        return "vivino.svg"

    @property
    def title(self) -> "str":
        return "Vivino"

    @property
    def primary_color(self) -> "str":
        return "#A61A30"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vivino</title>
     <path d="M12.476 18.034c0-1.087.889-1.989 1.988-1.989 1.1 0
 1.989.902 1.989 1.989 0 1.1-.89 1.989-1.989 1.989-1.1
 0-1.988-.89-1.988-1.99M12.043 24c-1.1 0-1.988-.902-1.988-1.989
 0-1.099.889-1.988 1.988-1.988 1.087 0 1.989.889 1.989 1.988A2.003
 2.003 0 0112.043 24M5.2 14.007c0-1.087.89-1.988 1.989-1.988 1.087 0
 1.989.901 1.989 1.988 0 1.1-.902 1.989-1.99 1.989-1.098
 0-1.988-.89-1.988-1.989m4.385-5.892c1.1 0 1.989.902 1.989 1.989 0
 1.1-.89 1.976-1.989 1.976-1.1 0-1.988-.877-1.988-1.976
 0-1.087.889-1.989 1.988-1.989m2.384-4.187c1.1 0 1.989.89 1.989 1.989
 0 1.087-.89 1.988-1.989 1.988A2.003 2.003 0 019.98
 5.917c0-1.1.902-1.99 1.99-1.99M14.401 0c1.1 0 1.99.89 1.99 1.989 0
 1.087-.89 1.988-1.99 1.988a2.003 2.003 0
 01-1.988-1.988c0-1.1.901-1.989 1.988-1.989M11.6 18.034c0 1.1-.89
 1.989-1.99 1.989a1.995 1.995 0 01-1.988-1.99c0-1.086.902-1.988
 1.989-1.988 1.1 0 1.989.902 1.989
 1.989m-1.544-4.027c0-1.087.889-1.988 1.988-1.988 1.087 0 1.989.901
 1.989 1.988 0 1.1-.902 1.989-1.989 1.989-1.1
 0-1.988-.89-1.988-1.989m4.385-1.927c-1.1 0-1.99-.877-1.99-1.976
 0-1.087.89-1.989 1.99-1.989 1.099 0 1.988.902 1.988 1.989 0 1.1-.89
 1.976-1.988 1.976m4.36 1.927c0 1.1-.89 1.989-1.989 1.989-1.1
 0-1.989-.89-1.989-1.989 0-1.087.89-1.988 1.99-1.988 1.098 0 1.988.901
 1.988 1.988Z" />
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
