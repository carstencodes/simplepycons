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


class HubspotIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hubspot"

    @property
    def original_file_name(self) -> "str":
        return "hubspot.svg"

    @property
    def title(self) -> "str":
        return "HubSpot"

    @property
    def primary_color(self) -> "str":
        return "#FF7A59"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HubSpot</title>
     <path d="M18.164 7.93V5.084a2.198 2.198 0 001.267-1.978v-.067A2.2
 2.2 0 0017.238.845h-.067a2.2 2.2 0 00-2.193 2.193v.067a2.196 2.196 0
 001.252 1.973l.013.006v2.852a6.22 6.22 0 00-2.969
 1.31l.012-.01-7.828-6.095A2.497 2.497 0 104.3 4.656l-.012.006 7.697
 5.991a6.176 6.176 0 00-1.038 3.446c0 1.343.425 2.588 1.147
 3.607l-.013-.02-2.342 2.343a1.968 1.968 0 00-.58-.095h-.002a2.033
 2.033 0 102.033 2.033 1.978 1.978 0 00-.1-.595l.005.014
 2.317-2.317a6.247 6.247 0 104.782-11.134l-.036-.005zm-.964
 9.378a3.206 3.206 0 113.215-3.207v.002a3.206 3.206 0 01-3.207 3.207z"
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
