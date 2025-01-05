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


class ByjusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "byjus"

    @property
    def original_file_name(self) -> "str":
        return "byjus.svg"

    @property
    def title(self) -> "str":
        return "Byju's"

    @property
    def primary_color(self) -> "str":
        return "#813588"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Byju's</title>
     <path d="M2.327.016A2.325 2.325 0 0 0 0 2.34v19.32a2.325 2.325 0
 0 0 2.327 2.323h19.346A2.325 2.325 0 0 0 24 21.66V2.34A2.325 2.325 0
 0 0 21.673.016zm10.054 3.496a3.443 3.443 0 0 1 .07 0 4.317 4.317 0 0
 1 3.267 1.462 4.447 4.447 0 0 1 .961 2.365 4.157 4.157 0 0 1-.456
 2.27 5.024 5.024 0 0 1 2.424 2.008 5.237 5.237 0 0 1 .73 3.374 4.68
 4.68 0 0 1-1.15 2.466 4.84 4.84 0 0 1-2.26 1.535l-4.987 1.439a1.494
 1.494 0 0 1-.41.058 1.497 1.497 0 0 1-1.432-1.075L5.524 6.909a1.487
 1.487 0 0 1 1.018-1.841l4.956-1.429a3.443 3.443 0 0 1
 .883-.127zm.248.861a3.091 3.091 0 0 0-.855.122L6.94 5.888a.744.744 0
 0 0-.51.922l3.53 12.206a.745.745 0 0 0 .921.509l4.664-1.345a4.085
 4.085 0 0 0-.896-8.003 3.297 3.297 0 0 0 1.138-2.272 3.479 3.479 0 0
 0-.928-2.549 2.989 2.989 0 0 0-2.23-.983Z" />
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
