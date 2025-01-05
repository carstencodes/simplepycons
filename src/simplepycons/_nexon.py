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


class NexonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nexon"

    @property
    def original_file_name(self) -> "str":
        return "nexon.svg"

    @property
    def title(self) -> "str":
        return "Nexon"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nexon</title>
     <path d="M5.138
 10.158v3.693h3.775v-.783H6.126v-.706h2.787v-.789H6.126v-.632h2.787v-.783zm15.778
 3.693v-2.234l2.34
 2.234H24v-3.693h-.987v2.234l-2.34-2.234h-.745v3.693zm-2.051-3.701h-4.072v3.7h4.072zm-.988
 2.918H15.78v-2.127h2.097zm-16.89.783v-2.234l2.34
 2.234h.748v-3.693h-.99v2.234l-2.34-2.234H0v3.693zm10.241-1.844-1.633
 1.844h1.249l1.009-1.14 1.012 1.14h1.249l-1.637-1.844
 1.64-1.849h-1.25l-1.014 1.145-1.012-1.145H9.589z" />
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
