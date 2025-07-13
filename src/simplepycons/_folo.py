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


class FoloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "folo"

    @property
    def original_file_name(self) -> "str":
        return "folo.svg"

    @property
    def title(self) -> "str":
        return "Folo"

    @property
    def primary_color(self) -> "str":
        return "#FF5C00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Folo</title>
     <path d="M5.382 0h13.236A5.37 5.37 0 0 1 24 5.383v13.235A5.37
 5.37 0 0 1 18.618 24H5.382A5.37 5.37 0 0 1 0 18.618V5.383A5.37 5.37 0
 0 1 5.382.001Zm7.887 17.31a1.813 1.813 0 1 0-3.626.002 1.813 1.813 0
 0 0 3.626-.002m-.535-6.527H7.213a1.813 1.813 0 1 0 0
 3.624h5.521a1.813 1.813 0 1 0 0-3.624m4.417-4.712H8.87a1.813 1.813 0
 1 0 0 3.625h8.283a1.813 1.813 0 1 0 0-3.624z" />
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
