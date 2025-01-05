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


class MaplibreIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "maplibre"

    @property
    def original_file_name(self) -> "str":
        return "maplibre.svg"

    @property
    def title(self) -> "str":
        return "MapLibre"

    @property
    def primary_color(self) -> "str":
        return "#396CB2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MapLibre</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zm0 3.19c2.937 0 5.371 2.265 5.371 5.035 0
 4.111-4.364 7.635-5.035 8.138-.084
 0-.084.084-.084.084-.084.084-.168.084-.168.084s-.168
 0-.168-.084l-.084-.084c-.84-.503-5.203-3.943-5.203-8.138 0-2.77
 2.434-5.036 5.371-5.036zm0 2.601c-1.427 0-2.602 1.173-2.602 2.684 0
 1.51 1.175 2.685 2.602 2.685 1.427 0 2.602-1.175 2.602-2.685S13.427
 5.79 12 5.79zM8.979 17.287h6.042a.66.66 0 0 1 .67.672v2.014a.66.66 0
 0 1-.67.67H8.98a.66.66 0 0 1-.67-.67v-2.014a.66.66 0 0 1
 .67-.672zm.755 1.258v.924h4.448v-.924H9.734z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/maplibre/maplibre-gl-js-do
cs/blob/e916a4cdd671890126f88b26b2b16c04220dc4b0/docs/pages/assets/fav'''

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
