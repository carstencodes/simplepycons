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


class SmartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "smart"

    @property
    def original_file_name(self) -> "str":
        return "smart.svg"

    @property
    def title(self) -> "str":
        return "smart"

    @property
    def primary_color(self) -> "str":
        return "#D7E600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>smart</title>
     <path d="M10.85.846A11.138 11.138 0 0 0 0 11.979v.04a11.136
 11.136 0 0 0 10.844 11.135h.283a10.983 10.983 0 0 0
 4.041-.758.395.395 0 0 0 .256-.369v-5.564a.21.21 0 0
 0-.274-.195c-1.202.489-2.215.957-3.96.957a5.222 5.222 0 0 1-5.22-5.22
 5.22 5.22 0 0 1 5.22-5.22c1.745 0 2.758.467 3.96.955a.21.21 0 0 0
 .274-.193V1.979a.395.395 0 0 0-.256-.37 10.983 10.983 0 0
 0-4.037-.763Zm5.863 1.82v18.67a.238.238 0 0 0 .377.19c3.413-2.122
 6.91-8.16 6.91-9.52 0-1.36-3.497-7.396-6.91-9.522a.238.238 0 0
 0-.377.182Z" />
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
