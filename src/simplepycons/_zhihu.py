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


class ZhihuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zhihu"

    @property
    def original_file_name(self) -> "str":
        return "zhihu.svg"

    @property
    def title(self) -> "str":
        return "Zhihu"

    @property
    def primary_color(self) -> "str":
        return "#0084FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zhihu</title>
     <path d="M5.721 0C2.251 0 0 2.25 0 5.719V18.28C0 21.751 2.252 24
 5.721 24h12.56C21.751 24 24 21.75 24 18.281V5.72C24 2.249 21.75 0
 18.281 0zm1.964 4.078c-.271.73-.5 1.434-.68 2.11h4.587c.545-.006.445
 1.168.445 1.171H9.384a58.104 58.104 0 01-.112
 3.797h2.712c.388.023.393 1.251.393 1.266H9.183a9.223 9.223 0 01-.408
 2.102l.757-.604c.452.456 1.512 1.712 1.906 2.177.473.681.063
 2.081.063 2.081l-2.794-3.382c-.653 2.518-1.845 3.607-1.845
 3.607-.523.468-1.58.82-2.64.516 2.218-1.73 3.44-3.917
 3.667-6.497H4.491c0-.015.197-1.243.806-1.266h2.71c.024-.32.086-3.254.086-3.797H6.598c-.136.406-.158.447-.268.753-.594
 1.095-1.603 1.122-1.907 1.155.906-1.821 1.416-3.6
 1.591-4.064.425-1.124 1.671-1.125 1.671-1.125zM13.078
 6h6.377v11.33h-2.573l-2.184 1.373-.401-1.373h-1.219zm1.313
 1.219v8.86h.623l.263.937 1.455-.938h1.456v-8.86z" />
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
