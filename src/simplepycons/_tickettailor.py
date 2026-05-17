#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TicketTailorIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tickettailor"

    @property
    def original_file_name(self) -> "str":
        return "tickettailor.svg"

    @property
    def title(self) -> "str":
        return "Ticket Tailor"

    @property
    def primary_color(self) -> "str":
        return "#222432"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ticket Tailor</title>
     <path d="M21.328 19.239 15.283.631a.913.913 0 0
 0-1.15-.586l-3.374 1.096a2.146 2.146 0 1 1-4.083 1.325L3.131
 3.62a.73.73 0 0 0-.469.92l6.159 18.955a.73.73 0 0 0
 .92.469l3.545-1.152a2.148 2.148 0 1 1
 4.085-1.327l3.372-1.096a.913.913 0 0 0 .586-1.15zM10.302
 14.52H8.578V8.345H6.506V6.673h5.857v1.672h-2.061zm6.865-3.577h-2.061v6.176H13.38v-6.176h-2.073V9.271h5.86z"
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
