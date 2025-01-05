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


class PolygonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "polygon"

    @property
    def original_file_name(self) -> "str":
        return "polygon.svg"

    @property
    def title(self) -> "str":
        return "Polygon"

    @property
    def primary_color(self) -> "str":
        return "#7B3FE4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Polygon</title>
     <path d="m17.82 16.342 5.692-3.287A.98.98 0 0 0 24
 12.21V5.635a.98.98 0 0 0-.488-.846l-5.693-3.286a.98.98 0 0 0-.977
 0L11.15 4.789a.98.98 0 0 0-.489.846v11.747L6.67
 19.686l-3.992-2.304v-4.61l3.992-2.304 2.633 1.52V8.896L7.158
 7.658a.98.98 0 0 0-.977 0L.488 10.945a.98.98 0 0
 0-.488.846v6.573a.98.98 0 0 0 .488.847l5.693 3.286a.981.981 0 0 0
 .977 0l5.692-3.286a.98.98 0 0 0 .489-.846V6.618l.072-.041 3.92-2.263
 3.99 2.305v4.609l-3.99 2.304-2.63-1.517v3.092l2.14 1.236a.981.981 0 0
 0 .978 0v-.001Z" />
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
        yield from [
            "Matic",
        ]
