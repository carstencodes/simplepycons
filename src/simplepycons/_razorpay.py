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


class RazorpayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "razorpay"

    @property
    def original_file_name(self) -> "str":
        return "razorpay.svg"

    @property
    def title(self) -> "str":
        return "Razorpay"

    @property
    def primary_color(self) -> "str":
        return "#0C2451"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Razorpay</title>
     <path d="M22.436 0l-11.91 7.773-1.174 4.276 6.625-4.297L11.65
 24h4.391l6.395-24zM14.26 10.098L3.389 17.166 1.564
 24h9.008l3.688-13.902Z" />
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
