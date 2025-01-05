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


class StarlingBankIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "starlingbank"

    @property
    def original_file_name(self) -> "str":
        return "starlingbank.svg"

    @property
    def title(self) -> "str":
        return "Starling Bank"

    @property
    def primary_color(self) -> "str":
        return "#6935D3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Starling Bank</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm2.738 3.822h.666v2.724h-.666a4.794 4.794 0 0
 0-4.789 4.788V12H7.226v-.666c0-4.142 3.37-7.512 7.512-7.512zM14.05
 12h2.723v.666c0 4.142-3.37 7.512-7.512 7.512h-.666v-2.724h.666a4.794
 4.794 0 0 0 4.789-4.788z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.starlingbank.com/docs/brand/starl'''
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
