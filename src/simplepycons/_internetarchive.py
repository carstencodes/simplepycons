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


class InternetArchiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "internetarchive"

    @property
    def original_file_name(self) -> "str":
        return "internetarchive.svg"

    @property
    def title(self) -> "str":
        return "Internet Archive"

    @property
    def primary_color(self) -> "str":
        return "#666666"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Internet Archive</title>
     <path d="M22.667
 22.884V24H1.333v-1.116zm-.842-1.675v1.396H2.175v-1.396zM4.233
 6.14l.234.118.118 1.882.117 3.058v2.941l-.117 3.666-.02
 2.47-.332.098H3.062l-.352-.098-.136-2.47-.118-3.646v-2.941l.118-3.078.107-1.892.244-.107zm16.842
 0l.235.118.117 1.882.117 3.058v2.941l-.117 3.666-.02
 2.47-.332.098h-1.171l-.352-.098-.137-2.47-.117-3.646v-2.941l.117-3.078.108-1.892.244-.107zm-11.79
 0l.235.118.117 1.882.117 3.058v2.941l-.117 3.666-.02
 2.47-.331.098H8.114l-.352-.098-.136-2.47-.117-3.646v-2.941l.117-3.078.107-1.892.244-.107zm6.457
 0l.234.118.117 1.882.118 3.058v2.941l-.118 3.666-.019
 2.47-.332.098H14.57l-.351-.098-.137-2.47-.117-3.646v-2.941l.117-3.078.108-1.892.244-.107zm6.083-2.511V5.58H2.175V3.628zM11.798
 0l10.307 2.347-.413.723H1.951l-.618-.587Z" />
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
