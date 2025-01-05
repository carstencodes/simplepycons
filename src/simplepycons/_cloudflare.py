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


class CloudflareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cloudflare"

    @property
    def original_file_name(self) -> "str":
        return "cloudflare.svg"

    @property
    def title(self) -> "str":
        return "Cloudflare"

    @property
    def primary_color(self) -> "str":
        return "#F38020"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cloudflare</title>
     <path d="M16.5088
 16.8447c.1475-.5068.0908-.9707-.1553-1.3154-.2246-.3164-.6045-.499-1.0615-.5205l-8.6592-.1123a.1559.1559
 0 0
 1-.1333-.0713c-.0283-.042-.0351-.0986-.021-.1553.0278-.084.1123-.1484.2036-.1562l8.7359-.1123c1.0351-.0489
 2.1601-.8868
 2.5537-1.9136l.499-1.3013c.0215-.0561.0293-.1128.0147-.168-.5625-2.5463-2.835-4.4453-5.5499-4.4453-2.5039
 0-4.6284 1.6177-5.3876
 3.8614-.4927-.3658-1.1187-.5625-1.794-.499-1.2026.119-2.1665
 1.083-2.2861 2.2856-.0283.31-.0069.6128.0635.894C1.5683 13.171 0
 14.7754 0 16.752c0
 .1748.0142.3515.0352.5273.0141.083.0844.1475.1689.1475h15.9814c.0909
 0 .1758-.0645.2032-.1553l.12-.4268zm2.7568-5.5634c-.0771 0-.1611
 0-.2383.0112-.0566 0-.1054.0415-.127.0976l-.3378
 1.1744c-.1475.5068-.0918.9707.1543 1.3164.2256.3164.6055.498
 1.0625.5195l1.8437.1133c.0557 0
 .1055.0263.1329.0703.0283.043.0351.1074.0214.1562-.0283.084-.1132.1485-.204.1553l-1.921.1123c-1.041.0488-2.1582.8867-2.5527
 1.914l-.1406.3585c-.0283.0713.0215.1416.0986.1416h6.5977c.0771 0
 .1474-.0489.169-.126.1122-.4082.1757-.837.1757-1.2803
 0-2.6025-2.125-4.727-4.7344-4.727" />
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
