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


class OutlineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "outline"

    @property
    def original_file_name(self) -> "str":
        return "outline.svg"

    @property
    def title(self) -> "str":
        return "Outline"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Outline</title>
     <path d="M 15.081 21.857 L 15.081 22.459 C 15.081 23.636 13.812
 24.378 12.785 23.8 L 3.543 18.602 C 3.058 18.329 2.758 17.816 2.758
 17.26 L 2.758 6.742 C 2.758 6.185 3.058 5.672 3.543 5.399 L 12.785
 0.201 C 13.812 -0.378 15.082 0.365 15.081 1.544 L 15.081 2.145 L
 16.178 1.814 C 17.167 1.517 18.163 2.258 18.162 3.29 L 18.162 3.915 L
 19.511 3.746 C 20.431 3.632 21.243 4.348 21.242 5.275 L 21.242 18.726
 C 21.243 19.652 20.431 20.37 19.511 20.254 L 18.162 20.085 L 18.162
 20.71 C 18.163 21.743 17.167 22.484 16.178 22.186 L 15.081 21.857 Z M
 15.081 20.249 L 16.621 20.71 L 16.621 3.29 L 15.081 3.753 L 15.081
 20.249 Z M 18.162 5.467 L 18.162 18.534 L 19.702 18.726 L 19.702
 5.275 L 18.162 5.467 Z M 2.758 16.801 L 2.758 7.2 L 2.758 16.801 Z M
 4.298 6.742 L 4.298 17.26 L 13.54 22.459 L 13.54 1.544 L 4.298 6.742
 Z M 5.838 7.765 L 7.379 6.995 L 7.379 17.005 L 5.838 16.235 L 5.838
 7.765 Z" />
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
