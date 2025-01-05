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


class HomeAssistantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "homeassistant"

    @property
    def original_file_name(self) -> "str":
        return "homeassistant.svg"

    @property
    def title(self) -> "str":
        return "Home Assistant"

    @property
    def primary_color(self) -> "str":
        return "#18BCF2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Home Assistant</title>
     <path d="M22.939 10.627 13.061.749a1.505 1.505 0 0 0-2.121
 0l-9.879 9.878C.478 11.21 0 12.363 0 13.187v9c0 .826.675 1.5 1.5
 1.5h9.227l-4.063-4.062a2.034 2.034 0 0 1-.664.113c-1.13
 0-2.05-.92-2.05-2.05s.92-2.05 2.05-2.05 2.05.92 2.05 2.05c0
 .233-.041.456-.113.665l3.163 3.163V9.928a2.05 2.05 0 0
 1-1.15-1.84c0-1.13.92-2.05 2.05-2.05s2.05.92 2.05 2.05a2.05 2.05 0 0
 1-1.15 1.84v8.127l3.146-3.146A2.051 2.051 0 0 1 18 12.239c1.13 0
 2.05.92 2.05 2.05s-.92 2.05-2.05 2.05c-.25 0-.488-.047-.709-.13L12.9
 20.602v3.088h9.6c.825 0 1.5-.675
 1.5-1.5v-9c0-.825-.477-1.977-1.061-2.561z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/home-assistant/assets/blob'''

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
