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


class NzxtIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nzxt"

    @property
    def original_file_name(self) -> "str":
        return "nzxt.svg"

    @property
    def title(self) -> "str":
        return "NZXT"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NZXT</title>
     <path d="M1.763 8.936l2.101
 3.04-.002-3.04h1.773v6.128H3.99l-2.218-3.227v3.227H0V8.936zm22.237
 0v1.614h-1.612v4.514h-1.883V10.55h-1.611V8.936H24zm-9.598 0l.996
 1.573 1.061-1.573h1.947l-1.98 3.034 2.013
 3.094h-2.063l-1.005-1.558-.99
 1.558h-2.015l1.975-3.038-2.004-3.09h2.065zm-2.652 0L9.327
 13.51h2.372v1.554H6.573l2.379-4.584H6.704V8.936h5.046z" />
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
