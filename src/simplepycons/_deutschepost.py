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


class DeutschePostIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "deutschepost"

    @property
    def original_file_name(self) -> "str":
        return "deutschepost.svg"

    @property
    def title(self) -> "str":
        return "Deutsche Post"

    @property
    def primary_color(self) -> "str":
        return "#FFCC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Deutsche Post</title>
     <path d="M11.057 18.221 7.839 21.47H4.652l3.219-3.249zm-4.299
 0L3.541 21.47H.354l3.219-3.249zm8.227 0 3.219
 3.249h-3.187l-3.22-3.249zm4.3 0 3.217
 3.249h-3.187l-3.218-3.249zM10.465 2.53c3.765-.003 6.88 2.74 6.865
 6.676.553-1.502.937-3.789 1.016-5.39L24 5.22c-.452 6.621-5.43
 12.42-12.815 12.416C2.832 17.635-.397 10.389.039
 4.899l2.453-.779c-.399 3.125.57 5.378 1.238 6.41-.795-4.42
 2.549-7.998 6.735-8m.011 2.301a4.519 4.519 0 0 0-4.524 4.514 4.519
 4.519 0 0 0 4.524 4.514 4.518 4.518 0 0 0 4.525-4.514 4.518 4.518 0 0
 0-4.525-4.514" />
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
