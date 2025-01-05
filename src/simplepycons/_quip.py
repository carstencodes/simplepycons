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


class QuipIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quip"

    @property
    def original_file_name(self) -> "str":
        return "quip.svg"

    @property
    def title(self) -> "str":
        return "Quip"

    @property
    def primary_color(self) -> "str":
        return "#F27557"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Quip</title>
     <path d="M22.154 22.154H12a10.06 10.06 0 01-7.4-3.201C2.66 16.89
 1.69 14.19 1.868 11.35c.315-5.091 4.39-9.168
 9.482-9.484.22-.014.44-.02.657-.02A10.058 10.059 0 0118.952
 4.6a10.058 10.059 0 013.202 7.4zm-1.938-18.9C17.778.963 14.59-.186
 11.236.024 5.218.399.398 5.219.024 11.237c-.207 3.353.94 6.543 3.231
 8.98A12.047 12.048 0 0012 24h11.077c.51 0
 .923-.413.923-.922V12a12.047 12.048 0 00-3.784-8.745m-4.062
 11.976H7.846a.923.923 0 000 1.846h8.308a.923.923 0 000-1.846M7.846
 8.77h8.308a.923.923 0 000-1.847H7.846a.923.923 0 000 1.847m-2.769
 2.308a.923.923 0 000 1.845h13.846a.923.923 0 000-1.846H5.077Z" />
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
