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


class CrayonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "crayon"

    @property
    def original_file_name(self) -> "str":
        return "crayon.svg"

    @property
    def title(self) -> "str":
        return "Crayon"

    @property
    def primary_color(self) -> "str":
        return "#FF6A4C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Crayon</title>
     <path d="M1.9485 16.5624C3.1842 17.7981 4.8 18.4159 6.416
 18.4159c1.6158 0 3.2317-.6179
 4.4673-1.8535l5.798-5.798-1.4257-1.4258-5.798 5.7505c-1.6634
 1.6634-4.3723 1.6634-6.0832 0l-.095-.095c-1.6635-1.6634-1.6635-4.3723
 0-6.0832l.095-.095c1.6633-1.6635 4.3723-1.6635 6.0832 0l.4752.5227
 1.4258-1.4258-.4753-.5227c-2.4713-2.4713-6.5109-2.4713-8.9822
 0l-.0475.1425c-2.4713 2.4713-2.4713 6.511 0
 8.9823zm20.0556-9.1248c-1.2357-1.2357-2.8515-1.8535-4.4674-1.8535-1.6158
 0-3.2317.6179-4.4673 1.8535l-5.798 5.798 1.4257 1.4258
 5.798-5.7505c1.6634-1.6634 4.3723-1.6634 6.0832 0l.095.095c1.6634
 1.6634 1.6634 4.3723 0 6.0832l-.095.095c-1.6633 1.6635-4.3723
 1.6635-6.0832 0l-.4752-.4752-1.4258 1.4258.4753.4752c2.4713 2.4713
 6.5109 2.4713 8.9822 0l.095-.095c2.4713-2.4713 2.4713-6.511
 0-8.9823-.0475 0-.1425-.095-.1425-.095z" />
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
