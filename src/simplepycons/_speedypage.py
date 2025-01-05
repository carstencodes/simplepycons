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


class SpeedypageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "speedypage"

    @property
    def original_file_name(self) -> "str":
        return "speedypage.svg"

    @property
    def title(self) -> "str":
        return "SpeedyPage"

    @property
    def primary_color(self) -> "str":
        return "#1C71F9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SpeedyPage</title>
     <path d="M20.356 11.774a8.66 8.66 0 0 1-7.797 8.623C12.559 20.503
 0 22.18 0 22.18l1.383-4.978 10.192-1.544v-.025a3.617 3.617 0 0 0
 3.405-3.807 3.44 3.44 0 0
 0-.212-1.01h5.534c.054.318.054.638.054.958zm-16.686.452c0-4.444
 3.381-8.171 7.797-8.623C11.467 3.471 24 1.82 24 1.82l-1.41
 4.978-10.19 1.57v.025a3.556 3.556 0 0 0-3.353
 3.781c.026.346.08.664.214.984H3.724c-.026-.32-.054-.612-.054-.932z"
 />
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
