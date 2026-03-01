#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class YewIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yew"

    @property
    def original_file_name(self) -> "str":
        return "yew.svg"

    @property
    def title(self) -> "str":
        return "Yew"

    @property
    def primary_color(self) -> "str":
        return "#009A5B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yew</title>
     <path d="M21.47.002a1.18 1.18 0 0 0-.815.392L13.33
 8.566h-.002a3.5 3.5 0 0 0-1.423-.303 3.5 3.5 0 0
 0-1.287.246h-.002L3.345.394a1.18 1.18 0 0 0-.815-.39 1.18 1.18 0 0
 0-.853.298 1.18 1.18 0 0 0-.092 1.667l7.246 8.083a3.5 3.5 0 0 0-.466
 1.75 3.56 3.56 0 0 0 2.453 3.37v7.647A1.18 1.18 0 0 0 12 24a1.18 1.18
 0 0 0 1.18-1.18v-7.715a3.56 3.56 0 0 0 2.267-3.302 3.5 3.5 0 0
 0-.396-1.62l7.364-8.213a1.18 1.18 0 0 0-.092-1.668 1.18 1.18 0 0
 0-.854-.3m-9.563 1.573a9.84 9.84 0 0 0-5.39 1.61l.671.748a8.8 8.8 0 0
 1 4.72-1.357c1.787 0 3.448.527 4.836 1.435l.67-.748a9.84 9.84 0 0
 0-5.507-1.688M4.06 5.482a9.84 9.84 0 0 0-1.99 5.93 9.835 9.835 0 0 0
 8.248 9.705v-1.013a8.82 8.82 0 0 1-7.247-8.693 8.8 8.8 0 0 1
 1.666-5.175Zm15.777.113-.68.757a8.8 8.8 0 0 1 1.584 5.058 8.82 8.82 0
 0 1-7.062 8.657v1.016a9.835 9.835 0 0 0 8.062-9.673 9.84 9.84 0 0
 0-1.904-5.815m-7.93 4.241a1.955 1.955 0 0 1 1.965 1.967 1.955 1.955 0
 0 1-1.966 1.967 1.955 1.955 0 0 1-1.967-1.969 1.955 1.955 0 0 1
 1.967-1.966" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/yewstack/yew/blob/38e2478d'''

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
