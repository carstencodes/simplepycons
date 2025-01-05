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


class GsmarenadotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gsmarenadotcom"

    @property
    def original_file_name(self) -> "str":
        return "gsmarenadotcom.svg"

    @property
    def title(self) -> "str":
        return "GSMArena.com"

    @property
    def primary_color(self) -> "str":
        return "#D50000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GSMArena.com</title>
     <path d="M20.324 22.992c-.905-.454-12.625-5.27-12.625-5.27a1.275
 1.275 0 0 0-.389-.122c-.39-.056-.78.091-1.061.444 0 0-2.672
 4.354-3.066 4.948C2.782 23.58 3.2 24 3.726 24h16.38c.644 0
 .898-.67.218-1.008ZM19.688 0h-7.743c-.868 0-1.49.28-2.042 1.043L4.05
 10.497c-.333.457-.14.985.336 1.185.974.412 2.766.977 3.68
 1.388.718.326 1.157.204 1.552-.382l4.092-6.507.49-.005v7.405c0
 .924.37 1.279.946 1.54.577.246 4.144 1.773 4.689 1.973.644.246
 1.143-.05 1.143-.731V1.289c0-.706-.585-1.289-1.29-1.289Z" />
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
