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


class QuadNineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quad9"

    @property
    def original_file_name(self) -> "str":
        return "quad9.svg"

    @property
    def title(self) -> "str":
        return "Quad9"

    @property
    def primary_color(self) -> "str":
        return "#DC205E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Quad9</title>
     <path d="M6.822 24h5.608l6.331-9.48c1.463-2.185 2.288-4.197
 2.288-6.4C21.05 3.458 17.144 0 12 0 6.822 0 2.95 3.493 2.95 8.207c0
 4.507 3.459 8 8.345 8 .413 0 .757-.018 1.083-.07zM12 12.129c-2.426
 0-4.215-1.634-4.215-3.957 0-2.34 1.79-3.957 4.215-3.957 2.409 0 4.215
 1.617 4.215 3.957 0 2.323-1.806 3.957-4.215 3.957z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/Quad9DNS/documentation/blo'''

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
            "9.9.9.9",
            "Quad9 DNS",
        ]
