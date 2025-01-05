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


class ThingiverseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thingiverse"

    @property
    def original_file_name(self) -> "str":
        return "thingiverse.svg"

    @property
    def title(self) -> "str":
        return "Thingiverse"

    @property
    def primary_color(self) -> "str":
        return "#248BFB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Thingiverse</title>
     <path d="M11.955.005C5.425-.152-.091 5.485.007 11.805c-.235 6.756
 5.537 12.25 12.052 12.196C18.621 23.9 23.912 18.595 24 12.03 24.031
 5.483 18.505-.18 11.955.005zm-.047 1.701a10.276 10.276 0 0 1 7.36
 17.529 10.275 10.275 0 0 1-17.556-7.287C1.71 6.308 6.268 1.728 11.907
 1.706zm-5.55 4.781c-.322 0-.358.033-.358.361v2.248c0
 .351.04.391.398.391h3.823c.274 0 .274.004.274.265v9.736a.176.176 0 0
 0
 .051.146c.04.038.093.059.148.053h2.555c.247-.003.283-.035.283-.28v-9.32c0-.124.004-.239
 0-.39s.055-.21.218-.21h3.9c.319.004.35-.032.35-.344V6.855c0-.34-.024-.363-.37-.363h-5.626z"
 />
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
