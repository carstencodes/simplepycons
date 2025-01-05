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


class WellfoundIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wellfound"

    @property
    def original_file_name(self) -> "str":
        return "wellfound.svg"

    @property
    def title(self) -> "str":
        return "Wellfound"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wellfound</title>
     <path d="M23.998
 8.128c.063-1.379-1.612-2.376-2.795-1.664-1.23.598-1.322 2.52-.156
 3.234 1.2.862 2.995-.09 2.951-1.57zm0
 7.748c.063-1.38-1.612-2.377-2.795-1.665-1.23.598-1.322 2.52-.156
 3.234 1.2.863 2.995-.09 2.951-1.57zm-20.5 1.762L0 6.364h3.257l2.066
 8.106 2.245-8.106h3.267l2.244 8.106 2.065-8.106h3.257l-3.54
 11.274H11.39c-.73-2.713-1.46-5.426-2.188-8.14l-2.233 8.14H3.5z" />
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
