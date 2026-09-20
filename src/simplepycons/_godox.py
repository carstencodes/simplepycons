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


class GodoxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "godox"

    @property
    def original_file_name(self) -> "str":
        return "godox.svg"

    @property
    def title(self) -> "str":
        return "Godox"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Godox</title>
     <path d="M14.664 11.902V8.718l-.985.263v2.17a1.78 1.78 0 0
 0-1.341-.52 2.326 2.326 0 0 0-2.326 2.325 2.326 2.326 0 0 0 2.326
 2.326 2.33 2.33 0 0 0
 2.19-1.543c.187-.521.135-1.29.135-1.837m-13.286.105a1.34 1.34 0 0
 0-.393.949 1.34 1.34 0 0 0 1.342 1.341 1.34 1.34 0 0 0 1.342-1.341
 1.34 1.34 0 0 0-.15-.616l-.904.904-.695-.695 1.644-1.644c.62.588
 1.088 1.075 1.088 2.05a2.326 2.326 0 0 1-2.325 2.327A2.326 2.326 0 0
 1 0 12.956a2.32 2.32 0 0 1
 .713-1.675l1.613-1.613.695.695zm21.42-1.226L21.67
 12.2l-1.126-1.418-1.204.004 1.716 2.186-1.716 2.159 1.254-.004
 1.076-1.372 1.077 1.372L24 15.13l-1.716-2.159L24
 10.785zm-5.453-.151a2.326 2.326 0 0 1 2.325 2.325 2.326 2.326 0 0
 1-2.325 2.326 2.326 2.326 0 0 1-2.326-2.326 2.326 2.326 0 0 1
 2.326-2.325m0 .984a1.34 1.34 0 0 0-1.342 1.342 1.34 1.34 0 0 0 1.342
 1.342 1.34 1.34 0 0 0 1.341-1.342 1.34 1.34 0 0 0-1.341-1.342M7.333
 10.63a2.326 2.326 0 0 1 2.325 2.325 2.326 2.326 0 0 1-2.325 2.326
 2.326 2.326 0 0 1-2.326-2.326 2.326 2.326 0 0 1 2.326-2.325m0
 .984a1.34 1.34 0 0 0-1.342 1.342 1.34 1.34 0 0 0 1.342 1.342 1.34
 1.34 0 0 0 1.342-1.342 1.34 1.34 0 0 0-1.342-1.342m5.005 0a1.34 1.34
 0 0 1 1.342 1.342 1.34 1.34 0 0 1-1.342 1.342 1.34 1.34 0 0
 1-1.342-1.342 1.34 1.34 0 0 1 1.342-1.342" />
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
