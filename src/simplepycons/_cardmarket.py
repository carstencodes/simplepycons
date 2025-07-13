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


class CardmarketIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cardmarket"

    @property
    def original_file_name(self) -> "str":
        return "cardmarket.svg"

    @property
    def title(self) -> "str":
        return "Cardmarket"

    @property
    def primary_color(self) -> "str":
        return "#012169"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cardmarket</title>
     <path d="M14.837.772c-.45
 0-.6.255-.645.366-.044.11-.113.4.213.711l1.54 1.478a.124.124 0 0 1
 .002.18L10.021 9.47a.934.934 0 0 0-.274.673.936.936 0 0 0
 .289.669l3.977 3.82a.955.955 0 0 0 .664.267v.001c.259 0
 .5-.1.68-.281l5.815-5.853a.142.142 0 0 1 .103-.042c.023 0
 .065.005.1.04l1.54 1.478c.198.19.383.23.504.23.277 0
 .577-.217.577-.691L24 1.726a.951.951 0 0
 0-.95-.95zm-8.06.793-2.351.461s-.365.064-.606.428c-.192.286-.124.616-.124.616l3.082
 14.66V1.566ZM2.843 4.907v.001L.52
 5.752s-.308.106-.445.452c-.15.385-.03.634-.03.634L6.04
 23.224h.86C6.559 21.8 2.843 4.907 2.843 4.907ZM23.31 12.63a.59.59 0 0
 0-.417.175l-6.716 6.787a.976.976 0 0
 0-.287.706c.004.267.11.515.303.7l1.084 1.046-7.668-.006.005-7.574
 2.473 2.494a.592.592 0 0 0 .835.004.59.59 0 0 0
 .004-.835l-3.2-3.227c-.246-.25-.562-.33-.843-.214-.282.116-.45.396-.45.747l-.006
 8.794c0 .266.103.515.291.703a.986.986 0 0 0
 .702.291l8.92.007v-.002c.354 0
 .633-.168.747-.45.114-.283.03-.599-.224-.845l-1.708-1.647
 6.578-6.648a.591.591 0 0 0-.005-.835.589.589 0 0 0-.418-.17z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simple-icons/simple-icons/'''

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
