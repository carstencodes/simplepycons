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


class GskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gsk"

    @property
    def original_file_name(self) -> "str":
        return "gsk.svg"

    @property
    def title(self) -> "str":
        return "GSK"

    @property
    def primary_color(self) -> "str":
        return "#F36633"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>GSK</title>
     <path d="M16.769 13.5v2.114h1.49V12.3c0-.15.115-.174.2-.093l3.512
 3.408H24L20.279 12 24 8.384h-2.034l-3.512
 3.408c-.081.081-.2.058-.2-.093V8.384h-1.485v2.125c0 .763.5 1.225
 1.386 1.468.035.011.035.046 0 .057-.89.243-1.386.705-1.386
 1.466ZM8.323 11.191c0 .924.774 1.5 1.825 1.5h3.535a.388.388 0 0 1
 .416.416v.6a.388.388 0 0 1-.416.416H8.7v1.49h5.014a1.793 1.793 0 0 0
 1.837-1.838v-.657a1.791 1.791 0 0 0-1.836-1.837H10.2a.388.388 0 0
 1-.416-.416v-.717a.255.255 0 0 1 .277-.277h4.9V8.384H10.76a1.011
 1.011 0 0 0-1.016 1V9.8a.067.067 0 0 1-.065.069h-.005a1.269 1.269 0 0
 0-1.351 1.322ZM6.666 11.284H4.274v.448a.957.957 0 0 0
 .951.962h.585v1.155a.278.278 0 0 1-.278.277H1.907a.416.416 0 0
 1-.416-.416v-3.42a.415.415 0 0 1 .415-.416H5.8v-1.49h-4a1.8 1.8 0 0
 0-1.8 1.8v3.635a1.8 1.8 0 0 0 1.8 1.8h3.017A1.018 1.018 0 0 0 5.834
 14.6v-.4a.067.067 0 0 1 .065-.07c.808-.023 1.328-.416
 1.328-1.1v-1.746Z" />
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
            "GlaxoSmithKline",
        ]
