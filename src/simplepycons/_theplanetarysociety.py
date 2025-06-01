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


class ThePlanetarySocietyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "theplanetarysociety"

    @property
    def original_file_name(self) -> "str":
        return "theplanetarysociety.svg"

    @property
    def title(self) -> "str":
        return "The Planetary Society"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The Planetary Society</title>
     <path d="M3.545 1.81A12.428 12.428 0 0 0 0 2.35a10.409 10.409 0 0
 1 1.838-.146c5.602.048 10.114 4.543 10.16 10.075-2.263 1.066-4.976
 2.147-7.986 3.158-1.258.423-2.956 1.053-3.751 1.482a2.073 2.073 0 0
 1-.04.035l.257-.065c1.338-.338 2.714-.703 4.112-1.116a106.969 106.969
 0 0 0 7.364-2.455c-.404 4.299-3.506 7.81-7.599 8.872 5.472-.627
 9.837-4.8 10.155-9.883 6.236-2.597 9.957-5.18
 9.443-6.805-.454-1.435-5.038-1.7-11.657-.554.229.226.492.512.757.826
 3.3-.31 5.532-.007 5.83.934.335 1.06-1.348 2.612-4.382
 4.296-.395-5.198-5.1-9.236-10.956-9.194z" />
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
