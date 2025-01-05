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


class RobinhoodIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "robinhood"

    @property
    def original_file_name(self) -> "str":
        return "robinhood.svg"

    @property
    def title(self) -> "str":
        return "Robinhood"

    @property
    def primary_color(self) -> "str":
        return "#CCFF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Robinhood</title>
     <path d="M2.84 24h.53c.096 0 .192-.048.224-.128C7.591 13.696
 11.94 8.656 14.67 5.638c.112-.128.064-.225-.096-.225h-4.88a.55.55 0 0
 0-.45.225L5.746 9.972c-.514.642-.642 1.236-.642 2.086v4.43c-1.14
 3.194-1.862 5.361-2.392
 7.32-.032.125.016.192.129.192M20.447.646c-.754-.802-4.157-.834-5.73-.224a3
 3 0 0 0-.786.465 41 41 0 0 0-3.323
 3.178c-.112.113-.064.225.097.225h5.409c.497 0 .786.289.786.786v6.1c0
 .16.128.208.225.064l3.258-4.254c.53-.69.69-.898.835-1.861.192-1.413.08-3.58-.77-4.479m-6.982
 16.18 2.231-3.676a.7.7 0 0 0
 .064-.29V6.73c0-.16-.112-.225-.224-.097-3.355 3.74-5.971 7.672-8.395
 12.407-.06.12.016.225.16.177l5.009-1.54c.565-.174.882-.402
 1.155-.852" />
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
