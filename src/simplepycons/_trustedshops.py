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


class TrustedShopsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "trustedshops"

    @property
    def original_file_name(self) -> "str":
        return "trustedshops.svg"

    @property
    def title(self) -> "str":
        return "Trusted Shops"

    @property
    def primary_color(self) -> "str":
        return "#FFDC0F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Trusted Shops</title>
     <path d="M15.187 14.332c-1.1 1.626-2.63 3.108-4.687 3.108-2.175
 0-3.442-1.362-3.442-3.562 0-3.561 2.63-7.052 6.335-7.052 1.242 0
 2.916.502 2.916 2.009 0 2.7-4.231 3.609-6.311
 4.135-.072.457-.143.908-.143 1.362 0 .933.501 1.793 1.53 1.793 1.338
 0 2.412-1.29 3.203-2.247zm-1.148-5.808c0-.55-.31-.978-.884-.978-1.722
 0-2.608 3.346-2.94 4.66 1.601-.48 3.824-1.794 3.824-3.682zM12 0a12 12
 0 1 0 12 11.997A11.997 11.997 0 0 0 12 0zm-.1 19.523a7.563 7.563 0 1
 1 7.564-7.563 7.563 7.563 0 0 1-7.563 7.56Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brand.trustedshops.com/d/dorIFVeUmcN9'''

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
