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


class HboIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hbo"

    @property
    def original_file_name(self) -> "str":
        return "hbo.svg"

    @property
    def title(self) -> "str":
        return "HBO"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HBO</title>
     <path d="M7.042 16.896H4.414v-3.754H2.708v3.754H.01L0
 7.22h2.708v3.6h1.706v-3.6h2.628zm12.043.046C21.795 16.94 24 14.689 24
 11.978a4.89 4.89 0 0 0-4.915-4.92c-2.707-.002-4.09 1.991-4.432
 2.795.003-1.207-1.187-2.632-2.58-2.634H7.59v9.674l4.181.001c1.686 0
 2.886-1.46 2.888-2.713.385.788 1.72 2.762 4.427
 2.76zm-7.665-3.936c.387 0 .692.382.692.817 0
 .435-.305.817-.692.817h-1.33v-1.634zm.005-3.633c.387 0
 .692.382.692.817 0 .436-.305.818-.692.818h-1.33V9.373zm1.77
 2.607c.305-.039.813-.387.992-.61-.063.276-.068 1.074.006
 1.35-.204-.314-.688-.701-.998-.74zm3.43 0a2.462 2.462 0 1 1 4.924 0
 2.462 2.462 0 0 1-4.925 0zm2.462 1.936a1.936 1.936 0 1 0 0-3.872
 1.936 1.936 0 0 0 0 3.872Z" />
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
