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


class UnlicenseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unlicense"

    @property
    def original_file_name(self) -> "str":
        return "unlicense.svg"

    @property
    def title(self) -> "str":
        return "Unlicense"

    @property
    def primary_color(self) -> "str":
        return "#808080"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Unlicense</title>
     <path d="M24 12c0 6.627-5.373 12-12 12S0 18.627 0 12 5.373 0 12
 0s12 5.373 12 12ZM12 2.449A9.551 9.551 0 0 0 2.449 12c0 2.09.672
 4.024 1.811 5.597L17.597 4.26A9.508 9.508 0 0 0 12 2.449Zm0
 19.102A9.551 9.551 0 0 0 21.551
 12c0-2.09-.672-4.024-1.811-5.597L6.403 19.74A9.508 9.508 0 0 0 12
 21.551Zm0-2.816a6.704 6.704 0 0 1-3.34-.885l2.32-2.32a3.674 3.674 0 0
 0 4.388-2.06h3.206A6.737 6.737 0 0 1 12 18.734ZM5.265 12A6.735 6.735
 0 0 1 15.34 6.15l-2.32 2.32a3.673 3.673 0 0 0-4.55 4.55l-2.32
 2.32A6.704 6.704 0 0 1 5.265 12Zm13.28-1.592h-2.443L17.85
 8.66c.309.54.545 1.128.695 1.748Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:PD-ic'''

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
