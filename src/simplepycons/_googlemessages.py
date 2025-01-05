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


class GoogleMessagesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlemessages"

    @property
    def original_file_name(self) -> "str":
        return "googlemessages.svg"

    @property
    def title(self) -> "str":
        return "Google Messages"

    @property
    def primary_color(self) -> "str":
        return "#1A73E8"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Messages</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0zM4.911 7.089h11.456a2.197 2.197 0 0 1 2.165
 2.19v5.863a2.213 2.213 0 0 1-2.177 2.178H8.04c-1.174
 0-2.04-.99-2.04-2.178v-4.639L4.503
 7.905c-.31-.42-.05-.816.408-.816zm3.415 2.19c-.347 0-.68.21-.68.544 0
 .334.333.544.68.544h7.905c.346 0 .68-.21.68-.544
 0-.334-.334-.545-.68-.545zm0 2.177c-.347 0-.68.21-.68.544 0
 .334.333.544.68.544h7.905c.346 0 .68-.21.68-.544
 0-.334-.334-.544-.68-.544zm-.013 2.19c-.346 0-.68.21-.68.544 0
 .334.334.544.68.544h5.728c.347 0 .68-.21.68-.544
 0-.334-.333-.545-.68-.545z" />
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
