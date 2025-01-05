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


class ScrimbaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scrimba"

    @property
    def original_file_name(self) -> "str":
        return "scrimba.svg"

    @property
    def title(self) -> "str":
        return "Scrimba"

    @property
    def primary_color(self) -> "str":
        return "#2B283A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scrimba</title>
     <path d="M24 6.222a2.222 2.222 0 01-2.222 2.222h-8.89a2.222 2.222
 0 010-4.444h8.89C23.005 4 24 4.995 24 6.222zm-7.333 9.334h-8.89a2.222
 2.222 0 000 4.444h8.89a2.222 2.222 0 000-4.444zm0-5.778H13.11a2.222
 2.222 0 000 4.444h3.556a2.222 2.222 0 000-4.444zM2.222 15.556a2.222
 2.222 0 100 4.444 2.222 2.222 0 000-4.444z" />
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
