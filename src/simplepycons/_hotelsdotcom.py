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


class HotelsdotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hotelsdotcom"

    @property
    def original_file_name(self) -> "str":
        return "hotelsdotcom.svg"

    @property
    def title(self) -> "str":
        return "Hotels.com"

    @property
    def primary_color(self) -> "str":
        return "#EF3346"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hotels.com</title>
     <path d="M19.064 0H4.936a4.937 4.937 0 0 0-4.93 4.93V19.06A4.94
 4.94 0 0 0 4.935 24h14.128a4.926 4.926 0 0 0 4.93-4.941V4.93A4.93
 4.93 0 0 0 19.065 0zM8.55 10.63v2.329a.32.32 0 0
 1-.337.337H5.884a.32.32 0 0
 1-.337-.337V10.63c0-.2.137-.337.337-.337h2.34c.2 0
 .336.137.336.337h-.01zm5.162 7.491a.32.32 0 0
 1-.337.337h-2.328a.32.32 0 0
 1-.337-.337v-2.328c0-.2.136-.337.337-.337h2.328c.19 0
 .337.136.337.337v2.328zm0-5.162a.32.32 0 0 1-.337.337h-2.328a.32.32 0
 0 1-.337-.337V10.63c0-.2.136-.337.337-.337h2.328c.2 0
 .337.137.337.337v2.329zm5.974 4.372a.654.654 0 0 1-.22.516l-2.308
 2.297c-.18.168-.432.052-.432-.2V7.28H4.062c-.253
 0-.369-.264-.2-.432L6.169
 4.55c.137-.147.274-.232.506-.232h11.473c.854 0 1.538.685 1.538
 1.539V17.33z" />
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
