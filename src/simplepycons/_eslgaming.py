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


class EslgamingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eslgaming"

    @property
    def original_file_name(self) -> "str":
        return "eslgaming.svg"

    @property
    def title(self) -> "str":
        return "ESLGaming"

    @property
    def primary_color(self) -> "str":
        return "#FFFF09"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ESLGaming</title>
     <path d="M12 0C5.373 0 0 5.373 0 12c0 6.628 5.373 12 12
 12s12-5.372 12-12c0-6.627-5.373-12-12-12zm.455 2.163a9.8 9.8 0 0 1
 5.789 2.222L4.384 18.244a9.862 9.862 0 0 1-1.06-1.582zm7.191
 3.632a9.802 9.802 0 0 1 2.192 5.806l-14.45 9.1a9.834 9.834 0 0
 1-1.592-1.055zm1.979 8.292c-.888 4.45-5.619 8.892-11.9 7.494Z" />
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
