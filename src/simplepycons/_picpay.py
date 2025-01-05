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


class PicpayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "picpay"

    @property
    def original_file_name(self) -> "str":
        return "picpay.svg"

    @property
    def title(self) -> "str":
        return "PicPay"

    @property
    def primary_color(self) -> "str":
        return "#21C25E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PicPay</title>
     <path d="M16.463 1.587v7.537H24V1.587zm1.256
 1.256h5.025v5.025h-5.025zm1.256 1.256v2.513h2.513V4.099zM3.77
 5.355V8.53h3.376c2.142 0 3.358 1.04 3.358 2.939 0 1.947-1.216
 3.011-3.358 3.011H3.769V8.53H0v13.884h3.769v-4.76h3.57c4.333 0
 6.815-2.352 6.815-6.32 0-3.771-2.482-5.978-6.814-5.978Z" />
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
