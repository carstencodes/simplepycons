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


class RenrenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "renren"

    @property
    def original_file_name(self) -> "str":
        return "renren.svg"

    @property
    def title(self) -> "str":
        return "Renren"

    @property
    def primary_color(self) -> "str":
        return "#217DC6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Renren</title>
     <path d="M5.66 9.553V5.254A6.794 6.794 0 0 0 1.606
 16.34c2.379-1.152 4.042-3.755 4.054-6.787zm1.132 4.115c-.423
 1.752-1.687 3.25-3.262 4.245a6.76 6.76 0 0 0 3.26.833 6.772 6.772 0 0
 0 3.264-.833c-1.575-.996-2.84-2.494-3.262-4.245zm5.184-6.103a6.79
 6.79 0 0 0-4.052-2.31V9.52c0 3.045 1.667 5.663 4.051 6.818a6.767
 6.767 0 0 1-1.607-4.387 6.755 6.755 0 0 1 1.608-4.386zc1.003 1.183
 1.655 2.714 1.655 4.387 0 1.674-.65 3.203-1.655 4.388 2.38-1.15
 4.088-3.755 4.1-6.787V5.254a6.9 6.901 0 0 0-4.1 2.31zM18.34 9.52c0
 3.046 1.667 5.663 4.053 6.82A6.793 6.793 0 0 0 18.34 5.255zm-1.132
 4.148c-.423 1.752-1.687 3.25-3.263 4.245a6.76 6.76 0 0 0 3.262.833
 6.772 6.772 0 0 0 3.263-.833c-1.575-.996-2.839-2.494-3.262-4.245z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://seeklogo.com/vector-logo/184137/renre'''

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
