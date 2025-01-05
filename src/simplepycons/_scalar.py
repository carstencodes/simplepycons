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


class ScalarIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scalar"

    @property
    def original_file_name(self) -> "str":
        return "scalar.svg"

    @property
    def title(self) -> "str":
        return "Scalar"

    @property
    def primary_color(self) -> "str":
        return "#1A1A1A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scalar</title>
     <path d="M14.044 0c.243 0
 .486.202.486.486v5.423l3.804-3.845c.202-.202.526-.202.688 0l2.914
 2.914c.162.162.202.486 0 .648v.04L18.09 9.47h5.423c.284 0
 .486.203.486.486v4.088a.468.468 0 0 1-.486.486h-5.423l3.845
 3.804c.162.202.202.526 0 .688l-2.914 2.914c-.162.162-.486.202-.648
 0h-.04L14.53 18.09v5.423a.468.468 0 0 1-.486.486H9.956a.468.468 0 0
 1-.486-.486v-2.833c0-.89.365-1.74.972-2.388l5.261-5.261a1.466 1.466 0
 0 0 0-2.064l-5.22-5.221A3.4 3.4 0 0 1 9.47
 3.359V.486c0-.284.203-.486.486-.486h4.088ZM5.585 2.105h.04l8.864
 8.863a1.466 1.466 0 0 1 0 2.064l-8.863 8.904c-.162.202-.486.202-.688
 0l-2.874-2.833c-.162-.203-.202-.486 0-.688L5.91 14.53H.486A.468.468 0
 0 1 0 14.043V9.956c0-.283.202-.486.486-.486h5.423L2.064
 5.666a.548.548 0 0 1 0-.688l2.874-2.873a.421.421 0 0 1 .647 0Z" />
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
