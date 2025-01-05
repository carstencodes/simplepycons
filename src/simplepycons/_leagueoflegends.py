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


class LeagueOfLegendsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "leagueoflegends"

    @property
    def original_file_name(self) -> "str":
        return "leagueoflegends.svg"

    @property
    def title(self) -> "str":
        return "League of Legends"

    @property
    def primary_color(self) -> "str":
        return "#C28F2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>League of Legends</title>
     <path d="m1.912 0 1.212 2.474v19.053L1.912
 24h14.73l1.337-4.682H8.33V0ZM12 1.516c-.913
 0-1.798.112-2.648.312v1.74a9.738 9.738 0 0 1 2.648-.368c5.267 0 9.536
 4.184 9.536 9.348a9.203 9.203 0 0 1-2.3 6.086l-.273.954-.602
 2.112c2.952-1.993 4.89-5.335 4.89-9.122C23.25 6.468 18.213 1.516 12
 1.516Zm0 2.673c-.924 0-1.814.148-2.648.414v13.713h8.817a8.246 8.246 0
 0 0 2.36-5.768c0-4.617-3.818-8.359-8.529-8.359zM2.104 7.312A10.858
 10.858 0 0 0 .75 12.576c0 1.906.492 3.7 1.355 5.266z" />
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
