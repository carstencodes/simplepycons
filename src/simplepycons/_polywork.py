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


class PolyworkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "polywork"

    @property
    def original_file_name(self) -> "str":
        return "polywork.svg"

    @property
    def title(self) -> "str":
        return "Polywork"

    @property
    def primary_color(self) -> "str":
        return "#543DE0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Polywork</title>
     <path d="M19.125 0H4.875A4.865 4.865 0 0 0 0 4.875v14.25C0 21.825
 2.175 24 4.875 24h6.6c2.7 0 4.875-2.175 4.875-4.875V16.65h2.775c2.7 0
 4.875-2.175 4.875-4.875v-6.9C24 2.175 21.825 0 19.125 0zM16.5
 1.275h2.625a3.6 3.6 0 0 1 3.6 3.6v2.7H16.5v-6.3zM15.075
 9v6.45H8.85V9h6.225zM8.85 1.2h6.225v6.375H8.85V1.2zM1.275 4.8a3.6 3.6
 0 0 1 3.6-3.6H7.5v6.375H1.275V4.8zM7.5 9v6.45H1.2V9h6.3zm0
 13.725H4.8a3.6 3.6 0 0 1-3.6-3.6V16.8h6.3v5.925zm7.575-3.525a3.6 3.6
 0 0 1-3.6 3.6H8.85v-5.925h6.225V19.2zm7.65-7.35a3.6 3.6 0 0 1-3.6
 3.6H16.5V9h6.225v2.85z" />
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
