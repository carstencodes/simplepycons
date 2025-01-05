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


class BetterStackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "betterstack"

    @property
    def original_file_name(self) -> "str":
        return "betterstack.svg"

    @property
    def title(self) -> "str":
        return "Better Stack"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Better Stack</title>
     <path d="m.7792 10.7479-.7654 6.6384a2.0957 2.0957 0 0 0 .696
 1.8122l1.8965 1.672c.6494.5725 1.658.0145 1.5185-.84L2.6039
 10.705c-.1723-1.056-1.7022-1.02-1.8247.0429Zm12.3733 8.714L8.63
 6.431c-.5023-1.4472-2.6082-1.3845-3.0203.0898l-1.376
 4.9234c-.156.559-.216.8822.0005 1.4212h.5225l1.8993
 6.0694c.294.7324.9017 1.3009 1.6611 1.5538l2.8315.9435c1.2417.4137
 2.4268-.7513 2.004-1.97zm10.6297-1.0332L15.7907
 3.4433c-.6971-1.3072-2.5779-1.2727-3.227.0589l-1.9652
 3.9555c-.2375.487-.1274.6608.07.9435.1585.2268.526.2447.6758.012.147-.2287.488-.2076.6058.0375l5.1379
 10.687a2.735 2.735 0 0 0 2.1416 1.6016l2.7183.3476c1.4628.1924
 2.5299-1.3539 1.8343-2.6582z" />
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
