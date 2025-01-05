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


class CinnamonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cinnamon"

    @property
    def original_file_name(self) -> "str":
        return "cinnamon.svg"

    @property
    def title(self) -> "str":
        return "Cinnamon"

    @property
    def primary_color(self) -> "str":
        return "#DC682E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cinnamon</title>
     <path d="M12 0C5.373 0 0 5.373 0 12c0 6.628 5.373 12 12 12 6.628
 0 12-5.372 12-12 0-6.627-5.372-12-12-12zm0 2.045c5.498 0 9.955 4.457
 9.955 9.955 0 .844-.116 1.66-.314 2.443l-4.735-5.26-6.054 6.887
 2.921-5.844-1.46-2.609-8.604 9.889A9.908 9.908 0 0 1 2.045 12c0-5.498
 4.457-9.955 9.955-9.955z" />
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
