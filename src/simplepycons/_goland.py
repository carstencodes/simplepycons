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


class GolandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "goland"

    @property
    def original_file_name(self) -> "str":
        return "goland.svg"

    @property
    def title(self) -> "str":
        return "GoLand"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GoLand</title>
     <path d="M0 0v24h24V0Zm6.764 3a5.448 5.448 0 0 1 3.892
 1.356L9.284 6.012A3.652 3.652 0 0 0 6.696 5c-1.6 0-2.844 1.4-2.844
 3.08v.028c0 1.812 1.244 3.14 3 3.14a3.468 3.468 0 0 0
 2.048-.596V9.228H6.708v-1.88H11v4.296a6.428 6.428 0 0 1-4.228
 1.572c-3.076 0-5.196-2.164-5.196-5.092v-.028A5.08 5.08 0 0 1 6.764
 3Zm10.432 0c3.052 0 5.244 2.276 5.244 5.088v.028a5.116 5.116 0 0
 1-5.272 5.12c-3.056-.02-5.248-2.296-5.248-5.112v-.028A5.116 5.116 0 0
 1 17.196 3Zm-.028 2A2.96 2.96 0 0 0 14.2 8.068v.028a3.008 3.008 0 0 0
 3 3.112 2.96 2.96 0 0 0 2.964-3.084v-.028A3.004 3.004 0 0 0 17.168
 5ZM2.252 19.5h9V21h-9z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.jetbrains.com/company/brand/#bran'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.jetbrains.com/company/brand/#logo'''

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
