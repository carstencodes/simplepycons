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


class LinkfireIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "linkfire"

    @property
    def original_file_name(self) -> "str":
        return "linkfire.svg"

    @property
    def title(self) -> "str":
        return "Linkfire"

    @property
    def primary_color(self) -> "str":
        return "#FF3850"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Linkfire</title>
     <path d="M10.08 1.997A10.041 10.042 0 0 0 0 12.006a10.041 10.042
 0 0 0 10.08 10 10.037 10.038 0 0 0 7.12-2.933c2.883-2.796 4.509-8.065
 5.775-12.861l.038-.152.09-.343a.227.227 0 0 0-.038-.197.234.234 0 0
 0-.185-.09h-1.711a.23.23 0 0 1-.215-.14.227.227 0 0 1
 .053-.25l2.925-2.646v-.011a.23.23 0 0 0 .053-.246.23.23 0 0
 0-.216-.143zm.385 4.645h3.847a1.686 1.686 0 0 1 1.682
 1.686v3.844a1.686 1.686 0 0 1-1.682 1.686H10.47a1.686 1.686 0 0
 1-1.684-1.686v-.722h1.442v.722a.246.246 0 0 0 .242.242h3.848a.242.242
 0 0 0 .242-.242V8.324a.242.242 0 0 0-.242-.242H10.47a.242.242 0 0
 0-.242.242v.722H8.784v-.718a1.686 1.686 0 0 1 1.684-1.686zM7.582
 9.526h3.84a1.686 1.686 0 0 1 1.684 1.686v.718h-1.44v-.718a.242.242 0
 0 0-.24-.242H7.577a.242.242 0 0 0-.242.242v3.847a.242.242 0 0 0
 .242.242h3.847a.242.242 0 0 0 .241-.242v-.718h1.448v.718a1.686 1.686
 0 0 1-1.686 1.682H7.582a1.686 1.686 0 0 1-1.69-1.682v-3.847a1.686
 1.686 0 0 1 1.69-1.686z" />
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
