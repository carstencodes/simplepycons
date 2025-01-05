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


class BurpSuiteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "burpsuite"

    @property
    def original_file_name(self) -> "str":
        return "burpsuite.svg"

    @property
    def title(self) -> "str":
        return "Burp Suite"

    @property
    def primary_color(self) -> "str":
        return "#FF6633"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Burp Suite</title>
     <path d="M0 0v24h24V0Zm11.063 3.357h1.874v2.756L10.41
 9.2h2.527v3.748h4.579l-4.578
 5.592v2.104h-1.876v-2.758l2.528-3.086h-2.527V11.05h-4.58l4.58-5.592Z"
 />
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
