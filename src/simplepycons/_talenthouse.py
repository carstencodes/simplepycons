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


class TalenthouseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "talenthouse"

    @property
    def original_file_name(self) -> "str":
        return "talenthouse.svg"

    @property
    def title(self) -> "str":
        return "Talenthouse"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Talenthouse</title>
     <path d="M22.373 7.42V0H1.627v7.42h6.66V24h7.428V7.42h6.66zM12.31
 0h-.623zm-.004 3.41V.618h8.865L17.652 3.41Zm-5.948
 0L2.83.618h8.857V3.41H6.358zm-.608.308-3.503 2.76V.949ZM2.837
 6.802l3.52-2.781h4.894L8.46 6.8H2.837Zm6.068.438
 2.78-2.782v14.781l-1.602 2.046-1.183 1.51Zm.326 16.142.555-.706
 2.216-2.825 2.77 3.535zm3.078-18.924 2.786
 2.782v15.556l-2.786-3.556zM15.55 6.8l-2.8-2.78h4.904l3.519
 2.78h-5.623Zm6.206-.322L18.25 3.71 21.744.963l.02-.015Z" />
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
