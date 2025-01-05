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


class WebtreesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webtrees"

    @property
    def original_file_name(self) -> "str":
        return "webtrees.svg"

    @property
    def title(self) -> "str":
        return "webtrees"

    @property
    def primary_color(self) -> "str":
        return "#2694E8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>webtrees</title>
     <path d="M2.957 4.34q.647 0 1.269.243.634.243 1.093.7.459.448.662
 1l1.592 4.59 1.31-3.82Q9.84 4.26 11.92 4.26q.459 0 1.106.203.729.23
 1.228.809.5.58.905 1.782l1.296 3.82
 1.606-4.59q.189-.54.649-.998.472-.459 1.079-.703.608-.243
 1.283-.243.62.04 1.241.338.783.378 1.228 1.106.459.73.459 1.66 0
 .81-.364 1.54l-4.225 8.652q-1.025 2.106-3.037
 2.106-.905-.04-1.634-.567-.728-.54-1.133-1.498L12 13.72l-1.606
 3.955q-.243.634-.647 1.093-.406.447-.945.702-.54.257-1.134.27-1.013
 0-1.755-.486-.742-.5-1.297-1.62L.392 8.983Q0 8.16 0
 7.443q0-.89.46-1.632.459-.756 1.254-1.134.622-.297 1.243-.337Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://wtwi.jprodina.cz/index.php?title=Logo'''
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
