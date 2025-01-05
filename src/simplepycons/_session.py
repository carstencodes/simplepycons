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


class SessionIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "session"

    @property
    def original_file_name(self) -> "str":
        return "session.svg"

    @property
    def title(self) -> "str":
        return "Session"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Session</title>
     <path d="m19.431 12.193-4.53-2.51h3.071a4.847 4.847 0 0 0
 4.842-4.841A4.848 4.848 0 0 0 17.972 0H7.252a6.073 6.073 0 0 0-6.066
 6.066 6.566 6.566 0 0 0 3.383 5.741l4.53 2.51H6.028a4.847 4.847 0 0
 0-4.842 4.841A4.848 4.848 0 0 0 6.028 24h10.72a6.073 6.073 0 0 0
 6.066-6.066 6.568 6.568 0 0 0-3.383-5.741zm-14.136-1.7a5.065 5.065 0
 0 1-2.607-4.309C2.627 3.61 4.79 1.5 7.367 1.5h10.508c1.797 0 3.345
 1.378 3.434 3.173a3.345 3.345 0 0 1-3.337 3.51H11.92a.67.67 0 0
 0-.67.67l-.001 4.94zM16.633 22.5H6.124c-1.797
 0-3.345-1.378-3.434-3.173a3.345 3.345 0 0 1 3.337-3.51h6.053c.37 0
 .67-.3.67-.67v-4.94l5.954 3.3a5.065 5.065 0 0 1 2.608 4.309c.06
 2.575-2.103 4.684-4.679 4.684" />
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
