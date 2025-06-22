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


class BookingdotcomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bookingdotcom"

    @property
    def original_file_name(self) -> "str":
        return "bookingdotcom.svg"

    @property
    def title(self) -> "str":
        return "Booking.com"

    @property
    def primary_color(self) -> "str":
        return "#003A9A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Booking.com</title>
     <path d="M24 0H0v24h24ZM8.575 6.563h2.658c2.108 0 3.473 1.15
 3.473 2.898 0 1.15-.575 1.82-.91 2.108l-.287.263.335.192c.815.479
 1.318 1.389 1.318 2.395 0 1.988-1.51 3.257-3.857
 3.257H7.449V7.713c0-.623.503-1.126 1.126-1.15zm1.7
 1.868c-.479.024-.694.264-.694.79v1.893h1.676c.958 0 1.294-.743
 1.294-1.365 0-.815-.503-1.318-1.318-1.318zm-.096
 4.36c-.407.071-.598.31-.598.79v2.251h1.868c.934 0 1.509-.55
 1.509-1.533 0-.934-.599-1.509-1.51-1.509zm7.737 2.394c.743 0
 1.341.599 1.341 1.342a1.34 1.34 0 0 1-1.341 1.341 1.355 1.355 0 0
 1-1.341-1.341c0-.743.598-1.342 1.34-1.342z" />
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
