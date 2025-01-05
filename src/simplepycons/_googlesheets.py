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


class GoogleSheetsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlesheets"

    @property
    def original_file_name(self) -> "str":
        return "googlesheets.svg"

    @property
    def title(self) -> "str":
        return "Google Sheets"

    @property
    def primary_color(self) -> "str":
        return "#34A853"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Sheets</title>
     <path d="M11.318 12.545H7.91v-1.909h3.41v1.91zM14.728
 0v6h6l-6-6zm1.363 10.636h-3.41v1.91h3.41v-1.91zm0
 3.273h-3.41v1.91h3.41v-1.91zM20.727 6.5v15.864c0 .904-.732
 1.636-1.636 1.636H4.909a1.636 1.636 0 0 1-1.636-1.636V1.636C3.273.732
 4.005 0 4.909 0h9.318v6.5h6.5zm-3.273
 2.773H6.545v7.909h10.91v-7.91zm-6.136 4.636H7.91v1.91h3.41v-1.91z" />
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
