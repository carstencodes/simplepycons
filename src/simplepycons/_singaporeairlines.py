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


class SingaporeAirlinesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "singaporeairlines"

    @property
    def original_file_name(self) -> "str":
        return "singaporeairlines.svg"

    @property
    def title(self) -> "str":
        return "Singapore Airlines"

    @property
    def primary_color(self) -> "str":
        return "#F99F1C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Singapore Airlines</title>
     <path d="M8.981 0 7.786 1.79c-.473.728-.062 1.51-.062 1.51l5.475
 9.055c1.263 2.17-.536 4.535-.536 4.535L9.36 22.015h2.738c1.387 0
 2.014-1.133 2.014-1.133l1.73-2.673c.628-.978 1.45-1.008
 1.45-1.008h1.572c-.977.41-1.418 1.418-1.418 1.418l-1.946 2.993c-.76
 1.133-1.643.969-1.643.969h-7.83l3.713-5.792c.875-1.318 0-2.42
 0-2.42L4.796 6.355 3.756 7.93c-.907 1.45-.032 2.294-.032 2.294l3.56
 5.722c.79 1.193.224 1.914.224 1.914l-4 6.14h10.513a2.97 2.97 0 0 0
 2.674-1.574l2.232-3.364c.535-.852 1.728-.728
 1.728-.728l-1.512-2.388h-2.17c-1.542 0-2.14 1.286-2.14 1.286l-2.045
 3.117h-.002c-.187.225-.404.505-.628.35-.217-.155.093-.566.093-.566l2.744-4.28c.404-.666
 1.133-1.986 1.133-3.148 0-1.162-.915-2.666-.915-2.666zM7.004 3.146
 5.618 5.224c-.41.69 0 1.41 0 1.41l4.69 7.77c.659 1.161.154 2.262.154
 2.262l-3.364 5.31h1.668l3.62-5.622c1.543-2.332.124-4.216.124-4.216z"
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
