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


class MuoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "muo"

    @property
    def original_file_name(self) -> "str":
        return "muo.svg"

    @property
    def title(self) -> "str":
        return "MUO"

    @property
    def primary_color(self) -> "str":
        return "#C60D0D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MUO</title>
     <path d="M4.887 6.016 0
 10.903v7.048h19.108l4.873-4.874v-7.06Zm5.46 3.57a.295.295 0 0 1
 .314.314v3.652h3V9.9a.303.303 0 0 1 .331-.314.295.295 0 0 1
 .315.314v3.72a.506.506 0 0 1-.56.552h-3.18a.502.502 0 0
 1-.551-.552V9.9a.303.303 0 0 1 .33-.314zm-5.113.041a.597.597 0 0 1
 .465.22l1.638 1.99L8.96 9.81a.47.47 0 0 1 .378-.183h.164a.18.18 0 0 1
 .183.183.193.193 0 0 1-.046.128L7.668 12.4a.433.433 0 0
 1-.33.19.443.443 0 0 1-.323-.185l-1.45-1.753v3.246a.303.303 0 0
 1-.331.315.295.295 0 0 1-.315-.315V9.942a.295.295 0 0 1
 .315-.315zm9.942 0h3.334a.502.502 0 0 1 .552.552v3.44a.502.502 0 0
 1-.552.553h-3.334a.502.502 0 0 1-.552-.552v-3.44a.502.502 0 0 1
 .552-.553zm.093.62v3.304h3.148v-3.303zm-5.775.584c.032 0
 .191.012.191.25v2.817a.303.303 0 0 1-.33.315.295.295 0 0
 1-.315-.315V11.49a.591.591 0 0 1
 .133-.378l.131-.164.012-.013c.058-.058.104-.104.178-.104zM24
 14.498l-3.486 3.486H24Z" />
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
        yield from [
            "MakeUseOf",
        ]
