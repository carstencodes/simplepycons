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


class ShenzhenMetroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shenzhenmetro"

    @property
    def original_file_name(self) -> "str":
        return "shenzhenmetro.svg"

    @property
    def title(self) -> "str":
        return "Shenzhen Metro"

    @property
    def primary_color(self) -> "str":
        return "#009943"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shenzhen Metro</title>
     <path d="M.27 0v.155c0 4.69 3.033 8.751 7.331 10.434v2.736C3.303
 14.99.271 19.019.271 23.768V24H4.36v-.232c0-2.459 1.278-4.623
 3.24-5.934V24h3.165v-7.384c.408-.065.82-.098 1.234-.1.423 0 .834.038
 1.235.1V24h3.165v-6.148c1.925 1.313 3.163 3.469 3.163
 5.916V24h4.168v-.232c0-4.691-3.033-8.751-7.331-10.434V10.6c4.298-1.665
 7.33-5.696 7.33-10.446V.001h-4.09v.154c0 2.458-1.277 4.622-3.24
 5.934V0h-3.165v7.305c-.408.066-.821.1-1.235.103a8.11 8.11 0 0
 1-1.234-.103V.001H7.6V6.07C5.675 4.757 4.438 2.602
 4.438.154V.001zm10.495 11.358c.82.084 1.648.084
 2.469.001v1.205a12.236 12.236 0 0 0-2.47 0z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://en.wikipedia.org/wiki/File:Shenzhen_M'''

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
