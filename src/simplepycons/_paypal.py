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


class PaypalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paypal"

    @property
    def original_file_name(self) -> "str":
        return "paypal.svg"

    @property
    def title(self) -> "str":
        return "PayPal"

    @property
    def primary_color(self) -> "str":
        return "#002991"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PayPal</title>
     <path d="M15.607 4.653H8.941L6.645 19.251H1.82L4.862
 0h7.995c3.754 0 6.375 2.294 6.473
 5.513-.648-.478-2.105-.86-3.722-.86m6.57 5.546c0 3.41-3.01
 6.853-6.958 6.853h-2.493L11.595 24H6.74l1.845-11.538h3.592c4.208 0
 7.346-3.634 7.153-6.949a5.24 5.24 0 0 1 2.848 4.686M9.653
 5.546h6.408c.907 0 1.942.222 2.363.541-.195 2.741-2.655 5.483-6.441
 5.483H8.714Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://newsroom.paypal-corp.com/media-resour'''
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
