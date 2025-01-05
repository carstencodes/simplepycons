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


class XiaomiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "xiaomi"

    @property
    def original_file_name(self) -> "str":
        return "xiaomi.svg"

    @property
    def title(self) -> "str":
        return "Xiaomi"

    @property
    def primary_color(self) -> "str":
        return "#FF6900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Xiaomi</title>
     <path d="M12 0C8.016 0 4.756.255 2.493 2.516.23 4.776 0 8.033 0
 12.012c0 3.98.23 7.235 2.494 9.497C4.757 23.77 8.017 24 12 24c3.983 0
 7.243-.23 9.506-2.491C23.77 19.247 24 15.99 24
 12.012c0-3.984-.233-7.243-2.502-9.504C19.234.252 15.978 0 12 0zM4.906
 7.405h5.624c1.47 0 3.007.068 3.764.827.746.746.827 2.233.83
 3.676v4.54a.15.15 0 0 1-.152.147h-1.947a.15.15 0 0
 1-.152-.148V11.83c-.002-.806-.048-1.634-.464-2.051-.358-.36-1.026-.441-1.72-.458H7.158a.15.15
 0 0 0-.151.147v6.98a.15.15 0 0 1-.152.148H4.906a.15.15 0 0
 1-.15-.148V7.554a.15.15 0 0 1 .15-.149zm12.131 0h1.949a.15.15 0 0 1
 .15.15v8.892a.15.15 0 0 1-.15.148h-1.949a.15.15 0 0
 1-.151-.148V7.554a.15.15 0 0 1 .151-.149zM8.92 10.948h2.046c.083 0
 .15.066.15.147v5.352a.15.15 0 0 1-.15.148H8.92a.15.15 0 0
 1-.152-.148v-5.352a.15.15 0 0 1 .152-.147Z" />
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
