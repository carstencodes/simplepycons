#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class FiveHundredPxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "500px"

    @property
    def original_file_name(self) -> "str":
        return "500px.svg"

    @property
    def title(self) -> "str":
        return "500px"

    @property
    def primary_color(self) -> "str":
        return "#222222"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>500px</title>
     <path d="M7.451 8.9995A3.0005 3.0005 0 1 0 10.4514 12a3.0275
 3.0275 0 0 0-3.0006-3.0005Zm0 5.371A2.3554 2.3554 0 1 1 9.7912
 12a2.3704 2.3704 0 0 1-2.3404 2.3704Zm6.448-5.371A3.0005 3.0005 0 1 0
 16.8997 12a3.0005 3.0005 0 0 0-3.0005-3.0005Zm0 5.371A2.3554 2.3554 0
 1 1 16.2396 12a2.3314 2.3314 0 0 1-2.3404 2.3704zM2.29 10.7997a2.0224
 2.0224 0 0 0-1.5903.42V9.6297h2.7005c.09 0 .15-.03.15-.3
 0-.2701-.12-.2701-.18-.2701H.3997a.27.27 0 0 0-.27.27V11.97c0
 .15.09.18.24.21a.228.228 0 0 0 .27-.06A1.7073 1.7073 0 0 1 2.14 11.4
 1.5603 1.5603 0 0 1 3.4902 12.72 1.5183 1.5183 0 0 1 2.17
 14.4004h-.18a1.5303 1.5303 0 0
 1-1.4103-.9901c-.03-.09-.09-.15-.33-.06-.2401.09-.2701.15-.2401.24a2.1274
 2.1274 0 0 0 2.7005 1.2602A2.1274 2.1274 0 0 0 3.9703 12.15 2.1004
 2.1004 0 0 0 2.29 10.7998zm16.65-1.7703a1.6263 1.6263 0 0 0-1.4403
 1.6203v2.6704c0 .15.12.18.3.18s.3001-.03.3001-.18v-2.6704a1.0082
 1.0082 0 0 1 .8702-1.0202.9872.9872 0 0 1 .7501.24.9572.9572 0 0 1
 .33.7202 1.2002 1.2002 0 0 1-.21.57A.9452.9452 0 0 1 19 11.55c-.12
 0-.21 0-.24.27 0 .1801 0 .2701.15.3001a1.4763 1.4763 0 0 0 .8701-.18
 1.6113 1.6113 0 0 0 .8702-1.2602 1.5543 1.5543 0 0
 0-1.4463-1.6803.8311.8311 0 0 1-.264.03zm3.9307 1.5602
 1.0802-1.0801c.03-.03.12-.12-.06-.3301a.3.3 0 0 0-.2101-.12.156.156 0
 0 0-.12.06l-1.0802
 1.0802-1.0802-1.1102c-.09-.09-.18-.06-.33.06-.15.12-.15.24-.06.33l1.0801
 1.0802-1.0862 1.1102a.228.228 0 0 0-.06.12.252.252 0 0 0
 .12.2101.483.483 0 0 0 .21.12.318.318 0 0 0 .1501-.06l1.0802-1.0802
 1.0802 1.0802a.156.156 0 0 0 .12.06.3.3 0 0 0
 .21-.12c.09-.12.12-.24.03-.3z" />
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