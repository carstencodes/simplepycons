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


class VivoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vivo"

    @property
    def original_file_name(self) -> "str":
        return "vivo.svg"

    @property
    def title(self) -> "str":
        return "vivo"

    @property
    def primary_color(self) -> "str":
        return "#415FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>vivo</title>
     <path d="M19.604 14.101c-1.159 0-1.262-.95-1.262-1.24
 0-.29.103-1.242 1.262-1.242h2.062c1.16 0 1.263.951 1.263 1.242 0
 .29-.104 1.24-1.263 1.24m-2.062-3.527c-2.142 0-2.333 1.752-2.333
 2.287 0 .535.19 2.286 2.333 2.286h2.062c2.143 0 2.334-1.751
 2.334-2.286 0-.535-.19-2.287-2.334-2.287m-5.477.107c-.286
 0-.345.05-.456.213-.11.164-2.022 3.082-2.022
 3.082-.06.09-.126.126-.206.126-.08 0-.145-.036-.206-.126 0
 0-1.912-2.918-2.022-3.082-.11-.164-.17-.213-.456-.213h-.668c-.154
 0-.224.12-.127.267l2.283 3.467c.354.521.614.732 1.196.732s.842-.21
 1.196-.732l2.284-3.467c.096-.146.026-.267-.128-.267m-8.876.284c0-.203.08-.284.283-.284h.505c.203
 0 .283.08.283.283v3.9c0 .202-.08.283-.283.283h-.505c-.203
 0-.283-.08-.283-.283zm-1.769-.285c-.287
 0-.346.05-.456.213-.11.164-2.022 3.082-2.022
 3.082-.061.09-.126.126-.206.126-.08 0-.145-.036-.206-.126 0
 0-1.912-2.918-2.023-3.082-.11-.164-.169-.213-.455-.213H.175c-.171
 0-.224.12-.127.267l2.283 3.467c.355.521.615.732 1.197.732.582 0
 .842-.21
 1.196-.732l2.283-3.467c.097-.146.044-.267-.127-.267m1.055-.893c-.165-.164-.165-.295
 0-.46l.351-.351c.165-.165.296-.165.46 0l.352.351c.165.165.165.296 0
 .46l-.352.352c-.164.165-.295.165-.46 0z" />
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
