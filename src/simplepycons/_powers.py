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


class PowersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "powers"

    @property
    def original_file_name(self) -> "str":
        return "powers.svg"

    @property
    def title(self) -> "str":
        return "POWERS"

    @property
    def primary_color(self) -> "str":
        return "#E74536"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>POWERS</title>
     <path d="M12.31 12.347s-.008.73-.008 1.068c0
 .34.339.544.777.544v.486h-2.988v-.486c.408 0
 .79-.204.79-.544v-2.673c0-.545-.52-.557-.79-.595v-.466h2.55c1.042 0
 2.403-.125 2.403 1.228 0 1.403-1.233 1.441-2.304
 1.441zm-.017-2.212v1.559h.494c.35 0 .777-.063.777-.772
 0-.749-.318-.795-.907-.795-.254 0-.364.008-.364.008zM12 4.551l12
 7.45-12 7.448L0 12zm-8.645 7.45c2.764 1.713 7.373 4.575 8.645
 5.364L20.644 12A7141.71 7141.71 0 0 0 12 6.636c-1.272.787-5.881
 3.649-8.645 5.365Z" />
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
