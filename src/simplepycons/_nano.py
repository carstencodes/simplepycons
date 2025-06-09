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


class NanoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nano"

    @property
    def original_file_name(self) -> "str":
        return "nano.svg"

    @property
    def title(self) -> "str":
        return "Nano"

    @property
    def primary_color(self) -> "str":
        return "#209CE9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nano</title>
     <path d="m3.723 0 6.875 10.76H4.775v1.365h5.881l-1.76
 2.73h-4.12v1.364h3.242L3.006 24h1.85l5.068-7.781h4.215L19.129
 24h1.865l-4.941-7.781h3.232v-1.364h-4.1l-1.732-2.73h5.832V10.76h-5.803L20.45
 0h-1.785l-6.588 10.107L5.627 0H3.723zm8.324 12.959 1.217
 1.896h-2.451l1.234-1.896z" />
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
