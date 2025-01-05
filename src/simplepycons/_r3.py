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


class RThreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "r3"

    @property
    def original_file_name(self) -> "str":
        return "r3.svg"

    @property
    def title(self) -> "str":
        return "R3"

    @property
    def primary_color(self) -> "str":
        return "#EC1D24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>R3</title>
     <path d="M24 13.457c0 .841-.688 1.53-1.53 1.53-.842
 0-1.53-.689-1.53-1.53a1.53 1.53 0 1 1 3.06 0zM6.147 2.853c-1.123
 0-2.172.3-3.08.828v-.828H0v12.134h3.067V9a3.077 3.077 0 0 1
 3.08-3.08l1.029-.007 2.105-3.06H6.147zm8.746 6.08
 2.078-3.02v-3.06h-6.615l-2.104 3.06h4.99l-2.565 3.735 1.53
 2.653a3.098 3.098 0 0 1 4.65 2.686c0 1.717-1.39 3.1-3.1 3.1-1.71
 0-3.1-1.39-3.1-3.1h-3.06c0 3.4 2.76 6.16 6.154 6.16 3.4 0 6.16-2.76
 6.16-6.16a6.162 6.162 0 0 0-5.018-6.054z" />
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
