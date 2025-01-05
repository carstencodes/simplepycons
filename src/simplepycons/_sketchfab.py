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


class SketchfabIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sketchfab"

    @property
    def original_file_name(self) -> "str":
        return "sketchfab.svg"

    @property
    def title(self) -> "str":
        return "Sketchfab"

    @property
    def primary_color(self) -> "str":
        return "#1CAAD9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sketchfab</title>
     <path d="M11.3 0A11.983 11.983 0 0 0 .037 11a13.656 13.656 0 0 0
 0 2 11.983 11.983 0 0 0 11.29 11h1.346a12.045 12.045 0 0 0 11.3-11.36
 13.836 13.836 0 0 0 0-1.7A12.049 12.049 0 0 0 12.674 0zM15 6.51l2.99
 1.74s-6.064 3.24-6.084 3.24S5.812 8.27 5.8 8.26l2.994-1.77
 2.992-1.76zm-6.476 5.126L11 13v5.92l-2.527-1.4-2.46-1.43v-5.76zm9.461
 1.572v2.924L15.5 17.574 13 19.017v-6.024l2.489-1.345 2.5-1.355z" />
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
