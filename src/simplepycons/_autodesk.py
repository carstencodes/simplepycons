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


class AutodeskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autodesk"

    @property
    def original_file_name(self) -> "str":
        return "autodesk.svg"

    @property
    def title(self) -> "str":
        return "Autodesk"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Autodesk</title>
     <path d="m.129 20.202 14.7-9.136h7.625c.235 0 .445.188.445.445 0
 .21-.092.305-.21.375l-7.222 4.323c-.47.283-.633.845-.633 1.265l-.008
 2.725H24V4.362a.561.561 0 0 0-.585-.562h-8.752L0 12.893V20.2h.129z"
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
