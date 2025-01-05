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


class ExpensifyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "expensify"

    @property
    def original_file_name(self) -> "str":
        return "expensify.svg"

    @property
    def title(self) -> "str":
        return "Expensify"

    @property
    def primary_color(self) -> "str":
        return "#0185FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Expensify</title>
     <path d="M8.16
 17.52h7.68v-2.28h-4.872v-2.136h4.152v-2.328h-4.152v-2.04h4.872V6.48H8.16v11.04z
 M21.6 12a9.608 9.608 0 01-2.16 6.072l1.704 1.704A11.958 11.958 0 0024
 12c0-2.928-1.056-5.616-2.784-7.68l-1.704 1.704A9.61 9.61 0 0121.6 12z
 M18.072 19.44a9.608 9.608 0 01-12.048.072L4.32 21.216A11.913 11.913 0
 0012 24c2.976 0 5.688-1.08 7.776-2.856l-1.704-1.704z M4.632
 18.168A9.613 9.613 0 012.4 12c0-5.304 4.296-9.6 9.6-9.6 2.352 0
 4.488.84 6.168 2.232l1.704-1.704A12.02 12.02 0 0012 0C5.376 0 0 5.376
 0 12c0 3 1.104 5.76 2.928 7.872l1.704-1.704z" />
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
