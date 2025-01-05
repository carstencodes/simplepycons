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


class SharexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sharex"

    @property
    def original_file_name(self) -> "str":
        return "sharex.svg"

    @property
    def title(self) -> "str":
        return "ShareX"

    @property
    def primary_color(self) -> "str":
        return "#2885F1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ShareX</title>
     <path d="M5.217 15.774v.054c.083 3.469 2.543 6.416 5.99
 7.607h-.002c1.095.377 2.246.568 3.404.565 5.159 0 9.347-3.697
 9.389-8.275a7.49 7.49 0 0 0-.563-2.668c-1.19 3.446-4.138 5.906-7.607
 5.987h-.176c-2.01
 0-3.854-.8-5.294-2.13-1.656-1.53-2.78-3.765-3.01-6.295-1.3
 1.407-2.093 3.2-2.13 5.155Zm3.01-10.557H8.17c-3.36.08-6.23 2.39-7.49
 5.669l-.117.32A10.408 10.408 0 0 0 0 14.608c0 5.159 3.697 9.347 8.275
 9.389a7.49 7.49 0 0 0
 2.668-.563c-3.446-1.19-5.906-4.138-5.987-7.607v-.176c0-2.01.8-3.854
 2.13-5.296 1.53-1.656 3.765-2.78
 6.296-3.01-1.407-1.3-3.2-2.093-5.155-2.129Zm7.601
 13.566.324-.015c3.327-.223 6.129-2.636 7.283-5.974A10.36 10.36 0 0 0
 24 9.392c0-5.16-3.697-9.347-8.275-9.39a7.49 7.49 0 0
 0-2.668.563c3.446 1.19 5.906 4.14 5.987 7.607v.176c0 2.01-.8
 3.854-2.13 5.294-1.53 1.656-3.765 2.78-6.295 3.01 1.407 1.3 3.2 2.094
 5.155 2.13zM.002 8.275a7.49 7.49 0 0 0 .563 2.668c1.19-3.446
 4.14-5.906 7.607-5.987h.176c2.01 0 3.854.8 5.294
 2.13.334.31.643.643.925.999 1.146 1.436 1.9 3.27 2.085 5.297
 1.3-1.407 2.094-3.2 2.13-5.155V8.17C18.7 4.703 16.24 1.756
 12.795.564A10.408 10.408 0 0 0 9.393 0C4.23 0 .045 3.697.002 8.275Z"
 />
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
