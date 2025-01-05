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


class RiotGamesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "riotgames"

    @property
    def original_file_name(self) -> "str":
        return "riotgames.svg"

    @property
    def title(self) -> "str":
        return "Riot Games"

    @property
    def primary_color(self) -> "str":
        return "#EB0029"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Riot Games</title>
     <path d="M13.458.86 0 7.093l3.353 12.761
 2.552-.313-.701-8.024.838-.373 1.447 8.202
 4.361-.535-.775-8.857.83-.37 1.591 9.025
 4.412-.542-.849-9.708.84-.374 1.74 9.87L24 17.318V3.5Zm.316
 19.356.222 1.256L24 23.14v-4.18l-10.22 1.256Z" />
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
