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


class AiohttpIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aiohttp"

    @property
    def original_file_name(self) -> "str":
        return "aiohttp.svg"

    @property
    def title(self) -> "str":
        return "AIOHTTP"

    @property
    def primary_color(self) -> "str":
        return "#2C5BB4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AIOHTTP</title>
     <path d="M0 12C.01 5.377 5.377.01 12 0c6.623.01 11.99 5.377 12
 12-.01 6.623-5.377 11.99-12 12C5.377 23.99.01 18.623 0 12zm12
 11.004a10.948 10.948 0 0 0 6.81-2.367l-.303-.656a.746.746 0 0
 1-.621-1.347l-.722-1.563a1.244 1.244 0 0
 1-1.543-.734l-2.474.633v.012a.747.747 0 1 1-1.475-.178L8.2
 15.31a1.244 1.244 0 0 1-1.278.607l-.748 2.59a.747.747 0 0 1-.17
 1.388l.052 1.36A10.935 10.935 0 0 0 12 23.003zM5.75
 21.05l-.044-1.142a.747.747 0 0 1 .18-1.482l.749-2.59a1.245 1.245 0 0
 1-.759-1.147l-4.674-.566A11.035 11.035 0 0 0 5.75
 21.05zm13.3-.608a11.083 11.083 0 0 0 2.74-3.421l-3.826-.751a1.245
 1.245 0 0 1-.528.672l.732 1.588a.747.747 0 0 1 .598
 1.3l.285.612zm2.878-3.698A10.934 10.934 0 0 0 23.004 12a10.95 10.95 0
 0 0-2.492-6.965L19 5.551a.749.749 0 0 1-.726.922.747.747 0 0
 1-.682-.442L14.449 7.1a2.492 2.492 0 0 1-1.015 2.737l2.857
 4.901a1.245 1.245 0 0 1 1.732
 1.236l3.904.77zm-8.846-.068l2.465-.63a1.242 1.242 0 0 1
 .486-1.157l-2.856-4.9a2.478 2.478 0 0 1-2.444-.11l-2.77 3.892a1.242
 1.242 0 0 1 .354 1.263l3.483 1.497a.746.746 0 0 1
 1.282.143v.002zm-7.17-2.284a1.246 1.246 0 0 1
 1.81-.794l2.77-3.89a2.484 2.484 0 0
 1-.93-1.94c0-.603.219-1.186.617-1.64L6.476 2.487a11.013 11.013 0 0
 0-5.33 11.328l4.765.578zm8.44-7.572l3.174-1.083v-.01a.747.747 0 0 1
 1.345-.448l1.433-.489A10.982 10.982 0 0 0 6.745 2.333l3.64 3.581a2.49
 2.49 0 0 1 3.967.904l-.002.003z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/aio-libs/aiohttp/blob/fb5f'''

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
