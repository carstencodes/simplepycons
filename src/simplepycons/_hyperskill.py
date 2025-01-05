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


class HyperskillIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hyperskill"

    @property
    def original_file_name(self) -> "str":
        return "hyperskill.svg"

    @property
    def title(self) -> "str":
        return "Hyperskill"

    @property
    def primary_color(self) -> "str":
        return "#8C5AFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hyperskill</title>
     <path d="M22 22.6a1.4 1.4 0 0 1-1.4 1.4h-1.2a1.4 1.4 0 0
 1-1.4-1.4V1.4A1.4 1.4 0 0 1 19.4 0h1.2A1.4 1.4 0 0 1 22
 1.4zm-8-14a1.4 1.4 0 0 1-1.4 1.4h-1.2A1.4 1.4 0 0 1 10 8.6V3.4A1.4
 1.4 0 0 1 11.4 2h1.2A1.4 1.4 0 0 1 14 3.4zm-8.001 8a1.4 1.4 0 0 1-1.4
 1.4H3.4A1.4 1.4 0 0 1 2 16.6V7.4A1.4 1.4 0 0 1 3.4 6h1.2A1.4 1.4 0 0
 1 6 7.4v9.2zm8.001 4a1.4 1.4 0 0 1-1.4 1.4h-1.2a1.4 1.4 0 0
 1-1.4-1.4v-5.2a1.4 1.4 0 0 1 1.4-1.4h1.2a1.4 1.4 0 0 1 1.4 1.4z" />
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
