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


class GridsomeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gridsome"

    @property
    def original_file_name(self) -> "str":
        return "gridsome.svg"

    @property
    def title(self) -> "str":
        return "Gridsome"

    @property
    def primary_color(self) -> "str":
        return "#00A672"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gridsome</title>
     <path d="M12.026.017l-.108.001C4.905.135-.102 5.975.002
 11.956.025 19.286 6.02 24.13 12.083 23.98c7.208-.2 12.323-6.461
 11.892-12.05a2.197 2.197 0 0 0-2.192-2.001h-3.15a2.155 2.155 0 0
 0-2.161 2.147c0 1.187.967 2.148 2.16 2.148h.788c-.87 2.791-3.62
 5.455-7.44 5.56-3.803.095-7.61-2.904-7.768-7.569a2.173 2.173 0 0 0
 0-.159c-.148-3.72 2.895-7.637 7.88-7.845a2.096 2.096 0 0 0
 2.003-2.183 2.095 2.095 0 0 0-2.07-2.011zm-.018 9.911a2.15 2.15 0 0
 0-2.146 2.151 2.15 2.15 0 0 0 2.146 2.152 2.15 2.15 0 0 0 2.147-2.152
 2.15 2.15 0 0 0-2.147-2.15Z" />
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
