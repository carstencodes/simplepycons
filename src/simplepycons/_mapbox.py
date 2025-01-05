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


class MapboxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mapbox"

    @property
    def original_file_name(self) -> "str":
        return "mapbox.svg"

    @property
    def title(self) -> "str":
        return "Mapbox"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Mapbox</title>
     <path d="M12 0C5.372 0 0 5.372 0 12s5.372 12 12 12 12-5.372
 12-12S18.628 0 12 0zm5.696 14.943c-4.103 4.103-11.433 2.794-11.433
 2.794S4.94 10.421 9.057 6.304c2.281-2.281 6.061-2.187 8.45.189s2.471
 6.168.189 8.45zm-4.319-7.91l-1.174 2.416-2.416 1.174 2.416 1.174
 1.174 2.416 1.174-2.416 2.416-1.174-2.416-1.174-1.174-2.416z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.mapbox.com/about/press/brand-guid'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.mapbox.com/about/press/brand-guid'''

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
