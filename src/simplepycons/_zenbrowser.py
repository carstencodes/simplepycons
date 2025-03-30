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


class ZenBrowserIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zenbrowser"

    @property
    def original_file_name(self) -> "str":
        return "zenbrowser.svg"

    @property
    def title(self) -> "str":
        return "Zen Browser"

    @property
    def primary_color(self) -> "str":
        return "#F76F53"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zen Browser</title>
     <path d="M24 12c0 6.627-5.373 12-12 12S0 18.627 0 12 5.373 0 12
 0s12 5.373 12 12zm-12 9.846c5.438 0 9.846-4.408 9.846-9.846S17.438
 2.154 12 2.154 2.154 6.562 2.154 12 6.562 21.846 12 21.846zM20 12a8 8
 0 1 1-16 0 8 8 0 0 1 16 0zm-8 6.462a6.462 6.462 0 1 0 0-12.924 6.462
 6.462 0 0 0 0 12.924zm0-1.847a4.615 4.615 0 1 0 0-9.23 4.615 4.615 0
 0 0 0 9.23zM15.692 12a3.692 3.692 0 1 1-7.384 0 3.692 3.692 0 0 1
 7.384 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/zen-browser/branding/blob/
4b99730c9d3c8fe3ec71d31a07e74cfd488fc27f/Official/Word%20Marks/SVG/zen'''

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
